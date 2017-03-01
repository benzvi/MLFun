import json

from stack_overflow_center.data_extractor.writers.base_writer import BaseWriter


class PostsJSONWriter(BaseWriter):
    def __init__(self, path):
        super(PostsJSONWriter, self).__init__(path)
        self.result = {}

    def write(self, analyzed_post):
        self.result[analyzed_post.id] = analyzed_post.to_list()

    def done(self):
        json.dump(self.result, self.file)
        self.file.flush()
        self.file.close()
