# coding=utf-8

import pyid3tagger.const as const


def guess_tags_versions(file_path):
    """

    :param file_path:
    :return: List of possible tag versions
    """

    versions = list()

    mp3_file = open(file_path)

    mp3_file.seek(-128, 2)  # todo make save
    if mp3_file.read(3) == 'TAG':
        versions.append(const.ID3v1_VERSION)
        versions.append(const.ID3v1_1_VERSION)

    mp3_file.seek(0)
    if mp3_file.read(3) == 'ID3':
        version_bytes = mp3_file.read(2)
        if version_bytes == '\x02\x00':
            versions.append(const.ID3v2_2_VERSION)
        elif version_bytes == '\x03\x00':
            versions.append(const.ID3v2_3_VERSION)
        elif version_bytes == '\x04\x00':
            versions.append(const.ID3v2_4_VERSION)

    # todo id3v2.4 tag at end of file

    return tuple(versions)


def remove_all_tags(file_path, preserve_file_stat=False):
    """
    Remove all ID3 tags from a file.
    :param file_path:
    :param preserve_file_stat:
    :return:
    """

    # todo
