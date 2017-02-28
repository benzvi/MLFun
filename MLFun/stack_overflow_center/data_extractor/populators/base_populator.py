class BasePopulator(object):
    @staticmethod
    def populate(raw_object, analyzed_object):
        """
        Populates specified raw_object to specified analyzed_object
        """
        raise NotImplementedError("Should have implemented this")