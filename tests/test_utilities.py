# coding=utf-8

import os
import shutil
import unittest

import pyid3tagger


class UtilitiesTest(unittest.TestCase):

    def test_guess_tags_versions_id3v1(self):
        versions = pyid3tagger.guess_tags_versions('TestData\\id3v1\\id3v1_001_basic.mp3')
        self.assertEqual(2, len(versions))
        self.assertTrue(pyid3tagger.ID3v1_VERSION in versions)
        self.assertTrue(pyid3tagger.ID3v1_1_VERSION in versions)

    def test_guess_tags_versions_no_tag(self):
        versions = pyid3tagger.guess_tags_versions('TestData\\no_tag.mp3')
        self.assertEqual(0, len(versions))

    def test_remove_id3v1_tag(self):
        source_path = 'TestData\\id3v1\\id3v1_274_extra.mp3'
        target_path = 'should_have_no_tag.mp3'
        compare_file_path = 'TestData\\no_tag.mp3'

        if os.path.exists(target_path):
            os.remove(target_path)
        shutil.copyfile(source_path, target_path)

        versions = pyid3tagger.guess_tags_versions(target_path)
        self.assertEqual(2, len(versions))
        self.assertTrue(pyid3tagger.ID3v1_VERSION in versions)
        self.assertTrue(pyid3tagger.ID3v1_1_VERSION in versions)

        # remove tag
        pyid3tagger.remove_ID3_1_tag(target_path)

        versions = pyid3tagger.guess_tags_versions(target_path)
        self.assertEqual(0, len(versions))

        no_tag_file_content = open(compare_file_path).read()
        should_have_no_tag_file_content = open(target_path).read()

        self.assertEqual(no_tag_file_content, should_have_no_tag_file_content)

        os.remove(target_path)

    def test_remove_id3v1_tag_no_tag(self):
        source_path = 'TestData\\no_tag.mp3'
        target_path = 'should_have_no_tag.mp3'

        if os.path.exists(target_path):
            os.remove(target_path)
        shutil.copyfile(source_path, target_path)

        # remove not existing tag
        pyid3tagger.remove_ID3_1_tag(target_path)

        versions = pyid3tagger.guess_tags_versions(target_path)
        self.assertEqual(0, len(versions))

        no_tag_file_content = open(source_path).read()
        should_have_no_tag_file_content = open(target_path).read()

        self.assertEqual(no_tag_file_content, should_have_no_tag_file_content)

        os.remove(target_path)

if __name__ == '__main__':
    unittest.main()
