from visitorprettyprinter import *
from sintatico import *

# Testando prettyprinter
print("# main.py")
lexico = lex.lex()
lexico.input(open('entrada.exp').read())
sint = yacc.yacc()
tree = sint.parse(debug = True)
vp = VisitorPrettyPrinter()
tree.accept(vp)
print('')