import json
from lxml import etree
from datetime import datetime

from stack_overflow_center.data_extractor.raw_post import RawPost

QUESTION_TYPE = 1
OLDEST_RELEVANT_YEAR = 2015


def parse_posts_xml(path):
    for i, (event, element) in enumerate(etree.iterparse(path, tag="row")):

        if i >= 100000 and i % 100000 == 0:
            print "Went over %s posts" % i

        post_type = int(element.get("PostTypeId"))

        if post_type == QUESTION_TYPE:
            creation_date = datetime.strptime(element.get("CreationDate"), "%Y-%m-%dT%H:%M:%S.%f")
            if creation_date.year >= OLDEST_RELEVANT_YEAR:
                yield RawPost(element.get('Id'), element.get("Body"), int(element.get('Score') or 0),
                                        element.get("Title"), element.get("Tags"), int(element.get("AnswerCount") or 0),
                                        int(element.get("CommentCount") or 0), int(element.get("FavoriteCount") or 0))

        element.clear()


def parse_tags_xml(path):
    for event, element in etree.iterparse(path, tag="row"):
        yield element.get("TagName"), int(element.get("Count"))
        element.clear()
