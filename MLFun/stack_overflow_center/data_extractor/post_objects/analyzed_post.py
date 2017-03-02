class AnalyzedPost(object):
    def __init__(self, id="", score=0, answer_count=0, comment_count=0, favorite_count=0, flat_body="", words_count=0,
                 code_lines_count=0, average_sentence_length=0, average_word_length=0, caps_count=0, exclams_count=0,
                 images_count=0, title_words_count=0, total_tags_count=0):

        self.id = id
        self.score = score
        self.answer_count = answer_count
        self.comment_count = comment_count
        self.favorite_count = favorite_count
        self.flat_body = flat_body
        self.words_count = words_count
        self.code_lines_count = code_lines_count
        self.average_sentence_length = average_sentence_length
        self.average_word_length = average_word_length
        self.caps_count = caps_count
        self.exclams_count = exclams_count
        self.images_count = images_count
        self.title_words_count = title_words_count
        self.total_tags_count = total_tags_count

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
