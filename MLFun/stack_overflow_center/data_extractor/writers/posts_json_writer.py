import json

from stack_overflow_center.data_extractor.writers.base_writer import BaseWriter


class PostsJSONWriter(BaseWriter):
    def __init__(self, path):
        super(PostsJSONWriter, self).__init__(path)
        self.result = {}

    def write(self, analyzed_post):
        self.result[analyzed_post.id] = {
            'WordsCount': analyzed_post.words_count,
            'CodeLinesCount': analyzed_post.code_lines_count,
            'AvgSentenceLength': analyzed_post.average_sentence_length,
            'AvgWordLength': analyzed_post.average_word_length,
            'CapsCount': analyzed_post.caps_count,
            'ExclamsCount': analyzed_post.exclams_count,
            'ImagesCount': analyzed_post.images_count,
            "Score": analyzed_post.score,
            "TitleWordsCount": analyzed_post.title_words_count,
            "TotalTagsCount": analyzed_post.total_tags_count,
            "AnswerCount": analyzed_post.answer_count,
            "CommentCount": analyzed_post.comment_count,
            "FavoriteCount": analyzed_post.favorite_count
        }

    def done(self):
        json.dump(self.result, self.file)
        self.file.flush()
        self.file.close()
