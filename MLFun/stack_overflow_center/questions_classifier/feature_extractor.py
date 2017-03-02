import json
import numpy


def extract_questions_features(settings):
    with open(settings.STACK_OVERFLOW_DEST_POSTS_META_FILE_PATH, "r") as features_file:
        return numpy.asarray(json.load(features_file).values())