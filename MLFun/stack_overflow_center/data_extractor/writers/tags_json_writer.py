import json

from stack_overflow_center.data_extractor.writers.base_writer import BaseWriter


class TagsJSONWriter(BaseWriter):
    def __init__(self, path):
        super(TagsJSONWriter, self).__init__(path)
        self.result = {}

    def write(self, tag_data):
        self.result[tag_data[0]] = tag_data[1]

    def done(self):
        json.dump(self.result, self.file)
        self.file.flush()
        self.file.close()
