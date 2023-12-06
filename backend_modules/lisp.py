# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:29:33 2023

@author: rutkowsk
"""

#==============================================================
# BACK END PARSER (ACTION RULES)
#==============================================================
import math

def binary_op(op, lhs, rhs):
    return '(' + op + ' ' + lhs + ' ' + rhs + ')'

def unary_op(op, x):
    if op in {'sin', 'cos', 'sqrt', 'tan', '-'}:
        return f'({op.upper()} {x})'
    else:
        return None

def atomic(x):
    return x

def const_pi():
    return 'PI'
