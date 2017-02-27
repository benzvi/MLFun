import json

from django.conf import settings

from stack_overflow_center.data_extractor.pipes.base_pipe import BasePipe


class TagsPipe(BasePipe):

    @staticmethod
    def transform(parsed_post, analyzed_post):
        with open(settings.STACK_OVERFLOW_DEST_TAGS_FILE_PATH) as json_file:
            tags_data = json.load(json_file)

        tags = parsed_post.tags

        count = 0
        tags = tags[1:len(tags) - 1]
        tags = tags.replace("><", ",").split(",")

        for tag in tags:
            count += tags_data[tag]

        analyzed_post.total_tags_count = count