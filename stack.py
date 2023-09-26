# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:41:29 2023

@author: rutkowsk
"""

#==============================================================
# BACK END PARSER (ACTION RULES)
#==============================================================
import math
op_code = {'+':'ADD', '-':'SUB', '*':'MUL', '/':'DIV'}

def binary_op(op, lhs, rhs):
    op_name = op_code.get(op, None)
    if op_name:
        return lhs + rhs + '\n' + op_name
    else:
        return None

def unary_op(op, rhs):
    if op == '-': return rhs + '\nNEG'
    else: return None

def atomic(x):
    return '\n' + 'PUSH ' + x

def const_pi():
    return '\nPUSH PI'