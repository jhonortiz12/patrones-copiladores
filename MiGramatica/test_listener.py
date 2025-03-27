import sys
from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MyListener import MyListener
from antlr4.tree.Tree import ParseTreeWalker

print("Ingresa código (finaliza con Ctrl+D en Linux/macOS o Ctrl+Z + Enter en Windows):")
input_text = sys.stdin.read()
input_stream = InputStream(input_text)
lexer = MiGramaticaLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = MiGramaticaParser(token_stream)
tree = parser.programa()

walker = ParseTreeWalker()
listener = MyListener()
walker.walk(listener, tree)
