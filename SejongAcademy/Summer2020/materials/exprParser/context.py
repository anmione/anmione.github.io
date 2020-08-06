
class Context:
    def __init__(self):
        self.constants = []
        self.variables = dict([])
        self.program = []
        self.stack = []
        self.last_popped = 0

    def new_var(self, name):
        if name not in self.variables:
            self.variables[name] = 0

    def new_const(self, number):
        self.constants.append(number)
        return len(self.constants)-1

    def emit1(self, op):
        self.program.append((op))

    def emit2(self, op, arg):
        self.program.append((op, arg))


    def programCode(self):
        return self.program
    
    def getStack(self):
        return self.stack
    
    def execute(self):
        pc = 0
        while pc < len(self.program):
#            print("Debug: " + str(self.program[pc]))
#            print("Debug: " + str(self.program[pc][0]))
            if self.program[pc][0] == 'LOAD_CONST':
#                print("Debug: Pushing!")
                self.stack.append(self.constants[self.program[pc][1]])

            elif self.program[pc][0] == 'LOAD_VAR':
                
#                print("Debug: Pushing var!")
                self.stack.append(self.variables[self.program[pc][1]])

            elif self.program[pc] == 'POP_TOP':
                self.last_popped = self.stack.pop()
            elif self.program[pc][0] == 'STORE':
                self.variables[self.program[pc][1]] = self.last_popped
                self.last_popped = 0
            elif self.program[pc] == 'BIN_OP_MUL':
                arg2 = self.stack.pop()
                arg1 = self.stack.pop()
                res = arg1 * arg2
                self.stack.append(res)
            elif self.program[pc] == 'BIN_OP_SUB':
                arg2 = self.stack.pop()
                arg1 = self.stack.pop()
                res = arg1 - arg2
                self.stack.append(res)
            elif self.program[pc] == 'BIN_OP_ADD':
                arg2 = self.stack.pop()
                arg1 = self.stack.pop()
                res = arg1 + arg2
                self.stack.append(res)
            elif self.program[pc] == 'BIN_OP_DIV':
                arg2 = self.stack.pop()
                arg1 = self.stack.pop()
                res = arg1 / arg2
                self.stack.append(res)

            else:
                pass
#                print("Debug: gaaa!")
            pc = pc + 1
#        print("Out of loop")
        print(str(self.stack))
