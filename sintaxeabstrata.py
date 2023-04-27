from abc import abstractmethod
from abc import ABCMeta

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        visitor.visitSomaExp(self)

class SubExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        visitor.visitSubExp(self)

class DivExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        visitor.visitDivExp(self)

class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        visitor.visitMulExp(self)

class NumExp(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        visitor.visitNumExp(self)




# Tenta instanciar um objeto de cada classe concreta desse módulo. Caso não consiga, será lançado erro
def main():
    print("# teste sintaxeabstrata.py")
    import sys, inspect
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and obj.__name__ != 'ABCMeta' and obj.__name__ != 'Exp':
            a = obj()


if __name__ == '__main__':
    main()