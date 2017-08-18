# coding=utf-8

import struct

import pyid3tagger.const as const
import pyid3tagger.utilities as utilities

__author__ = "Peter Klassen peter@mediadock.org"
__license__ = "MIT License"
__copyright__ = "(c) 2017 Peter Klassen peter@mediadock.org"


class ID3v1BaseClass(object):

    base_tag = '%s' + '\x00' * 30

    def __init__(self):
        self.file_path = None
        self.title = ''
        self.artist = ''
        self.album = ''
        self.year = 1970
        self.comment = ''
        self.genre = 0

    def read(self, file_path):
        raise const.PyID3TaggerNotImplementedError('This should be implemented by the derived class')

    def write(self, file_path):
        raise const.PyID3TaggerNotImplementedError('This should be implemented by the derived class')


class ID3v1Tag(ID3v1BaseClass):
    pass

    def read(self, file_path):

        self.file_path = file_path

        try:
            mp3_file = open(file_path)
        except IOError:
            raise const.PyID3TaggerIOError(IOError.message)

        mp3_file.seek(-128, 2)
        if mp3_file.read(3) != 'TAG':
            raise const.PyID3TaggerInvalidData('File does not contain a ID3v1 Tag')
        self.title = mp3_file.read(30).split('\x00')[0]
        self.artist = mp3_file.read(30).split('\x00')[0]
        self.album = mp3_file.read(30).split('\x00')[0]
        self.year = int(mp3_file.read(4))
        self.comment = mp3_file.read(30).split('\x00')[0]
        self.genre = ord(mp3_file.read(1))

    def write(self, file_path=None):
        if not self.file_path and not file_path:
            raise  # todo
        if file_path:
            self.file_path = file_path
        utilities.remove_ID3_1_tag(file_path)

        try:
            mp3_file = open(file_path, 'a')
        except IOError:
            raise const.PyID3TaggerIOError(IOError.message)

        mp3_file.write('TAG')
        title_tag = self.base_tag % self.title
        mp3_file.write(title_tag[:30])
        artist_tag = self.base_tag % self.artist
        mp3_file.write(artist_tag[:30])
        album_tag = self.base_tag % self.album
        mp3_file.write(album_tag[:30])
        year_tag = '%04i' % self.year
        mp3_file.write(year_tag[:4])
        comment_tag = self.base_tag % self.comment
        mp3_file.write(comment_tag[:30])
        genre_tag = struct.pack('h', self.genre)
        mp3_file.write(genre_tag[0])

    # todo convert to other types


class ID3v1_1Tag(ID3v1BaseClass):

    def __init__(self):
        super(ID3v1_1Tag, self).__init__()
        self.track = 0

    def read(self, file_path):

        self.file_path = file_path

        try:
            mp3_file = open(file_path)
        except IOError:
            raise const.PyID3TaggerIOError(IOError.message)

        mp3_file.seek(-128, 2)
        if mp3_file.read(3) != 'TAG':
            raise const.PyID3TaggerInvalidData('File does not contain a ID3v1 Tag')
        self.title = mp3_file.read(30).split('\x00')[0]
        self.artist = mp3_file.read(30).split('\x00')[0]
        self.album = mp3_file.read(30).split('\x00')[0]
        self.year = int(mp3_file.read(4))
        self.comment = mp3_file.read(28).split('\x00')[0]
        empty_byte = mp3_file.read(1)
        if empty_byte != '\x00':
            raise const.PyID3TaggerInvalidData('')  # todo message
        self.track = ord(mp3_file.read(1))
        self.genre = ord(mp3_file.read(1))

    def write(self, file_path=None):
        if not self.file_path and not file_path:
            raise  # todo
        if file_path:
            self.file_path = file_path
        utilities.remove_ID3_1_tag(file_path)

        try:
            mp3_file = open(file_path, 'a')
        except IOError:
            raise const.PyID3TaggerIOError(IOError.message)

        mp3_file.write('TAG')
        title_tag = self.base_tag % self.title
        mp3_file.write(title_tag[:30])
        artist_tag = self.base_tag % self.artist
        mp3_file.write(artist_tag[:30])
        album_tag = self.base_tag % self.album
        mp3_file.write(album_tag[:30])
        year_tag = '%04i' % self.year
        mp3_file.write(year_tag[:4])
        comment_tag = self.base_tag % self.comment
        mp3_file.write(comment_tag[:28])
        mp3_file.write('\x00')
        track_tag = struct.pack('h', self.track)
        mp3_file.write(track_tag[0])
        genre_tag = struct.pack('h', self.genre)
        mp3_file.write(genre_tag[0])

    # todo convert to other types


class ID3v2BaseClass(object):
    pass
