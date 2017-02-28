from stack_overflow_center.data_extractor.populators.base_populator import BasePopulator


class DefaultPopulator(BasePopulator):
    @staticmethod
    def populate(raw_post, analyzed_post):
        analyzed_post.id = raw_post.id
        analyzed_post.score = raw_post.score
        analyzed_post.answer_count = raw_post.answer_count
        analyzed_post.comment_count = raw_post.comment_count
        analyzed_post.favorite_count = raw_post.favorite_count
