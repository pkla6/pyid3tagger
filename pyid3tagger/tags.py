# coding=utf-8


import pyid3tagger.const as const
import pyid3tagger.utilities as utilities

__author__ = "Peter Klassen peter@mediadock.org"
__license__ = "MIT License"
__copyright__ = "(c) 2019 Peter Klassen peter@mediadock.org"


class ID3v1BaseClass(object):

    base_tag = '%s' + '\x00' * 30

    def __init__(self):
        self.file_path = None
        self.__title = ''
        self.__artist = ''
        self.__album = ''
        self.__year = 1970
        self.__comment = ''
        self.__genre = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise const.PyID3TaggerInvalidData('Title has to be a string')
        self.__title = title

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, artist):
        if not isinstance(artist, str):
            raise const.PyID3TaggerInvalidData('Artist has to be a string')
        self.__artist = artist

    @property
    def album(self):
        return self.__album

    @album.setter
    def album(self, album):
        if not isinstance(album, str):
            raise const.PyID3TaggerInvalidData('Album has to be a stirng')
        self.__album = album

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise const.PyID3TaggerInvalidData('Year has to be a integer')
        if year < 0:
            raise const.PyID3TaggerInvalidData('Year has to be bigger or equal 0')
        if year > 9999:
            raise const.PyID3TaggerInvalidData('Year has to be lesser or equal 9999')
        self.__year = year

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment):
        if not isinstance(comment, str):
            raise const.PyID3TaggerInvalidData('Comment has to be a string')
        self.__comment = comment

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        if not isinstance(genre, int):
            raise const.PyID3TaggerInvalidData('Genre has to be a integer')
        if genre not in range(256):
            raise const.PyID3TaggerInvalidData('Genre has to be 0 <= genre <= 255')
        self.__genre = genre

    def read(self, file_path):
        raise const.PyID3TaggerNotImplementedError('This should be implemented by the derived class')

    def write(self, file_path):
        raise const.PyID3TaggerNotImplementedError('This should be implemented by the derived class')


class ID3v1Tag(ID3v1BaseClass):

    def read(self, file_path):

        self.file_path = file_path

        try:
            mp3_file = open(self.file_path, 'rb')
        except IOError as io_error:
            raise const.PyID3TaggerIOError(io_error.message)

        mp3_file.seek(-128, 2)
        if mp3_file.read(3) != 'TAG':
            raise const.PyID3TaggerInvalidData('File does not contain a ID3v1 Tag')
        self.title = mp3_file.read(30).split('\x00')[0]
        self.artist = mp3_file.read(30).split('\x00')[0]
        self.album = mp3_file.read(30).split('\x00')[0]
        raw_year = mp3_file.read(4)
        if not raw_year.isdigit():
            raise const.PyID3TaggerInvalidData('Invalid year')
        self.year = int(raw_year)
        self.comment = mp3_file.read(30).split('\x00')[0]
        self.genre = ord(mp3_file.read(1))

    def generate(self):
        tag = 'TAG'
        title_tag = self.base_tag % self.title
        tag += title_tag[:30]
        artist_tag = self.base_tag % self.artist
        tag += artist_tag[:30]
        album_tag = self.base_tag % self.album
        tag += album_tag[:30]
        year_tag = '%04i' % self.year
        tag += year_tag[:4]
        comment_tag = self.base_tag % self.comment
        tag += comment_tag[:30]
        genre_tag = chr(max(min(self.genre, 255), 0))
        tag += genre_tag[0]
        return tag

    def write(self, file_path=None):
        if not self.file_path and not file_path:
            raise const.PyID3TaggerFilePathException('No file path specified')
        if file_path:
            self.file_path = file_path
        utilities.remove_ID3_1_tag(self.file_path)

        try:
            mp3_file = open(file_path, 'ab')
        except IOError as ioerror:
            raise const.PyID3TaggerIOError(ioerror.message)

        mp3_file.write(self.generate())

    # todo convert to other types


class ID3v1_1Tag(ID3v1BaseClass):

    def __init__(self):
        super(ID3v1_1Tag, self).__init__()
        self.__track = 0

    @property
    def track(self):
        return self.__track

    @track.setter
    def track(self, track):
        if not isinstance(track, int):
            raise const.PyID3TaggerInvalidData('Track has to be a integer')
        if track not in range(256):
            raise const.PyID3TaggerInvalidData('Track has to be 0 <= track <= 255')
        self.__track = track

    def read(self, file_path):

        try:
            mp3_file = open(file_path, 'rb')
        except IOError as ioerror:
            raise const.PyID3TaggerIOError(ioerror.message)

        self.file_path = file_path

        mp3_file.seek(-128, 2)
        if mp3_file.read(3) != 'TAG':
            raise const.PyID3TaggerInvalidData('File does not contain a ID3v1 Tag')
        self.title = mp3_file.read(30).split('\x00')[0]
        self.artist = mp3_file.read(30).split('\x00')[0]
        self.album = mp3_file.read(30).split('\x00')[0]
        raw_year = mp3_file.read(4)
        if not raw_year.isdigit():
            raise const.PyID3TaggerInvalidData('Invalid year')
        self.year = int(raw_year)
        self.comment = mp3_file.read(28).split('\x00')[0]
        empty_byte = mp3_file.read(1)
        if empty_byte != '\x00':
            raise const.PyID3TaggerInvalidData('Byte before track not according to ID3v1.1 specification')
        self.track = ord(mp3_file.read(1))
        self.genre = ord(mp3_file.read(1))

    def generate(self):
        tag = 'TAG'
        title_tag = self.base_tag % self.title
        tag += title_tag[:30]
        artist_tag = self.base_tag % self.artist
        tag += artist_tag[:30]
        album_tag = self.base_tag % self.album
        tag += album_tag[:30]
        year_tag = '%04i' % self.year
        tag += year_tag[:4]
        comment_tag = self.base_tag % self.comment
        tag += comment_tag[:28]
        tag += '\x00'
        track_tag = chr(max(min(self.track, 255), 0))
        tag += track_tag[0]
        genre_tag = chr(max(min(self.genre, 255), 0))
        tag += genre_tag[0]
        return tag

    def write(self, file_path=None):
        if not self.file_path and not file_path:
            raise const.PyID3TaggerFilePathException('No file path specified')
        if file_path:
            self.file_path = file_path
        utilities.remove_ID3_1_tag(file_path)

        try:
            mp3_file = open(file_path, 'ab')
        except IOError as ioerror:
            raise const.PyID3TaggerIOError(ioerror.message)

        mp3_file.write(self.generate())

    # todo convert to other types


class ID3v2_3Tag(object):

    file_identifier = "ID3"
    version = '\x03\x00'

    def __init__(self):
        self.frames = list()
        self.padding_size = 1256

    @property
    def unsynchronisation(self):
        return False  # todo

    def extended_header(self):
        return False  # todo

    def experimental_indicator(self):
        return False  # todo

    def generate(self):
        tag = self.__class__.file_identifier + self.__class__.version
        tag += chr(self.unsynchronisation * 2 ** 7 +
                   self.extended_header() * 2 ** 6 +
                   self.experimental_indicator() * 2 ** 5)
        frames = ''
        for frame in self.frames:
            frames += frame.generate()
        if self.unsynchronisation:
            pass
            # todo unsynchronize frames
        # todo extended header
        if len(frames) == 0:
            return ''
        if len(frames) < self.padding_size:
            frames += '\x00' * (self.padding_size - len(frames))
        tag += utilities.int_to_four_sync_save_bytes(len(frames))
        tag += frames
        return tag
