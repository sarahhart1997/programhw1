# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:40:30 2023

@author: rutkowsk
"""

#==============================================================
# BACK END PARSER (ACTION RULES)
#==============================================================

op_code = {'+':'ADD', '-':'SUB', '*':'MUL', '/':'DIV'}

def binary_op(op, lhs, rhs):
    op_name = op_code.get(op, None)
    return op_name + '(' + lhs +  ', ' + rhs + ')'

def unary_op(op, rhs):
    if op == '-': return 'NEG' + '(' + rhs + ')'
    else: return None

def atomic(x):
    return  x

def const_pi():
    return 'PI'