# coding=utf-8

import re

import utilities
import const


class ID3v2_3BaseFrame(object):

    def __init__(self):
        self.__tag_alter_preservation = True
        self.__file_alter_preservation = True
        self.__read_only = False
        self.__compression = False
        self.__encryption = False
        self.__grouping_identity = False

    @property
    def tag_alter_preservation(self):
        return self.__tag_alter_preservation

    @tag_alter_preservation.setter
    def tag_alter_preservation(self, value):
        self.__tag_alter_preservation = bool(value)

    @property
    def file_alter_preservation(self):
        return self.__file_alter_preservation

    @file_alter_preservation.setter
    def file_alter_preservation(self, value):
        self.__file_alter_preservation = bool(value)

    @property
    def read_only(self):  # todo
        return self.__read_only

    @property
    def compression(self):  # todo
        return self.__compression

    @property
    def encryption(self):  # todo
        return self.__encryption

    @property
    def grouping_identity(self):  # todo
        return self.__grouping_identity

    def generate(self):
        header = self.frame_id
        payload = self.generate_payload()
        if len(payload) == 0:
            return ''
        header += utilities.int_to_four_bytes (len(payload))
        header += chr(self.tag_alter_preservation * 2 ** 7 +
                      self.file_alter_preservation * 2 ** 6 +
                      self.read_only * 2 ** 5)
        header += chr(self.compression * 2 ** 7 +
                      self.encryption * 2 ** 6 +
                      self.grouping_identity * 2 ** 5)

        return header + payload


class ID3v2_3TextInformationBaseFrame(ID3v2_3BaseFrame):

    def __init__(self, text, encoding=const.ID3v2_3ENCODING.ISO_8859_1):
        super(ID3v2_3TextInformationBaseFrame, self).__init__()
        self.__encoding = const.ID3v2_3ENCODING.ISO_8859_1
        self.__text = ''
        self.encoding = encoding
        self.text = text

    @property
    def text(self):
        return self.__text.decode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @text.setter
    def text(self, value):  # todo new line, range if iso 8859
        if not isinstance(value, unicode):
            raise  # todo
        self.__text = value.encode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, value):
        if not value in (const.ID3v2_3ENCODING.ISO_8859_1, const.ID3v2_3ENCODING.UNICODE):
            raise  # todo
        self.__text = self.text.decode(const.ID3v2_3_ENCODING_DICT[value])  # todo test
        self.__encoding = value

    def generate_payload(self):
        return self.encoding + self.__text


class ID3v2_3UrlBaseFrame(ID3v2_3BaseFrame):

    def __init__(self, url):
        super(ID3v2_3UrlBaseFrame, self).__init__()
        self.__url = ''
        self.url = url

    @property
    def url(self):
        return self.__url.decode(const.ID3v2_3_ENCODING_DICT[const.ID3v2_3ENCODING.ISO_8859_1])

    @url.setter
    def url(self, value):
        if not isinstance(value, unicode):
            raise  # todo
        url = value.encode(const.ID3v2_3_ENCODING_DICT[const.ID3v2_3ENCODING.ISO_8859_1])
        # if not utilities.check_is_ISO_639_2_code(url):  todo
        #    raise  # todo
        self.__url = url

    def generate_payload(self):
        return self.__url


class ID3v2_3LanguageMixIn(object):

    def __init__(self):
        self.__language = 'und'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if not utilities.check_is_ISO_639_2_code(value):
            raise  # todo
        self.__language = value


class ID3v2_3MimeTypeMixIn(object):

    def __init__(self):
        self.__mime_type = 'application/octet-stream'

    @property
    def mime_type(self):
        return self.__mime_type

    @mime_type.setter
    def mime_type(self, value):
        if not value in const.MIME_TYPES_LIST:
            raise  # todo
        self.__mime_type = value


class ID3v2_3_APIC_Frame(ID3v2_3BaseFrame, ID3v2_3MimeTypeMixIn):

    def __init__(self, mime_type, picture_type, description, picture, encoding=const.ID3v2_3ENCODING.UNICODE):
        ID3v2_3BaseFrame.__init__(self)
        ID3v2_3MimeTypeMixIn.__init__(self)
        self.__encoding = const.ID3v2_3ENCODING.ISO_8859_1
        self.__content_description = ''
        self.__picture_type = '\x00'
        self.encoding = encoding
        self.mime_type = mime_type
        self.picture_type = picture_type
        self.content_description = description
        self.picture = picture

    @property
    def frame_id(self):
        return 'APIC'

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, value):
        if not value in (const.ID3v2_3ENCODING.ISO_8859_1, const.ID3v2_3ENCODING.UNICODE):
            raise  # todo
        # todo new line, range if iso 8859
        new_content_description = self.content_description.decode(const.ID3v2_3_ENCODING_DICT[value])  # todo test
        self.__content_description = new_content_description
        self.__encoding = value

    @property
    def picture_type(self):
        return self.__picture_type

    @picture_type.setter
    def picture_type(self, value):
        if not value in const.ID3v2_3_PICTURE_TYPES_LIST:
            raise  # todo
        self.__picture_type = value

    @property
    def content_description(self):
        return self.__content_description.decode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @content_description.setter
    def content_description(self, value):  # todo range if iso 8859
        if not isinstance(value, unicode):
            raise  # todo
        self.__content_description = value.encode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    def generate_payload(self):
        payload = self.encoding
        payload += self.mime_type
        payload += '\x00'
        payload += self.picture_type
        payload += self.__content_description
        payload += '\x00'
        if self.encoding == const.ID3v2_3ENCODING.UNICODE:
            payload += '\x00'
        payload += self.picture
        return payload


class ID3v2_3_COMM_Frame(ID3v2_3BaseFrame, ID3v2_3LanguageMixIn):

    def __init__(self, description, text, language, encoding=const.ID3v2_3ENCODING.UNICODE):
        ID3v2_3BaseFrame.__init__(self)
        ID3v2_3LanguageMixIn.__init__(self)
        self.__encoding = const.ID3v2_3ENCODING.ISO_8859_1
        self.__content_description = ''
        self.__text = ''
        self.encoding = encoding
        self.language = language
        self.content_description = description
        self.text = text


    @property
    def frame_id(self):
        return 'COMM'

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, value):
        if not value in (const.ID3v2_3ENCODING.ISO_8859_1, const.ID3v2_3ENCODING.UNICODE):
            raise  # todo
        # todo new line, range if iso 8859
        new_text = self.text.decode(const.ID3v2_3_ENCODING_DICT[value])  # todo test
        new_content_description = self.content_description.decode(const.ID3v2_3_ENCODING_DICT[value])  # todo test
        self.__text = new_text
        self.__content_description = new_content_description
        self.__encoding = value

    @property
    def text(self):
        return self.__text.decode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @text.setter
    def text(self, value):  # todo new line, range if iso 8859
        if not isinstance(value, unicode):
            raise  # todo
        self.__text = value.encode(const.ID3v2_3_ENCODING_DICT[self.encoding])\

    @property
    def content_description(self):
        return self.__content_description.decode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @content_description.setter
    def content_description(self, value):  # todo range if iso 8859
        if not isinstance(value, unicode):
            raise  # todo
        self.__content_description = value.encode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    def generate_payload(self):
        payload = self.encoding
        payload += self.language
        payload += self.__content_description
        payload += '\x00'
        if self.encoding == const.ID3v2_3ENCODING.UNICODE:
            payload += '\x00'
        payload += self.__text
        return payload


class ID3v2_3_GEOB_Frame(ID3v2_3BaseFrame, ID3v2_3MimeTypeMixIn):

    def __init__(self, mime_type, filename, content_description, object, encoding=const.ID3v2_3ENCODING.ISO_8859_1):
        ID3v2_3BaseFrame.__init__(self)
        ID3v2_3MimeTypeMixIn.__init__(self)
        self.__content_description = ''
        self.__filename = ''
        self.__object = ''
        self.__encoding = const.ID3v2_3ENCODING.ISO_8859_1
        self.encoding = encoding  # todo property
        self.mime_type = mime_type
        self.content_description = content_description  # todo property
        self.filename = filename  # todo property
        self.object = object

    @property
    def frame_id(self):
        return 'GEOB'

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, value):
        if not value in (const.ID3v2_3ENCODING.ISO_8859_1, const.ID3v2_3ENCODING.UNICODE):
            raise  # todo
        # todo new line, range if iso 8859
        new_filename = self.filename.decode(const.ID3v2_3_ENCODING_DICT[value])  # todo test
        new_content_description = self.content_description.decode(const.ID3v2_3_ENCODING_DICT[value])  # todo test
        self.__filename = new_filename
        self.__content_description = new_content_description
        self.__encoding = value

    @property
    def filename(self):
        return self.__filename.decode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @filename.setter
    def filename(self, value):  # todo range if iso 8859
        if not isinstance(value, unicode):
            raise  # todo
        self.__filename = value.encode(const.ID3v2_3_ENCODING_DICT[self.encoding])\

    @property
    def content_description(self):
        return self.__content_description.decode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @content_description.setter
    def content_description(self, value):  # todo range if iso 8859
        if not isinstance(value, unicode):
            raise  # todo
        self.__content_description = value.encode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @property
    def object(self):
        return self.__object

    @object.setter
    def object(self, value):
        if not isinstance(value, str):
            raise  # todo
        self.__object = value

    def generate_payload(self):
        payload = self.encoding
        payload += self.mime_type
        payload += '\x00'
        payload += self.__filename
        payload += '\x00'
        if self.encoding == const.ID3v2_3ENCODING.UNICODE:
            payload += '\x00'
        payload += self.__content_description
        payload += '\x00'
        if self.encoding == const.ID3v2_3ENCODING.UNICODE:
            payload += '\x00'
        payload += self.object
        return payload


class ID3v2_3_TALB_Frame(ID3v2_3TextInformationBaseFrame):
    """
      TALB
       The 'Album/Movie/Show title' frame is intended for the title of the
       recording(/source of sound) which the audio in the file is taken
       from.
    """
    @property
    def frame_id(self):
        return 'TALB'


class ID3v2_3_TCON_Frame(ID3v2_3TextInformationBaseFrame):  # todo not according to specification
    """
      TCON
       The 'Content type', which previously was stored as a one byte numeric
       value only, is now a numeric string. You may use one or several of
       the types as ID3v1.1 did or, since the category list would be
       impossible to maintain with accurate and up to date categories,
       define your own.

       References to the ID3v1 genres can be made by, as first byte, enter
       "(" followed by a number from the genres list (appendix A.) and
       ended with a ")" character. This is optionally followed by a
       refinement, e.g. "(21)" or "(4)Eurodisco". Several references can be
       made in the same frame, e.g. "(51)(39)". If the refinement should
       begin with a "(" character it should be replaced with "((", e.g. "((I
       can figure out any genre)" or "(55)((I think...)". The following new
       content types is defined in ID3v2 and is implemented in the same way
       as the numerig content types, e.g. "(RX)".

         RX  Remix
         CR  Cover
    """
    @property
    def frame_id(self):
        return 'TCON'


class ID3v2_3_TDAT_Frame(ID3v2_3BaseFrame):
    """
      TDAT
       The 'Date' frame is a numeric string in the DDMM format containing
       the date for the recording. This field is always four characters
       long.
    """

    def __init__(self, day, month):
        ID3v2_3BaseFrame.__init__(self)
        self.__encoding = const.ID3v2_3ENCODING.ISO_8859_1
        self.__day = 1
        self.__month = 1
        self.day = day
        self.month = month

    @property
    def frame_id(self):
        return 'TDAT'

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if not isinstance(value, int):
            raise  # todo
        if not 0 < value < 32:
            raise  # todo
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if not isinstance(value, int):
            raise  # todo
        if not 0 < value < 13:
            raise  # todo
        self.__month = value

    def generate_payload(self):
        return self.__encoding + '%02i%02i' % (self.day, self.month)


class ID3v2_3_TIT1_Frame(ID3v2_3TextInformationBaseFrame):
    """
      TIT1
       The 'Content group description' frame is used if the sound belongs to
       a larger category of sounds/music. For example, classical music is
       often sorted in different musical sections (e.g. "Piano Concerto",
       "Weather - Hurricane").
    """
    @property
    def frame_id(self):
        return 'TIT1'


class ID3v2_3_TIT2_Frame(ID3v2_3TextInformationBaseFrame):
    """
      TIT2
       The 'Title/Songname/Content description' frame is the actual name of
       the piece (e.g. "Adagio", "Hurricane Donna").
    """
    @property
    def frame_id(self):
        return 'TIT2'


class ID3v2_3_TIT3_Frame(ID3v2_3TextInformationBaseFrame):
    """
      TIT3
       The 'Subtitle/Description refinement' frame is used for information
       directly related to the contents title (e.g. "Op. 16" or "Performed
       live at Wembley").
    """
    @property
    def frame_id(self):
        return 'TIT3'


class ID3v2_3_TPE1_Frame(ID3v2_3TextInformationBaseFrame):
    """
      TPE1
       The 'Lead artist(s)/Lead performer(s)/Soloist(s)/Performing group' is
       used for the main artist(s). They are seperated with the "/"
       character.
    """
    @property  # todo text separation with /
    def frame_id(self):
        return 'TPE1'


class ID3v2_3_TPE2_Frame(ID3v2_3TextInformationBaseFrame):
    """
      TPE2
       The 'Band/Orchestra/Accompaniment' frame is used for additional
       information about the performers in the recording.
    """
    @property
    def frame_id(self):
        return 'TPE2'


class ID3v2_3_TPOS_Frame(ID3v2_3BaseFrame):
    """
      TPOS
       The 'Part of a set' frame is a numeric string that describes which
       part of a set the audio came from. This frame is used if the source
       described in the "TALB" frame is divided into several mediums, e.g. a
       double CD. The value may be extended with a "/" character and a
       numeric string containing the total number of parts in the set. E.g.
       "1/2".
    """
    def __init__(self, text, encoding=const.ID3v2_3ENCODING.ISO_8859_1):
        ID3v2_3BaseFrame.__init__(self)
        self.__encoding = const.ID3v2_3ENCODING.ISO_8859_1
        self.__text = ''
        self.encoding = encoding
        self.text = text

    @property
    def frame_id(self):
        return 'TPOS'

    @property
    def text(self):
        return self.__text.decode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @text.setter
    def text(self, value):  # todo new line, range if iso 8859
        if not isinstance(value, (unicode, str)):
            raise  # todo
        if not re.match(r'\A\d+/\d+\Z', value):
            raise  # todo
        self.__text = value.encode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, value):
        if not value in (const.ID3v2_3ENCODING.ISO_8859_1, const.ID3v2_3ENCODING.UNICODE):
            raise  # todo
        self.__text = self.text.decode(const.ID3v2_3_ENCODING_DICT[value])  # todo test
        self.__encoding = value

    def generate_payload(self):
        return self.encoding + self.__text


class ID3v2_3_TRCK_Frame(ID3v2_3BaseFrame):
    """
      TRCK
       The 'Track number/Position in set' frame is a numeric string
       containing the order number of the audio-file on its original
       recording. This may be extended with a "/" character and a numeric
       string containing the total numer of tracks/elements on the original
       recording. E.g. "4/9".
    """
    def __init__(self, text, encoding=const.ID3v2_3ENCODING.ISO_8859_1):
        ID3v2_3BaseFrame.__init__(self)
        self.__encoding = const.ID3v2_3ENCODING.ISO_8859_1
        self.__text = ''
        self.encoding = encoding
        self.text = text

    @property
    def frame_id(self):
        return 'TRCK'

    @property
    def text(self):
        return self.__text.decode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @text.setter
    def text(self, value):  # todo new line, range if iso 8859
        if not isinstance(value, (unicode, str)):
            raise  # todo
        if not re.match(r'\A\d+(/\d+)?\Z', value):
            raise  # todo
        self.__text = value.encode(const.ID3v2_3_ENCODING_DICT[self.encoding])

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, value):
        if not value in (const.ID3v2_3ENCODING.ISO_8859_1, const.ID3v2_3ENCODING.UNICODE):
            raise  # todo
        self.__text = self.text.decode(const.ID3v2_3_ENCODING_DICT[value])  # todo test
        self.__encoding = value

    def generate_payload(self):
        return self.encoding + self.__text


class ID3v2_3_TYER_Frame(ID3v2_3BaseFrame):
    """
      TYER
       The 'Year' frame is a numeric string with a year of the recording.
       This frames is always four characters long (until the year 10000).
    """
    def __init__(self, year):
        ID3v2_3BaseFrame.__init__(self)
        self.__encoding = const.ID3v2_3ENCODING.ISO_8859_1
        self.__year = 2000
        self.year = year

    @property
    def frame_id(self):
        return 'TYER'

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise  # todo
        if not 999 < value < 10000:
            raise  # todo
        self.__year = value

    def generate_payload(self):
        return self.__encoding + str(self.__year)


class ID3v2_3_WCOM_Frame(ID3v2_3UrlBaseFrame):
    """
      WCOM
       The 'Commercial information' frame is a URL pointing at a webpage
       with information such as where the album can be bought. There may be
       more than one "WCOM" frame in a tag, but not with the same content.
    """

    @property
    def frame_id(self):
        return 'WCOM'


class ID3v2_3_WCOP_Frame(ID3v2_3UrlBaseFrame):
    """
      WCOP
       The 'Copyright/Legal information' frame is a URL pointing at a
       webpage where the terms of use and ownership of the file is
       described.
    """

    @property
    def frame_id(self):
        return 'WCOP'


class ID3v2_3_WOAF_Frame(ID3v2_3UrlBaseFrame):
    """
      WOAF
       The 'Official audio file webpage' frame is a URL pointing at a file
       specific webpage.
    """

    @property
    def frame_id(self):
        return 'WOAF'


class ID3v2_3_WOAR_Frame(ID3v2_3UrlBaseFrame):
    """
      WOAR
       The 'Official artist/performer webpage' frame is a URL pointing at
       the artists official webpage. There may be more than one "WOAR" frame
       in a tag if the audio contains more than one performer, but not with
       the same content.
    """

    @property
    def frame_id(self):
        return 'WOAR'


class ID3v2_3_WOAS_Frame(ID3v2_3UrlBaseFrame):
    """
      WOAS
       The 'Official audio source webpage' frame is a URL pointing at the
       official webpage for the source of the audio file, e.g. a movie.
    """

    @property
    def frame_id(self):
        return 'WOAS'


class ID3v2_3_WORS_Frame(ID3v2_3UrlBaseFrame):
    """
      WORS
       The 'Official internet radio station homepage' contains a URL
       pointing at the homepage of the internet radio station.
    """

    @property
    def frame_id(self):
        return 'WORS'


class ID3v2_3_WPAY_Frame(ID3v2_3UrlBaseFrame):
    """
      WPAY
       The 'Payment' frame is a URL pointing at a webpage that will handle
       the process of paying for this file.
    """

    @property
    def frame_id(self):
        return 'WPAY'


class ID3v2_3_WPUB_Frame(ID3v2_3UrlBaseFrame):
    """
      WPUB
       The 'Publishers official webpage' frame is a URL pointing at the
       official wepage for the publisher.
    """

    @property
    def frame_id(self):
        return 'WPUB'

