from abc import abstractmethod
from abc import ABCMeta

class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visitSomaExp(self, somaexp):
        pass
    @abstractmethod
    def visitSubExp(self, subexp):
        pass
    @abstractmethod
    def visitDivExp(self, divexp):
        pass
    @abstractmethod
    def visitMulExp(self, mulexp):
        pass
    @abstractmethod
    def visitNumExp(self, numexp):
        pass