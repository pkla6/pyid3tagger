# coding=utf-8

import tempfile

from tags import ID3v2_3Tag
import utilities


class FileTags(object):

    def __init__(self):
        self.__id3v1_tag = None
        self.__id3v1_1_tag = None
        self.__id3v2_tag = None
        self.__id3v2_3_tag = None
        self.__id3v2_4_start_tag = None
        self.__id3v2_4_end_tag = None

    @property
    def id3v2_3_tag(self):
        return self.__id3v2_3_tag

    @id3v2_3_tag.setter
    def id3v2_3_tag(self, value):
        if not isinstance(value, (ID3v2_3Tag, None)):
            raise  # todo
        self.__id3v2_3_tag = value

    def read(self, filename):
        pass  # todo

    def write(self, filename):
        with open(filename, 'rb') as origin_file:
            file_content = origin_file.read()
        temp_file = tempfile.TemporaryFile()
        temp_file.write(file_content)
        # remove v1 and v1_1 tags
        if len(file_content) > 128:
            temp_file.seek(-128, 2)
            if temp_file.read(3) == 'TAG':
                temp_file.seek(-128, 2)
                temp_file.truncate()

        temp_file.seek(0)
        id3v2_3_tag_data = self.id3v2_3_tag.generate()
        with open(filename, 'wb') as new_file:
            if self.id3v2_3_tag is not None:
                new_file.write(id3v2_3_tag_data)
            if temp_file.read(3) == 'ID3':
                version = ord(temp_file.read(1))
                temp_file.seek(2, 1)
                length = utilities.int_from_sync_save_bytes(temp_file.read(4))
                # todo 2v4 and footer available
                temp_file.seek(length, 1)
            else:
                temp_file.seek(0)
            # todo chuck wise
            new_file.write(temp_file.read())

        pass  # todo
