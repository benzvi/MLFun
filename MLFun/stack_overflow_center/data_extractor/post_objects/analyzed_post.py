
class AnalyzedPost(object):
    def __init__(self):
        self.id = ""
        self.score = 0
        self.answer_count = 0
        self.comment_count = 0
        self.favorite_count = 0
        self.flat_body = ""
        self.words_count = 0
        self.code_lines_count = 0
        self.average_sentence_length = 0
        self.average_word_length = 0
        self.caps_count = 0
        self.exclams_count = 0
        self.images_count = 0
        self.title_words_count = 0
        self.total_tags_count = 0


    def to_list(self):
        return [
            self.words_count,
            self.code_lines_count,
            self.average_sentence_length,
            self.average_word_length,
            self.caps_count,
            self.exclams_count,
            self.images_count,
            self.score,
            self.title_words_count,
            self.total_tags_count,
            self.answer_count,
            self.comment_count,
            self.favorite_count
        ]