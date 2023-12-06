# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:40:30 2023

@author: rutkowsk
"""

#==============================================================
# BACK END PARSER (ACTION RULES)
#==============================================================
import math

op_code = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}

def binary_op(op, lhs, rhs):
    op_name = op_code.get(op, None)
    return op_name + '(' + lhs + ', ' + rhs + ')'

def unary_op(op, rhs):
    if op == '-':
        return 'NEG' + '(' + rhs + ')'
    elif op == 'sin':
        return 'SIN' + '(' + rhs + ')'
    elif op == 'cos':
        return 'COS' + '(' + rhs + ')'
    elif op == 'sqrt':
        return 'SQRT' + '(' + rhs + ')'
    elif op == 'tan':
        return 'TAN' + '(' + rhs + ')'
    else:
        return None

def atomic(x):
    try:
        return str(float(x))
    except ValueError:
        return x

def const_pi():
    return 'PI'
