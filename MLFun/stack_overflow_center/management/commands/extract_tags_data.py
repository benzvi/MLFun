from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from stack_overflow_center.data_extractor.tags_data_extractor import extract_tags_data
from stack_overflow_center.data_extractor.xml_parser import parse_tags_xml


class Command(BaseCommand):
    help = 'Extract stack overflow tags data from the large xml file'

    def handle(self, *args, **options):
        extract_tags_data(settings.STACK_OVERFLOW_SRC_TAGS_FILE_PATH,
                          settings.STACK_OVERFLOW_DEST_TAGS_FILE_PATH,
                          parse_tags_xml)

        print "Finished extracting tags data successfully"
