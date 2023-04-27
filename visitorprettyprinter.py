from visitor import *
from sintaxeabstrata import *

class VisitorPrettyPrinter(Visitor):
    def visitSomaExp(self, somaexp):
        somaexp.exp1.accept(self)
        print(' + ', end='')
        somaexp.exp2.accept(self)
    def visitSubExp(self, subexp):
        subexp.exp1.accept(self)
        print(' - ', end='')
        subexp.exp2.accept(self)
    def visitDivExp(self, divexp):
        divexp.exp1.accept(self)
        print(' / ', end='')
        divexp.exp2.accept(self)
    def visitMulExp(self, mulexp):
        mulexp.exp1.accept(self)
        print(' * ', end='')
        mulexp.exp2.accept(self)
    def visitNumExp(self, numexp):
        print(numexp.exp, end='')


# Tenta instanciar um objeto da classe VistitorPrettyPrinter. Caso não consiga, será lançado erro
def main():
    vis = VisitorPrettyPrinter()
    SomaExp(NumExp(3), NumExp(4)).accept(vis)
    print('')

if __name__ == '__main__':
    main()