from MiGramaticaVisitor import MiGramaticaVisitor
from MiGramaticaParser import MiGramaticaParser

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}  # Diccionario para almacenar variables

    def visitAssign(self, ctx: MiGramaticaParser.AsignacionContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var_name] = value
        print(f"Asignación: {var_name} = {value}")  # Depuración

    def visitForLoop(self, ctx: MiGramaticaParser.ForLoopContext):
        print("Iniciando ciclo for...")  # Depuración

        init_var = ctx.inicializacion().ID().getText()
        init_value = self.visit(ctx.inicializacion().expresion())
        self.variables[init_var] = init_value
        print(f"Inicialización: {init_var} = {init_value}")  # Depuración

        left_expr = ctx.condicion().expresion(0)
        right_expr = ctx.condicion().expresion(1)
        op = ctx.condicion().op.text

        update_var = ctx.actualizacion().ID().getText()
        update_expr = ctx.actualizacion().expresion()

        while self.eval_condition(self.variables[init_var], self.visit(right_expr), op):
            print(f"Iteración (i = {self.variables[init_var]})")  # Depuración
            for stmt in ctx.sentencia():
                self.visit(stmt)

            # Corrección: Actualizar la variable de iteración
            self.variables[init_var] = self.visit(update_expr)
            print(f"Nueva actualización: {init_var} = {self.variables[init_var]}")  # Depuración

    def eval_condition(self, left, right, op):
        if op == "<":
            return left < right
        elif op == ">":
            return left > right
        elif op == "==":
            return left == right
        elif op == "!=":
            return left != right
        return False

    def visitAddSub(self, ctx: MiGramaticaParser.AddSubContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        result = left + right if ctx.op.text == "+" else left - right
        print(f"Operación: {left} {ctx.op.text} {right} = {result}")  # Depuración
        return result

    def visitMulDiv(self, ctx: MiGramaticaParser.MulDivContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        result = left * right if ctx.op.text == "*" else left / right
        print(f"Operación: {left} {ctx.op.text} {right} = {result}")  # Depuración
        return result

    def visitInt(self, ctx: MiGramaticaParser.IntContext):
        return int(ctx.INT().getText())

    def visitVariable(self, ctx: MiGramaticaParser.VariableContext):
        var_name = ctx.ID().getText()
        value = self.variables.get(var_name, 0)  # Evita errores si la variable no existe
        print(f"Variable '{var_name}' = {value}")  # Depuración
        return value

    def visitParens(self, ctx: MiGramaticaParser.ParensContext):
        return self.visit(ctx.expresion())
