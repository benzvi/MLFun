from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from stack_overflow_center.data_extractor.xml_parser import parse_tags_xml
from stack_overflow_center.data_extractor.xml_to_json_converter import convert


class Command(BaseCommand):
    help = 'Extract stack overflow tags data from the large xml file'

    def handle(self, *args, **options):
        convert(settings.STACK_OVERFLOW_SRC_TAGS_FILE_PATH,
                settings.STACK_OVERFLOW_DEST_TAGS_FILE_PATH,
                parse_tags_xml)

        print "Finished extracting tags data successfully"
