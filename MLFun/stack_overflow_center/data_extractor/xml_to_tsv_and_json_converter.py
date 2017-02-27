import json

from stack_overflow_center.data_extractor.config import PIPES
from stack_overflow_center.data_extractor.xml_parser import parse_posts_xml
from stack_overflow_center.data_extractor.analyzed_post import AnalyzedPost
from stack_overflow_center.data_extractor.writers.posts_writers_provider import PostsWritersProvider


def convert(from_path):
    writers = PostsWritersProvider().get_writers()
    for raw_post in parse_posts_xml(from_path):
        analyzed_post = AnalyzedPost(raw_post.id,
                                     raw_post.score,
                                     raw_post.answer_count,
                                     raw_post.comment_count,
                                     raw_post.favorite_count)

        for pipe in PIPES:
            pipe.transform(raw_post, analyzed_post)

        for writer in writers:
            writer.write(analyzed_post)

    for writer in writers:
        writer.done()
