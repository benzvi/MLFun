from stack_overflow_center.data_extractor.populators.base_populator import BasePopulator


class TitlePopulator(BasePopulator):

    @staticmethod
    def populate(raw_post, analyzed_post):
        analyzed_post.title_words_count = len(raw_post.title.split(" "))