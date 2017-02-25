
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
        pass
