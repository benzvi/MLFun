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
    meta_data = {}
    for event, element in etree.iterparse(path, tag="row"):

        post_type = int(element.get("PostTypeId"))

        if post_type == QUESTION_TYPE:
            creation_date = datetime.strptime(element.get("CreationDate"), "%Y-%m-%dT%H:%M:%S.%f")
            if creation_date.year >= OLDEST_RELEVANT_YEAR:
                id = element.get('Id')

                question_body = BeautifulSoup(element.get("Body"), 'html.parser')
                meta_data[id] = _calculate_features_from_question_body(question_body)
                meta_data[id].update({
                    "Score": int(element.get('Score')),
                    "TitleWordsCount": len(element.get("Title").split(" ")),
                    "TotalTagsCount": _calculate_total_tags_count(element.get("Tags")),
                    "AnswerCount": int(element.get("AnswerCount")),
                    "CommentCount": int(element.get("CommentCount")),
                    "FavoriteCount": int(element.get("FavoriteCount"))
                })

                yield [element.get("Id"), question_body]

        element.clear()

    yield meta_data


def parse_tags_xml(path):
    result = {}
    for event, element in etree.iterparse(path, tag="row"):
        result[element.get("TagName")] = int(element.get("Count"))
        element.clear()

    return result


def _calculate_features_from_question_body(body):
    code_lines_count = 0

    for code in body.find_all("pre"):
        code_lines_count += len([line for line in code.text.split("\n") if line])
        pass

    while body.pre:
        body.pre.extract()

    words_count = len(nltk.word_tokenize(body.text))
    avg_sentence_length = np.average([len(nltk.word_tokenize(sent)) for sent in nltk.sent_tokenize(body.text)])
    avg_word_length = np.average([len(w) for w in nltk.word_tokenize(body.text)])
    caps_count = np.sum([word.isupper() for word in nltk.word_tokenize(body.text)])
    exclams_count = body.text.count('!')
    images_count = len(body.find_all("img"))

    return {
        'WordsCount': words_count,
        'CodeLinesCount': code_lines_count,
        'AvgSentenceLength': avg_sentence_length,
        'AvgWordLength': avg_word_length,
        'CapsCount': caps_count,
        'ExclamsCount': exclams_count,
        'ImagesCount': images_count,
    }


def _calculate_total_tags_count(tags):
    count = 0

    tags = tags[1:len(tags) - 1]
    tags = tags.replace("><", ",").split(",")

    for tag in tags:
        count += tags_data[tag]

    return count
