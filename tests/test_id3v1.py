# coding=utf-8

import os
import shutil
import unittest

import pyid3tagger


class ID3v1Test(unittest.TestCase):

    def test_write_id3v1_tag(self):
        source_path = 'TestData\\no_tag.mp3'
        target_path = 'test.mp3'
        compare_file_path = 'TestData\\id3v1\\id3v1_001_basic.mp3'

        if os.path.exists(target_path):
            os.remove(target_path)
        shutil.copyfile(source_path, target_path)

        tag = pyid3tagger.ID3v1Tag()
        tag.title = 'Title'
        tag.artist = 'Artist'
        tag.album = 'Album'
        tag.year = 2003
        tag.comment = 'Comment'
        tag.genre = pyid3tagger.ID3v1_GENERES.HIP_HOP

        tag.write(target_path)

        test_file_content = open(compare_file_path).read()
        should_have_no_tag_file_content = open(target_path).read()

        self.assertEqual(test_file_content, should_have_no_tag_file_content)

        os.remove(target_path)

    def test_overwrite_id3v1_tag(self):
        source_path = 'TestData\\id3v1\\id3v1_274_extra.mp3'
        target_path = 'test.mp3'
        compare_file_path = 'TestData\\id3v1\\id3v1_001_basic.mp3'

        if os.path.exists(target_path):
            os.remove(target_path)
        shutil.copyfile(source_path, target_path)

        tag = pyid3tagger.ID3v1Tag()
        tag.title = 'Title'
        tag.artist = 'Artist'
        tag.album = 'Album'
        tag.year = 2003
        tag.comment = 'Comment'
        tag.genre = pyid3tagger.ID3v1_GENERES.HIP_HOP

        tag.write(target_path)

        test_file_content = open(compare_file_path).read()
        should_have_no_tag_file_content = open(target_path).read()

        self.assertEqual(test_file_content, should_have_no_tag_file_content)

        os.remove(target_path)

    # todo test exceptions
    #   test cases for year
    # todo read tests

    def test_read_id3v1_test_case_1(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_001_basic.mp3')
        self.assertEqual('Title', tag.title)
        self.assertEqual('Artist', tag.artist)
        self.assertEqual('Album', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('Comment', tag.comment)
        self.assertEqual(7, tag.genre)

    def test_read_id3v1_1_test_case_2(self):
        tag = pyid3tagger.ID3v1_1Tag()
        tag.read('TestData\\id3v1\\id3v1_002_basic.mp3')
        self.assertEqual('Title', tag.title)
        self.assertEqual('Artist', tag.artist)
        self.assertEqual('Album', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('Comment', tag.comment)
        self.assertEqual(12, tag.track)
        self.assertEqual(7, tag.genre)

    def test_read_id3v1_1_test_case_3(self):
        tag = pyid3tagger.ID3v1Tag()
        try:
            tag.read('TestData\\id3v1\\id3v1_003_basic_F.mp3')
        except pyid3tagger.PyID3TaggerInvalidData as e:
            self.assertEqual('File does not contain a ID3v1 Tag', e.message)
        else:
            self.fail('No exception where PyID3TaggerInvalidData should be raised')

    def test_read_id3v1_1_test_case_4(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_004_basic.mp3')
        self.assertEqual('', tag.title)
        self.assertEqual('', tag.artist)
        self.assertEqual('', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('', tag.comment)
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_1_test_case_5(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_005_basic.mp3')
        self.assertEqual('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaA', tag.title)
        self.assertEqual('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbB', tag.artist)
        self.assertEqual('cccccccccccccccccccccccccccccC', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('dddddddddddddddddddddddddddddD', tag.comment)
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_1_test_case_6(self):
        tag = pyid3tagger.ID3v1_1Tag()
        tag.read('TestData\\id3v1\\id3v1_006_basic.mp3')
        self.assertEqual('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaA', tag.title)
        self.assertEqual('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbB', tag.artist)
        self.assertEqual('cccccccccccccccccccccccccccccC', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('dddddddddddddddddddddddddddD', tag.comment)
        self.assertEqual(1, tag.track)
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_test_case_7(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_007_basic_W.mp3')
        self.assertEqual('12345', tag.title)
        self.assertEqual('12345', tag.artist)
        self.assertEqual('12345', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('12345', tag.comment)
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_1_test_case_8(self):
        tag = pyid3tagger.ID3v1_1Tag()
        tag.read('TestData\\id3v1\\id3v1_008_basic_W.mp3')
        self.assertEqual('12345', tag.title)
        self.assertEqual('12345', tag.artist)
        self.assertEqual('12345', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('12345', tag.comment)
        self.assertEqual(1, tag.track)
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_1_test_case_9(self):
        tag = pyid3tagger.ID3v1_1Tag()
        tag.read('TestData\\id3v1\\id3v1_009_basic.mp3')
        self.assertEqual('', tag.title)
        self.assertEqual('', tag.artist)
        self.assertEqual('', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('', tag.comment)
        self.assertEqual(255, tag.track)
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_1_test_case_10(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_010_year.mp3')
        self.assertEqual('', tag.title)
        self.assertEqual('', tag.artist)
        self.assertEqual('', tag.album)
        self.assertEqual(0, tag.year)
        self.assertEqual('', tag.comment)
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_1_test_case_11(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_011_year.mp3')
        self.assertEqual('', tag.title)
        self.assertEqual('', tag.artist)
        self.assertEqual('', tag.album)
        self.assertEqual(9999, tag.year)
        self.assertEqual('', tag.comment)
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_1_test_case_12(self):
        tag = pyid3tagger.ID3v1Tag()
        try:
            tag.read('TestData\\id3v1\\id3v1_012_year_F.mp3')
        except pyid3tagger.PyID3TaggerInvalidData as e:
            self.assertEqual(e.message, 'Invalid year')
        else:
            self.fail('This should raise an PyID3TaggerInvalidData exeption')

    def test_read_id3v1_1_test_case_13(self):
        tag = pyid3tagger.ID3v1Tag()
        try:
            tag.read('TestData\\id3v1\\id3v1_013_year_F.mp3')
        except pyid3tagger.PyID3TaggerInvalidData as e:
            self.assertEqual(e.message, 'Invalid year')
        else:
            self.fail('This should raise an PyID3TaggerInvalidData exeption')

    def test_read_id3v1_1_test_case_14(self):
        tag = pyid3tagger.ID3v1Tag()
        try:
            tag.read('TestData\\id3v1\\id3v1_014_year_F.mp3')
        except pyid3tagger.PyID3TaggerInvalidData as e:
            self.assertEqual(e.message, 'Invalid year')
        else:
            self.fail('This should raise an PyID3TaggerInvalidData exeption')

    def test_read_id3v1_test_case_genres(self):
        for i in range(80):
            tag = pyid3tagger.ID3v1Tag()
            tag.read('TestData\\id3v1\\id3v1_%03i_genre.mp3' % (i + 15,))
            self.assertEqual(i, tag.genre)
            self.assertEqual(pyid3tagger.ID3v1_GENERES.GENRE_2_NAME[i], tag.title)

    def test_read_id3v1_test_case_genres_w(self):
        for i in range(80, 148):
            tag = pyid3tagger.ID3v1Tag()
            tag.read('TestData\\id3v1\\id3v1_%03i_genre_W.mp3' % (i + 15,))
            self.assertEqual(i, tag.genre)
            self.assertEqual(pyid3tagger.ID3v1_GENERES.GENRE_2_NAME[i], tag.title)

    def test_read_id3v1_test_case_genres_f(self):
        for i in range(148, 256):
            tag = pyid3tagger.ID3v1Tag()
            tag.read('TestData\\id3v1\\id3v1_%03i_genre_f.mp3' % (i + 15,))
            self.assertEqual(i, tag.genre)
            self.assertEqual('Unknown/%i' % i, tag.title)

    def test_read_id3v1_test_case_271(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_271_extra.mp3')
        self.assertEqual(u'räksmörgås', tag.title.decode('latin-1'))
        self.assertEqual(u'räksmörgås', tag.artist.decode('latin-1'))
        self.assertEqual(u'räksmörgås', tag.album.decode('latin-1'))
        self.assertEqual(2003, tag.year)
        self.assertEqual(u'räksmörgås', tag.comment.decode('latin-1'))
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_test_case_272(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_272_extra.mp3')
        self.assertEqual(u'räksmörgås', tag.title.decode('utf-8'))
        self.assertEqual(u'räksmörgås', tag.artist.decode('utf-8'))
        self.assertEqual(u'räksmörgås', tag.album.decode('utf-8'))
        self.assertEqual(2003, tag.year)
        self.assertEqual(u'räksmörgås', tag.comment.decode('utf-8'))
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_test_case_273(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_273_extra.mp3')
        self.assertEqual('', tag.title)
        self.assertEqual('', tag.artist)
        self.assertEqual('', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('http://www.id3.org/', tag.comment)
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_test_case_274(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_274_extra.mp3')
        self.assertEqual('', tag.title)
        self.assertEqual('', tag.artist)
        self.assertEqual('', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('www.id3.org/', tag.comment)
        self.assertEqual(0, tag.genre)

    def test_read_id3v1_as_id3v1_1(self):
        tag = pyid3tagger.ID3v1_1Tag()
        tag.read('TestData\\id3v1\\id3v1_039_genre.mp3')
        self.assertEqual('Soundtrack', tag.title)
        self.assertEqual('', tag.artist)
        self.assertEqual('', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('', tag.comment)
        self.assertEqual(0, tag.track)
        self.assertEqual(24, tag.genre)


if __name__ == '__main__':
    unittest.main()
