from django.conf import settings

from stack_overflow_center.data_extractor.writers.posts_tsv_writer import PostsTSVWriter
from stack_overflow_center.data_extractor.writers.posts_json_writer import PostsJSONWriter


class PostsWritersProvider(object):
    def __init__(self):
        self._writers = [
            PostsJSONWriter(settings.STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH),
            PostsTSVWriter(settings.STACK_OVERFLOW_DEST_POSTS_FILE_PATH)
        ]

    def get_writers(self):
        return self._writers
