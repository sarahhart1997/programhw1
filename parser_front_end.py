'''
This program implements a recursive descent parser for the CFG below.
It does not implement the last rule:
    <factor> -> (<exp>)
Add code to the factor() function to implement this.

------------------------------------------------------------
1 <exp> → <term>{+<term> | -<term>}
2 <term> → <factor>{*<factor> | /<factor>}
3 <factor> → <number> | pi | -<factor> | (<exp>)
'''

from backend_modules.numeric import *
#from postfix import *
#from lisp import *
#from function import *
#from stack import *

class ParseError(Exception):
    def __init__(self, err):
        print(err)

#==============================================================
# FRONT END PARSER
#==============================================================

token_index = 0 # keeps track of what character we are currently reading.

def lookahead(): return w[token_index]

def read_token():
    global token_index
    token_index += 1
#---------------------------------------
# Parse an Expression   <exp> → <term>{+<term> | -<term>}
#
def exp():
    value = term()
    while True:
        if lookahead() == '+':
            read_token()
            value = binary_op('+', value, term())
        elif lookahead() == '-':
            read_token()
            value = binary_op('-', value, term())
        else:
            break
    return value
#---------------------------------------
# Parse a Term   <term> → <factor>{+<factor> | -<factor>}
#
def term():
    value = factor()
    while True:
        if lookahead() == '*':
            read_token()
            value = binary_op('*', value, factor())
        elif lookahead() == '/':
            read_token()
            value = binary_op('/', value, factor())
        else:
            break
    return value
#---------------------------------------
# Parse a Factor   <factor> → (<exp>) | <number>
#
def factor():
    global err
    value = None

    # Insert code here to handle (<exp>)
    if lookahead() == '(': #Look for opening parenthesis
        read_token()
        value = exp()

        if lookahead() == ')': #Look for closing parenthesis
            read_token()
        else:
            raise ParseError('Missing parentheses')

    elif lookahead() == 'pi':     # pi
        read_token()
        return const_pi()

    elif lookahead() == '-':    # unary minus
        read_token()
        return unary_op('-', factor())

    else:                       # should be a number
        try:
            value = atomic(lookahead())
            read_token()
        except ValueError:      # it was not
            raise ParseError('number expected, found: ' + lookahead())

    #print('factor returning', value)

    return value

#==============================================================
# User Interface Loop
#==============================================================
w = input('\nEnter expression: ')
while w != '':
    #-------------------------------
    # Split string into token list.
    #
    for c in '()+-*/':
        w = w.replace(c, ' '+c+' ')
    w = w.split()
    w.append('$') # EOF marker

    print('\nToken Stream:     ', end = '')
    for t in w: print(t, end = '  ')
    print('\n')

    #-------------------------------
    # Try parsing.
    #
    token_index = 0
    try:
        print('Value:           ', exp()) # call the parser
    except:
        print('parse error')

    #-------------------------------
    # Show where parsing terminated.
    #
    print('read | un-read:   ', end = '')
    for c in w[:token_index]: print(c, end = '')
    print(' | ', end = '')
    for c in w[token_index:]: print(c, end = '')
    print()
    w = input('\n\nEnter expression: ')


