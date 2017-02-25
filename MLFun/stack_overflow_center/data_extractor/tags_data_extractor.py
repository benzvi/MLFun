from django.conf import settings

from stack_overflow_center.data_extractor.xml_parser import parse_tags_xml
from stack_overflow_center.data_extractor.xml_to_json_converter import convert


def extract_tags_data():
    convert(settings.STACK_OVERFLOW_SRC_TAGS_FILE_PATH, settings.STACK_OVERFLOW_DEST_TAGS_FILE_PATH, parse_tags_xml)
