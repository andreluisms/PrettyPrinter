from lexico import *
import ply.yacc as yacc
from sintaxeabstrata import *


def p_exp_1(p):
    '''exp1 : exp1 MAIS exp2
             | exp1 MENOS exp2
             | exp2
    '''
    if (len(p) == 2):
        p[0] = p[1]
    elif (p[2] == '+'):
        p[0] = SomaExp(p[1], p[3])
    else:
        p[0] = SubExp(p[1], p[3])

def p_exp_2(p):
    '''exp2 : exp2 DIV exp3
             | exp2 MUL exp3
             | exp3
    '''
    if (len(p) == 2):
        p[0] = p[1]
    elif (p[2] == '+'):
        p[0] = SomaExp(p[1], p[3])
    else:
        p[0] = SubExp(p[1], p[3])

def p_exp_3(p):
    '''exp3 : NUM
    '''
    p[0] = NumExp(p[1])

def p_error(p):
    print ('Construção inválida envolvendo:', p)

def main():
    print("# teste sintatico.py")
    lexico = lex.lex()
    lexico.input(open('entrada.exp').read())
    sint = yacc.yacc()
    sint.parse(debug = True)


if __name__ == '__main__':
    main()

