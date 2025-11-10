from GrammarVisitor import GrammarVisitor
from GramarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def _init__(self):
        self.memory = {}

    # Definimos la asignacion
    def visitAssign(self,ctx):
        name=ctx.ID().getText()
        value=self.visit(ctx.expr())
        self.memory[name]=value
    
    # Definimos la impresion
    def visitPrint(self,ctx):
        value=self.visit(ctx.expr())
        print(value)

