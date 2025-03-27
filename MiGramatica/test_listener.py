from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MiGramaticaListener import MiGramaticaListener
from MyListener import MyListener

def main():
    entrada = input("Ingresa código: ")
    input_stream = InputStream(entrada)
    lexer = MiGramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiGramaticaParser(stream)
    tree = parser.programa()

    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == "__main__":
    main()
