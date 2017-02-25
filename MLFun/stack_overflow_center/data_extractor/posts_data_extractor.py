from django.conf import settings

from stack_overflow_center.data_extractor.xml_parser import parse_posts_xml
from stack_overflow_center.data_extractor.xml_to_tsv_and_json_converter import convert


def extract_posts_data():
        convert(settings.STACK_OVERFLOW_SRC_POSTS_FILE_PATH,
                settings.STACK_OVERFLOW_DEST_POSTS_FILE_PATH,
                settings.STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH,
                parse_posts_xml)