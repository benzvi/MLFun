class BasePipe(object):
    @staticmethod
    def transform(parsed_object, result):
        """
        Transforms specified parsed_object object to specified result object
        """
        raise NotImplementedError("Should have implemented this")