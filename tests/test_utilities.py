# coding=utf-8

import unittest

import pyid3tagger


class UtilitiesTest(unittest.TestCase):

    def test_guess_tags_versions_id2v1(self):
        versions = pyid3tagger.guess_tags_versions('TestData\\id3v1\\id3v1_001_basic.mp3')
        self.assertTrue(2, len(versions))
        self.assertTrue(pyid3tagger.ID3v1_VERSION in versions)
        self.assertTrue(pyid3tagger.ID3v1_1_VERSION in versions)

if __name__ == '__main__':
    unittest.main()
