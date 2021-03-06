from django.conf import settings

from stack_overflow_center.data_extractor.xml_parser import parse_tags_xml
from stack_overflow_center.data_extractor.writers.tags_json_writer import TagsJSONWriter

def extract(from_path):

    writer = TagsJSONWriter(settings.STACK_OVERFLOW_DEST_TAGS_FILE_PATH)

    for data in parse_tags_xml(from_path):
        writer.write(data)


    writer.done()