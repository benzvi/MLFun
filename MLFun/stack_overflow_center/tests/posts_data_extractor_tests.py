import json

from django.test import TestCase
from django.conf import settings

from stack_overflow_center.data_extractor.posts_data_extrator import extract

TEST_STACK_OVERFLOW_SRC_POSTS_FILE_PATH = "../tests/data/posts_test_data.xml"
TEST_STACK_OVERFLOW_DEST_POSTS_FILE_PATH = "../tests/data/test_questions.tsv"
TEST_STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH = "../tests/data/test_questions_meta.json"


class DataExtractorTests(TestCase):
    def test__convert_posts__correct_data_should_be_extracted(self):

        settings.STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH = TEST_STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH
        settings.STACK_OVERFLOW_DEST_POSTS_FILE_PATH = TEST_STACK_OVERFLOW_DEST_POSTS_FILE_PATH

        extract(TEST_STACK_OVERFLOW_SRC_POSTS_FILE_PATH)

        with open(TEST_STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH, "r") as meta_file:
            meta = json.load(meta_file)
            item_meta = meta["4"]
            self.assertEqual(item_meta[0], 69)
            self.assertEqual(item_meta[1], 4)
            self.assertEqual(item_meta[2], 17.3)
            self.assertEqual(item_meta[3], 3.4)
            self.assertEqual(item_meta[4], 5)
            self.assertEqual(item_meta[5], 0)
            self.assertEqual(item_meta[6], 0)
            self.assertEqual(item_meta[7], 441)
            self.assertEqual(item_meta[8], 12)
            self.assertEqual(item_meta[9], 1117322)
            self.assertEqual(item_meta[10], 13)
            self.assertEqual(item_meta[11], 3)
            self.assertEqual(item_meta[12], 36)
        for line in open(TEST_STACK_OVERFLOW_DEST_POSTS_FILE_PATH, "r"):
            id, text = line.split("\t")
            self.assertEqual(id, "4")
            break
