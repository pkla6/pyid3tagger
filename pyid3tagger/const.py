# coding=utf-8

__author__ = "Peter Klassen peter@mediadock.org"
__license__ = "MIT License"
__copyright__ = "(c) 2017 Peter Klassen peter@mediadock.org"

# versions
ID3v1_VERSION = 'ID3v1'
ID3v1_1_VERSION = 'ID3v1.1'
ID3v2_2_VERSION = 'ID3v2.2'
ID3v2_3_VERSION = 'ID3v2.3'
ID3v2_4_VERSION = 'ID3v2.4'

# ID3v1 genres
ID3v1_GENRE_HIP_HOP = 7


# exceptions
class PyID3TaggerException(Exception):
    pass


class PyID3TaggerNotImplementedError(PyID3TaggerException):
    pass


class PyID3TaggerInvalidData(PyID3TaggerException):
    pass


class PyID3TaggerIOError(PyID3TaggerException):
    pass
