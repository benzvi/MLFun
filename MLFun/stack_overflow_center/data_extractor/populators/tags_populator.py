
from django.conf import settings

from stack_overflow_center.data_extractor.populators.base_populator import BasePopulator
from stack_overflow_center.data_extractor.tags_data_repository import get_tags_data


class TagsPopulator(BasePopulator):

    @staticmethod
    def populate(parsed_post, analyzed_post):
        tags_data = get_tags_data(settings.STACK_OVERFLOW_DEST_TAGS_FILE_PATH)

        tags = parsed_post.tags

        count = 0
        tags = tags[1:len(tags) - 1]
        tags = tags.replace("><", ",").split(",")

        for tag in tags:
            count += tags_data[tag]

        analyzed_post.total_tags_count = count