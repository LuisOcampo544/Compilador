from .GrammarVisitor import GrammarVisitor
from .GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    # Definimos la maemoria o el entorno 
    def __init__(self):
        self.memory = {}

    # Definimos la asignacion
    def visitAssing(self,ctx:GrammarParser.AssingContext):
        # Se obtiene el tipo de variable (int, string)
        var_type = ctx.type_().getText()
        # Se obtiene el ID o nombre de la variable
        name = ctx.ID().getText()
        # Se obtiene el valor, ya sea un valor numerico o una expresion
        value = self.visit(ctx.expr())
    

        # Se almacena en memoria a partir del nombre y el valor
        # self.memory[name] = value

        # Validacion de tipos
        if var_type == 'int' and not isinstance(value, int):
            raise TypeError(f"Error en '{name}")
        
        if var_type == 'string' and not isinstance(value, str):
            raise TypeError(f"Error en '{name}")
        
        # Se almacena en memoria el valor y su tipo
        self.memory[name] = {'value': value, 'type': var_type}

    # Definimos la impresion
    def visitPrint(self,ctx:GrammarParser.PrintContext):
        # Definimos la expresion que se desea mostrar
        value=self.visit(ctx.expr())
        # Imprime el valor
        print(value)

    # Definimos las expresiones
    def visitExpr(self, ctx):
        # Busca si existen ID's
        if ctx.ID():
            # Obtiene del contexto el nombre de la variable
            name=ctx.ID().getText()
            # Si el nombre de la variable no esta, lanza un error
            if name not in self.memory:
                raise NameError(f"Variable '{name}' no definida")
            # Si existe el nombre retorna la variable
            return self.memory[name]['value']
        # Busca si es un numero
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        # Busca si es un string
        elif ctx.STRING():
            text=ctx.STRING().getText()
            return text[1:-1]
        # Busca el operador
        elif ctx.op:
            # Visita y obtiene lado izquierdo
            left=self.visit(ctx.expr(0))
            # Visita y obtiene lado derecho
            right=self.visit(ctx.expr(1))
            # Evalua la oepracion a realizar
            if ctx.op.text == '+':
                return left + right
            if ctx.op.text == '-':
                return left - right
            if ctx.op.text == '*':
                return left * right
            if ctx.op.text == '/':
                # Verifica la division de cero
                if right == 0:
                    raise ValueError("Division por cero")
                return left / right
            

