# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:25:20 2023

@author: rutkowsk
"""

#==============================================================
# BACK END PARSER (ACTION RULES)
#==============================================================
import math

symbol_table = {}

def binary_op(op, lhs, rhs):
    if op == '+':
        return lhs + rhs
    elif op == '-':
        return lhs - rhs
    elif op == '*':
        return lhs * rhs
    elif op == '/':
        return lhs / rhs
    else:
        return None

def atomic(x):
    if x.isidentifier():
        if x in symbol_table:
            return symbol_table[x]
        else:
            raise ParseError(f"Undefined variable: {x}")
    try:
        return float(x)
    except ValueError:
        raise ParseError('Invalid atomic value: ' + x)

def const_pi():
    return math.pi

def unary_op(op, x):
    if op == '-':
        return -x
    elif op == 'sin':
        return math.sin(x)
    elif op == 'cos':
        return math.cos(x)
    elif op == 'tan':
        return math.tan(x)
    elif op == 'sqrt':
        return math.sqrt(x)
    else:
        return None

def assign(var, value):
    symbol_table[var] = value