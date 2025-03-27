import sys
from antlr4 import InputStream, CommonTokenStream
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor

def main():
    entrada = input("Ingresa código: ")  
    lexer = MiGramaticaLexer(InputStream(entrada))
    stream = CommonTokenStream(lexer)
    parser = MiGramaticaParser(stream)
    tree = parser.programa()

    print("Árbol generado:", tree.toStringTree(recog=parser))  # 👀 Verificar si el árbol se genera

    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    main()
