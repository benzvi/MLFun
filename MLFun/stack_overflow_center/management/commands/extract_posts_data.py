from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from stack_overflow_center.data_extractor.xml_parser import parse_posts_xml
from stack_overflow_center.data_extractor.posts_data_extractor import extract_posts_data


class Command(BaseCommand):
    help = 'Extract stack overflow posts data from the large xml file'

    def handle(self, *args, **options):
        start_time = datetime.now()
        extract_posts_data(settings.STACK_OVERFLOW_SRC_POSTS_FILE_PATH,
                           settings.STACK_OVERFLOW_DEST_POSTS_FILE_PATH,
                           settings.STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH,
                           parse_posts_xml)

        end_time = datetime.now()
        print "Total time: %s" % (end_time - start_time)
        print "Finished extracting posts data successfully"