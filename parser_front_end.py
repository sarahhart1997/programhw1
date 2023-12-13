# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:40:30 2023

@author: rutkowsk
"""

#==============================================================
# FRONT END PARSER
#==============================================================
from backend_modules.numeric import *
class ParseError(Exception):
    def __init__(self, err):
        print(err)

token_index = 0  # keeps track of what character we are currently reading.

def lookahead():
    return w[token_index]

def read_token():
    global token_index
    token_index += 1

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

def factor():
    global err
    value = None

    if lookahead() == '(':  # Look for opening parenthesis
        read_token()
        value = exp()
        if lookahead() == ')':  # Look for closing parenthesis
            read_token()
        else:
            raise ParseError('Missing parentheses')

    elif lookahead().isidentifier():  # variable assignment or function name
        func_name = lookahead()
        read_token()  # Consume the function name
        if lookahead() == '(':
            read_token()
            inner_expr = exp()
            if lookahead() == ')':
                read_token()
                return unary_op(func_name, inner_expr)
            else:
                raise ParseError(f"Expected ')' after the argument of {func_name}, found: {lookahead()}")
        else:
            return atomic(func_name)

    elif lookahead() == 'pi':
        read_token()
        return const_pi()

    elif lookahead() == '-':
        read_token()
        return unary_op('-', factor())

    else:
        try:
            value = atomic(lookahead())
            read_token()
        except ValueError:
            raise ParseError('number expected, found: ' + lookahead())

    return value

def statement():
    var_name = lookahead()
    if var_name.isidentifier():
        read_token()  # Consume the variable name
        if lookahead() == '=':
            read_token()  # Consume the '='
            exp_result = exp()
            assign(var_name, exp_result)
            return f"{var_name} = {exp_result}"
        else:
            raise ParseError(f"Expected '=', found: {lookahead()}")
    else:
        raise ParseError(f"Invalid variable name: {var_name}")

# ... (rest of your code)

# ==============================================================
# User Interface Loop
# ==============================================================
w = input('\nEnter expression: ')
while w != '':
    for c in '()+-*/':
        w = w.replace(c, ' ' + c + ' ')
    w = w.split()
    w.append('$')  # EOF marker

    print('\nToken Stream:     ', end='')
    for t in w:
        print(t, end='  ')
    print('\n')

    token_index = 0
    try:
        print('Value:           ', statement())  # call the parser
    except ParseError as e:
        print('parse error:', e)

    print('read | un-read:   ', end='')
    for c in w[:token_index]:
        print(c, end='')
    print(' | ', end='')
    for c in w[token_index:]:
        print(c, end='')
    print()

    w = input('\n\nEnter expression: ')
    
print()
