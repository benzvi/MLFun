import abc

class BaseWriter(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, path):
        self.file = open(path, "w")

    @abc.abstractmethod
    def write(self, data):
        raise NotImplementedError("Should have implemented this")

    @abc.abstractmethod
    def done(self):
        raise NotImplementedError("Should have implemented this")