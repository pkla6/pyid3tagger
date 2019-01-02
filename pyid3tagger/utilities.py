# coding=utf-8

import errno
import os
import stat
import tempfile

import pyid3tagger.const as const

__author__ = "Peter Klassen peter@mediadock.org"
__license__ = "MIT License"
__copyright__ = "(c) 2017 Peter Klassen peter@mediadock.org"


def guess_tags_versions(file_path):
    """

    :param file_path:
    :return: List of possible tag versions
    """

    versions = list()

    mp3_file = open(file_path, 'rb')

    try:
        mp3_file.seek(-128, 2)  # todo make save
    except:
        pass
    else:
        if mp3_file.read(3) == 'TAG':
            mp3_file.seek(-3, 2)
            if mp3_file.read(1) == '\x00':  # todo test
                if mp3_file.read(1) == '\x00':
                    versions.append(const.ID3v1_1_VERSION)
                    versions.append(const.ID3v1_VERSION)
                else:
                    versions.append(const.ID3v1_1_VERSION)
            else:
                versions.append(const.ID3v1_VERSION)

    mp3_file.seek(0)
    if mp3_file.read(3) == 'ID3':
        version_bytes = mp3_file.read(2)
        if version_bytes == '\x02\x00':
            versions.append(const.ID3v2_2_VERSION)
        elif version_bytes == '\x03\x00':
            versions.append(const.ID3v2_3_VERSION)
        elif version_bytes == '\x04\x00':
            versions.append(const.ID3v2_4_VERSION)

    mp3_file.close()

    if get_ID3_2_4_end_tag_start_positions(file_path):
        versions.append(const.ID3v2_4_VERSION)

    return tuple(versions)


def has_ID3_2_4_begin_tag(file_path):  # todo test
    mp3_file = open(file_path, 'rb')
    return mp3_file.read(5) == '\x73\x68\x51\x04\x00'


def get_ID3_2_4_end_tag_start_positions(file_path):  # todo test
    """

    :param file_path:
    :return:
    """
    read_length = 1024
    positions = list()
    start_positions = list()

    mp3_file = open(file_path, 'rb')
    # miss the first 'I'
    mp3_file.read(1)

    # find the starting 'I'
    chunk = mp3_file.read(read_length)
    count = 0
    while chunk:
        positions += [position * count + 1 for position, char in enumerate(chunk) if char == 'I']
        count += 1
        chunk = mp3_file.read(read_length)

    for position in positions:
        mp3_file.seek(position)
        if mp3_file.read(5) == '\x73\x68\x51\x04\x00':  # todo check end tag 3DI
            start_positions.append(position)

    return tuple(start_positions)


def remove_all_tags(file_path, preserve_file_stat=False):
    """
    Remove all ID3 tags from a file.
    :param file_path:
    :param preserve_file_stat:
    :return:
    """

    remove_ID3_1_tag(file_path, preserve_file_stat)

    # todo


def remove_ID3_1_tag(file_path, preserve_file_stat=False):  # todo test
    """

    :param file_path:
    :param preserve_file_stat:
    :return:
    """

    file_stat, mode = _read_file_stat(file_path)

    mp3_file = open(file_path, 'rb+')
    mp3_file.seek(-128, 2)
    if mp3_file.read(3) == 'TAG':
        mp3_file.seek(-128, 2)
        mp3_file.truncate()
    mp3_file.close()

    if preserve_file_stat:
        _write_file_stat(file_path, stat, mode)


def _read_file_stat(file_path):  # todo test
    """

    :param file_path:
    :return:
    """
    file_stat = os.stat(file_path)
    mode = stat.S_IMODE(file_stat.st_mode)
    return file_stat, mode


def _write_file_stat(file_path, file_stat, mode):  # todo test
    if hasattr(os, 'utime'):
        os.utime(file_path, (file_stat.st_atime, file_stat.st_mtime))
    if hasattr(os, 'chmod'):
        os.chmod(file_path, mode)
    if hasattr(os, 'chflags') and hasattr(file_stat, 'st_flags'):
        try:
            os.chflags(file_path, file_stat.st_flags)
        except OSError, why:
            for err in 'EOPNOTSUPP', 'ENOTSUP':
                if hasattr(errno, err) and why.errno == getattr(errno, err):
                    break
            else:
                raise


def int_from_sync_save_byte(byte):
    integer = ord(byte)
    if integer > 127:
        raise  # todo
    return integer


def int_from_sync_save_bytes(bytes):  # todo test
    counter = 0
    integer = 0
    for byte in bytes[::-1]:
        integer =  (int_from_sync_save_byte(byte) * 2 ** (7 * counter)) + integer
        counter += 1
    return integer


def int_to_sync_save_byte(integer):  # todo test
    if integer > 127:
        raise  # todo
    return chr(integer)


def int_to_byte(integer):  # todo test
    if integer > 2 ** 8 - 1:
        raise  # todo
    return chr(integer)


def int_to_four_sync_save_bytes(integer):  # todo test
    if integer > 268435456:
        raise  # todo
    b1_3, b4 = divmod(integer, 128)
    b1_2, b3 = divmod(b1_3, 128)
    b1, b2 = divmod(b1_2, 128)
    byte_string = int_to_sync_save_byte(b1) + int_to_sync_save_byte(b2) + \
                  int_to_sync_save_byte(b3) + int_to_sync_save_byte(b4)
    return byte_string

def int_to_four_bytes(integer):  # todo test
    if integer >=  2 ** 32:
        raise  # todo
    b1_3, b4 = divmod(integer, 2 ** 8)
    b1_2, b3 = divmod(b1_3, 2 ** 8)
    b1, b2 = divmod(b1_2, 2 ** 8)
    byte_string = int_to_byte(b1) + int_to_byte(b2) + \
                  int_to_byte(b3) + int_to_byte(b4)
    return byte_string

def byte_to_bin(byte):  # todo test
    if len(byte) != 1:
        raise  # todo
    byte = '00000000' + bin(ord(byte))[2:]
    return byte[-8:]

def check_is_ISO_639_2_code(code):
    return code in const.LANGUAGE_CODES_ISO_639_2_DICT.keys()

def check_is_ISO_8859_1_text(text):
    if not isinstance(str, text):
        return False
    return all(['\x20' <= i <= '\xff' for i in text])

def check_is_ISO_8859_1_full_text(text):
    if not isinstance(str, text):
        return False
    return all([('\x20' <= i <= '\xff' or i == '\xa0') for i in text])
