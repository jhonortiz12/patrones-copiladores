from antlr4 import InputStream, CommonTokenStream
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor

# Leer la entrada del usuario
codigo = input("Ingresa código: ")

# Crear el lexer y el parser
input_stream = InputStream(codigo)
lexer = MiGramaticaLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = MiGramaticaParser(token_stream)

# Iniciar el análisis sintáctico
tree = parser.programa()

# Verificar si hay errores
if parser.getNumberOfSyntaxErrors() > 0:
    print("Hubo errores en la entrada.")
else:
    # Visitar el árbol sintáctico
    visitor = EvalVisitor()
    visitor.visit(tree)
