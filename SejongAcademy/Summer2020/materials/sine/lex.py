
global loc
loc = 0
global buffer
buffer = ''

def initLex(fileName):
    global buffer

    file = open(fileName, 'r')
    line = file.read(1024)
    while (line != ''):
        buffer = buffer + line
        line = file.read(1024)
    file.close()


def nextTok():
    # Check for number
    global loc
    if loc >= len(buffer):
        return ('$$', 0)

    if buffer[loc] >= '0' and buffer[loc] <= '9':
        # Handle integer
        retval = ('num', int(buffer[loc]))

    elif buffer[loc] >= 'a' and buffer[loc] <= 'z':
        # Handle identifier
        retval = ('id', buffer[loc])
                  
    elif buffer[loc] in ['+', '-', '*', '/', '=']:
            retval = ('op', buffer[loc])
    elif buffer[loc] == '(':
        retval = ('lp', buffer[loc])
    elif buffer[loc] == ')':
        print("Debug: Found rp! Loc: " + str(loc) + " len: " + str(len(buffer)))
        retval = ('rp', buffer[loc])
    else:
        retval = ('!', '!')
        loc = loc + 1
        print('Invalid character')

    loc = loc + 1
    while loc < len(buffer) and buffer[loc] in [' ', '\n']:
        loc = loc + 1

    print ("Returning: " + str(retval))
    return retval



