import json
import nltk
import numpy as np
from lxml import etree
from datetime import datetime
from bs4 import BeautifulSoup

from django.conf import settings

QUESTION_TYPE = 1
OLDEST_RELEVANT_YEAR = 2015

with open(settings.STACK_OVERFLOW_DEST_TAGS_FILE_PATH) as json_file:
    tags_data = json.load(json_file)


def parse_posts_xml(path):

    for event, element in etree.iterparse(path, tag="row"):

        post_type = int(element.get("PostTypeId"))

        if post_type == QUESTION_TYPE:
            creation_date = datetime.strptime(element.get("CreationDate"), "%Y-%m-%dT%H:%M:%S.%f")
            if creation_date.year >= OLDEST_RELEVANT_YEAR:
                id = element.get('Id')
                flat_body = element.get("Body").replace("\n", "")
                result = [id, flat_body]

                question_body = BeautifulSoup(element.get("Body"), 'html.parser')
                result += _calculate_features_from_question_body(question_body)

                result += [
                    int(element.get('Score')),
                    len(element.get("Title").split(" ")),
                    _calculate_total_tags_count(element.get("Tags")),
                    int(element.get("AnswerCount")),
                    int(element.get("CommentCount")),
                    int(element.get("FavoriteCount"))
                ]

                yield result

        element.clear()


def parse_tags_xml(path):
    for event, element in etree.iterparse(path, tag="row"):
        yield element.get("TagName"), int(element.get("Count"))
        element.clear()


def _calculate_features_from_question_body(body):
    code_lines_count = 0

    for code in body.find_all("pre"):
        code_lines_count += len([line for line in code.text.split("\n") if line])
    while body.pre:
        body.pre.extract()

    words_count = len(nltk.word_tokenize(body.text))
    avg_sentence_length = np.average([len(nltk.word_tokenize(sent)) for sent in nltk.sent_tokenize(body.text)])
    avg_word_length = np.average([len(w) for w in nltk.word_tokenize(body.text)])
    caps_count = np.sum([word.isupper() for word in nltk.word_tokenize(body.text)])
    exclams_count = body.text.count('!')
    images_count = len(body.find_all("img"))

    return [
        words_count,
        code_lines_count,
        round(avg_sentence_length, 1),
        round(avg_word_length, 1),
        caps_count, exclams_count,
        images_count
    ]


def _calculate_total_tags_count(tags):
    count = 0

    tags = tags[1:len(tags) - 1]
    tags = tags.replace("><", ",").split(",")

    for tag in tags:
        count += tags_data[tag]

    return count
