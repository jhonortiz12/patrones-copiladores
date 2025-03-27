from MiGramaticaVisitor import MiGramaticaVisitor
from MiGramaticaParser import MiGramaticaParser

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}  # Diccionario para almacenar variables

    def visitAssign(self, ctx: MiGramaticaParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expresion())  
        self.variables[var_name] = value
        print(f"Asignación: {var_name} = {value}")

    def visitForLoop(self, ctx: MiGramaticaParser.ForLoopContext):
        init_var = ctx.inicializacion().ID().getText()
        init_value = self.visit(ctx.inicializacion().expresion())  
        self.variables[init_var] = init_value

        left_expr = ctx.condicion().expresion(0)
        right_expr = ctx.condicion().expresion(1)
        op = ctx.condicion().op.text  

        update_var = ctx.actualizacion().ID().getText()
        update_expr = ctx.actualizacion().expresion()

        while self.eval_condition(self.visit(left_expr), self.visit(right_expr), op):
            for stmt in ctx.sentencia():
                self.visit(stmt)  
            self.variables[update_var] = self.visit(update_expr)

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

    def visitMul(self, ctx: MiGramaticaParser.MulContext):
        return self.visit(ctx.expresion(0)) * self.visit(ctx.expresion(1))

    def visitDiv(self, ctx: MiGramaticaParser.DivContext):
        return self.visit(ctx.expresion(0)) / self.visit(ctx.expresion(1))

    def visitAdd(self, ctx: MiGramaticaParser.AddContext):
        return self.visit(ctx.expresion(0)) + self.visit(ctx.expresion(1))

    def visitSub(self, ctx: MiGramaticaParser.SubContext):
        return self.visit(ctx.expresion(0)) - self.visit(ctx.expresion(1))

    def visitInt(self, ctx: MiGramaticaParser.IntContext):
        return int(ctx.INT().getText())

    def visitVariable(self, ctx: MiGramaticaParser.VariableContext):
        var_name = ctx.ID().getText()
        return self.variables.get(var_name, 0)  

    def visitParens(self, ctx: MiGramaticaParser.ParensContext):
        return self.visit(ctx.expresion())
