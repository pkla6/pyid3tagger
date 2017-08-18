# coding=utf-8

import os
import shutil
import unittest

import pyid3tagger


class ID3v1Test(unittest.TestCase):

    def test_read_id3v1_test_case_1(self):
        tag = pyid3tagger.ID3v1Tag()
        tag.read('TestData\\id3v1\\id3v1_001_basic.mp3')
        self.assertEqual('Title', tag.title)
        self.assertEqual('Artist', tag.artist)
        self.assertEqual('Album', tag.album)
        self.assertEqual(2003, tag.year)
        self.assertEqual('Comment', tag.comment)
        self.assertEqual(7, tag.genre)

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
        tag.genre = pyid3tagger.ID3v1_GENRE_HIP_HOP

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
        tag.genre = pyid3tagger.ID3v1_GENRE_HIP_HOP

        tag.write(target_path)

        test_file_content = open(compare_file_path).read()
        should_have_no_tag_file_content = open(target_path).read()

        self.assertEqual(test_file_content, should_have_no_tag_file_content)

        os.remove(target_path)

    # todo test exceptions

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

    def test_read_id3v1_1_test_case_39(self):
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
