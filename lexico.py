import ply.lex as lex

tokens = ['MAIS', 'MENOS', 'MUL', 'DIV', 'NUM']
t_MAIS='\+'
t_MENOS='-'
t_MUL='\*'
t_DIV='/'
t_NUM='(0 | [1-9][0-9]*)'

def t_brancos(t):
    '[\t\n ]'
    pass

def t_error(t):
    print('Token desconhecido =', t.value)
    t.lexer.skip(1)

def main():
    print("# teste lexico.py")
    lexico = lex.lex()
    lexico.input(open('entrada.exp').read())
    for tok in lexico:
        print(tok.type, tok.value)
    



if __name__ == '__main__':
    main()