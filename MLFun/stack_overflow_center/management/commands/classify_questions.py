from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from stack_overflow_center.questions_classifier.classifier import classify


class Command(BaseCommand):
    help = 'Classify stack overflow questions'

    def handle(self, *args, **options):
        start_time = datetime.now()
        classify()

        end_time = datetime.now()
        print "Total time: %s" % (end_time - start_time)
        print "Finished classifying questions successfully"
