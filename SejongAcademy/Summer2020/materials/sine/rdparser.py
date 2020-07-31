
import lex
import sys



global currentTok
currentTok = ()


# S => E | e
# E => T Etail
# Etail => + T Etail | - T Etail | e
# T => F Ttail
# Ttail => * F Ttail | / F Ttail | e
# F => id 
# F => number
# F => (E)


def parse(fileName):
    global currentTok


    lex.initLex(fileName)
    currentTok = lex.nextTok()
    res = start()
    if res:
        print("Parse succeeded!")

def start():
    global currentTok

    if currentTok[0] == '$$':
        return True
    return expr()


def expr():
    global currentTok

    if currentTok[0] in ['id', 'num', 'lp']:
        print("E => T Etail")
        term()
        etail()
        return True
    else:
        print('Error. Bad token')
        return False

def term():
    global currentTok

    if currentTok[0] in ['id', 'num', 'lp']:
        print("T => F Ttail")
        factor()
        ttail()
    else:
        print('Error. Bad token')
        return False
        
def etail():
    global currentTok

    if currentTok[1] in ['+', '-']:
        operator = currentTok[1]
        print("Etail => + T Etail | - T Etail")
        currentTok = lex.nextTok()
        term()
        etail()
    else:
        print("Etail => e")
        

def ttail():
    global currentTok

    if currentTok[1] in ['*', '/']:
        operator = currentTok[1]
        currentTok = lex.nextTok()
        print("Ttail => * F Ttail | / F Ttail")
        term()
        etail()
    else:
        print("Ttail => e")


def factor():
    global currentTok
    
    if currentTok[0] == 'id':
        # Symbol table check/add
        print("F => id")
        currentTok = lex.nextTok()
    elif currentTok[0] == 'num':
        print("F => num")
        currentTok = lex.nextTok()
    else: 
        print("F => (E)")
        currentTok = lex.nextTok()
        expr()
        # Should be 'rp'
        if currentTok[0] == 'rp':
            currentTok = lex.nextTok()
        else:
            print("Error. Bad token")
            return False
    return True
        
if len(sys.argv) < 1:
    print('Usage: rdparser.py <filename>')
    sys.exit()

parse(sys.argv[1])



