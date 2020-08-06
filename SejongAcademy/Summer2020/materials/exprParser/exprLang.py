
spcString = "                    "

class Name():
    def __init__(self, value):
        self.type = "Name"
        self.nameText = value

    def toStringNode(self, lvl):
        return "Name: " + self.nameText

    def compile(self, ctx):
        ctx.emit2("LOAD_VAR", ctx.new_var(self.nameText))

class Number():

    def __init__(self, value):
        self.type = "Number"
        self.numberValue = value

    def toStringNode(self, lvl):
#        return spcString[:lvl] + "Val: " + str(self.numberValue)
        return "Val: " + str(self.numberValue)

    def compile(self, ctx):
        ctx.emit2("LOAD_CONST", ctx.new_const(self.numberValue))


class Assign():
    def __init__(self, var, expr):
        self.type = "Assign"
        self.var = var
        self.expr = expr

    def toStringNode(self, lvl):
        return "Assign: " + "\n" + spcString[:lvl+1] + self.var + "\n" + spcString[:lvl+1] +  self.expr.toStringNode(lvl+1)

    def compile(self, ctx):
        self.expr.compile(ctx)
        ctx.new_var(self.var)
        ctx.emit1("POP_TOP")
        ctx.emit2("STORE", self.var)
        pass

class Expr():
    def __init__(self, op, arg1, arg2):
        self.type = "Expr"
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

    def toStringNode(self, lvl):
        return "Expr: " + self.op + "\n" + spcString[:lvl] + str(self.arg1.toStringNode(lvl+1)) + "\n" + spcString[:lvl] + str(self.arg2.toStringNode(lvl+1))
#        return "Expr: " + self.op + "\n" + str(self.arg1.toStringNode(lvl+1)) + "\n" + spcString[:lvl+1] + str(self.arg2.toStringNode(lvl+1))
    
    def compile(self,ctx):
        self.arg1.compile(ctx)
        self.arg2.compile(ctx)
        if (self.op == '+'):
            ctx.emit1("BIN_OP_ADD")
        elif (self.op == '-'):
            ctx.emit1("BIN_OP_SUB")
        elif (self.op == '*'):
            ctx.emit1("BIN_OP_MUL")
        else:
            ctx.emit1("BIN_OP_DIV")

