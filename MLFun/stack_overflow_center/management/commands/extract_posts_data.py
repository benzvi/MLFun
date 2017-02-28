from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from stack_overflow_center.data_extractor.posts_data_extrator import extract


class Command(BaseCommand):
    help = 'Extract stack overflow posts data from the large xml file'

    def handle(self, *args, **options):
        start_time = datetime.now()
        extract(settings.STACK_OVERFLOW_SRC_POSTS_FILE_PATH)

        end_time = datetime.now()
        print "Total time: %s" % (end_time - start_time)
        print "Finished extracting posts data successfully"
