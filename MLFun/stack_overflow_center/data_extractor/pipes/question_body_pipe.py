import nltk
import numpy as np
from bs4 import BeautifulSoup

from stack_overflow_center.data_extractor.pipes.base_pipe import BasePipe


class QuestionBodyPipe(BasePipe):

    @staticmethod
    def transform(parsed_post, analyzed_post):
        body = BeautifulSoup(parsed_post.body, 'html.parser')
        analyzed_post.flat_body = parsed_post.body.encode('utf-8').replace("\n", "")

        for code in body.find_all("pre"):
            analyzed_post.code_lines_count += len([line for line in code.text.split("\n") if line])
        while body.pre:
            body.pre.extract()

        analyzed_post.words_count = len(nltk.word_tokenize(body.text))
        analyzed_post.average_sentence_length = round(np.average([len(nltk.word_tokenize(sent)) for sent in nltk.sent_tokenize(body.text)]), 1)
        analyzed_post.average_word_length = round(np.average([len(w) for w in nltk.word_tokenize(body.text)]), 1)
        analyzed_post.caps_count = np.sum([word.isupper() for word in nltk.word_tokenize(body.text)])
        analyzed_post.exclams_count = body.text.count('!')
        analyzed_post.images_count = len(body.find_all("img"))
