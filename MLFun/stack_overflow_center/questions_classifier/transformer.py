from stack_overflow_center.data_extractor.config import POPULATORS
from stack_overflow_center.data_extractor.post_objects.analyzed_post import AnalyzedPost
from stack_overflow_center.questions_classifier.feature_extractor import extract_questions_features


def transform(raw_post):
    analyzed_post = AnalyzedPost()

    for populator in POPULATORS:
        populator.populate(raw_post, analyzed_post)

    return extract_questions_features(analyzed_post.to_list())