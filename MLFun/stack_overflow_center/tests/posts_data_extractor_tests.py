import json

from django.test import TestCase

from stack_overflow_center.data_extractor.xml_parser import parse_posts_xml
from stack_overflow_center.data_extractor.posts_data_extractor import convert

TEST_STACK_OVERFLOW_SRC_POSTS_FILE_PATH = "../tests/data/posts_test_data.xml"
TEST_STACK_OVERFLOW_DEST_POSTS_FILE_PATH = "../tests/data/test_questions.tsv"
TEST_STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH = "../tests/data/test_questions_meta.json"


class DataExtractorTests(TestCase):
    def test__convert_posts__correct_data_should_be_extracted(self):
        convert(TEST_STACK_OVERFLOW_SRC_POSTS_FILE_PATH,
                TEST_STACK_OVERFLOW_DEST_POSTS_FILE_PATH,
                TEST_STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH,
                parse_posts_xml)

        with open(TEST_STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH, "r") as meta_file:
            meta = json.load(meta_file)
            item_meta = meta["4"]
            self.assertEqual(item_meta["TotalTagsCount"], 1117322)
            self.assertEqual(item_meta["AnswerCount"], 13)
            self.assertEqual(item_meta["CommentCount"], 3)
            self.assertEqual(item_meta["ExclamsCount"], 0)
            self.assertEqual(item_meta["CapsCount"], 5)
            self.assertEqual(item_meta["Score"], 441)
            self.assertEqual(item_meta["TitleWordsCount"], 12)
            self.assertEqual(item_meta["WordsCount"], 69)
            self.assertEqual(item_meta["ImagesCount"], 0)
            self.assertEqual(item_meta["CodeLinesCount"], 4)
            self.assertEqual(item_meta["AvgWordLength"], 3.4)
            self.assertEqual(item_meta["AvgSentenceLength"], 17.3)

        for line in open(TEST_STACK_OVERFLOW_DEST_POSTS_FILE_PATH, "r"):
            id, text = line.split("\t")

            self.assertEqual(id, "4")
