
class AnalyzedPost(object):
    def __init__(self, id, score, answer_count, comment_count, favorite_count):
        self.id = id
        self.score = score
        self.answer_count = answer_count
        self.comment_count = comment_count
        self.favorite_count = favorite_count
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