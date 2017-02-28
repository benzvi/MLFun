import json

from stack_overflow_center.data_extractor.writers.base_writer import BaseWriter


class PostsJSONWriter(BaseWriter):
    def __init__(self, path):
        super(PostsJSONWriter, self).__init__(path)
        self.result = {}

    def write(self, analyzed_post):
        self.result[analyzed_post.id] = [
            analyzed_post.words_count,
            analyzed_post.code_lines_count,
            analyzed_post.average_sentence_length,
            analyzed_post.average_word_length,
            analyzed_post.caps_count,
            analyzed_post.exclams_count,
            analyzed_post.images_count,
            analyzed_post.score,
            analyzed_post.title_words_count,
            analyzed_post.total_tags_count,
            analyzed_post.answer_count,
            analyzed_post.comment_count,
            analyzed_post.favorite_count
        ]

    def done(self):
        json.dump(self.result, self.file)
        self.file.flush()
        self.file.close()
