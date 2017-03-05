from datetime import datetime

from lxml import etree

from stack_overflow_center.data_extractor.post_objects.raw_post import RawPost

QUESTION_TYPE = 1
OLDEST_RELEVANT_YEAR = 2015


def parse_posts_xml(path):
    for i, (event, element) in enumerate(etree.iterparse(path, tag="row")):

        if i >= 100000 and i % 100000 == 0:
            print "Went over %s posts" % i

        yield _parse_post(element)
        element.clear()


def parse_post_from_client(post):
    return _parse_post(post)


def _parse_post(post):
    post_type = int(post.get("PostTypeId"))

    if post_type == QUESTION_TYPE:
        creation_date = datetime.strptime(post.get("CreationDate"), "%Y-%m-%dT%H:%M:%S.%f")
        if creation_date.year >= OLDEST_RELEVANT_YEAR:
            return RawPost(post.get('Id'), post.get("Body"), int(post.get('Score') or 0),
                           post.get("Title"), post.get("Tags"), int(post.get("AnswerCount") or 0),
                           int(post.get("CommentCount") or 0), int(post.get("FavoriteCount") or 0))


def parse_tags_xml(path):
    for event, element in etree.iterparse(path, tag="row"):
        yield element.get("TagName"), int(element.get("Count"))
        element.clear()
