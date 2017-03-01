from django.conf import settings

from stack_overflow_center.data_extractor.config import POPULATORS
from stack_overflow_center.data_extractor.post_objects.analyzed_post import AnalyzedPost
from stack_overflow_center.data_extractor.writers.posts_writers_provider import PostsWritersProvider
from stack_overflow_center.data_extractor.xml_parser import parse_posts_xml


def extract(from_path):
    writers = PostsWritersProvider(settings).get_writers()
    for raw_post in parse_posts_xml(from_path):
        analyzed_post = AnalyzedPost()

        for populator in POPULATORS:
            populator.populate(raw_post, analyzed_post)

        for writer in writers:
            writer.write(analyzed_post)

    for writer in writers:
        writer.done()
