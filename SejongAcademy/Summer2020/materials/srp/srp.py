
global loc
loc = 0

def nextTok(theline):
    # Check for number
    global loc
#    print ("Len: " + str(len(theline)))
#    print ("loc: " + str(loc))
    if loc >= len(theline):
        return ('e', 0)

    if theline[loc] >= '0' and theline[loc] <= '9':
        # Handle integer
        retval = ('v', int(theline[loc]))
        loc = loc + 1

    elif theline[loc] in ['+', '-', '*', '/', '=']:
            retval = ('o', theline[loc])
    else:
        retval = ('!', '!')
        loc = loc + 1
        print('Invalid character')

    loc = loc + 1
    while loc < len(theline) and theline[loc] in [' ', '\n']:
        loc = loc + 1

#    print ("Returning: " + str(retval))
    return retval


global stack
global sp

stack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sp = -1

def push(val):
    global stack
    global sp
    if sp > len(stack):
        print("Error stack full!")
    else:
        sp = sp + 1
        stack[sp] = val

def pop():
    global stack
    global sp

    if sp >= 0:
        retval = stack[sp]
        sp = sp - 1
    else:
        retval = ''
    return retval

def do_op(o1, o2, op):
    if op == '+':
        res = int(o1) + int(o2)
    elif op == '-':
        res = int(o1) - int(o2)
    elif op == '*':
        res = int(o1) * int(o2)
    else:
        res = int(o1) / int (o2)
    return res

progfile = open('test.srp', 'r')

nextline = progfile.readline()

print ("Next line: " + nextline)

tok = nextTok(nextline)
while tok[0] != '!' and tok[0] != 'e':
    if tok[0] == 'v':
        print ("Value")
        push(tok[1])
    else:
        print("op")
        o1 = pop()
        o2 = pop()
        res = do_op(o1, o2, tok[1])
        push(res)

    tok = nextTok(nextline)

print("Res: " + str(pop()))

