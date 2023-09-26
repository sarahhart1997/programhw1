# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:25:20 2023

@author: rutkowsk
"""

#==============================================================
# BACK END PARSER (ACTION RULES)
#==============================================================
import math
def binary_op(op, lhs, rhs):
    if op == '+': return lhs + rhs
    elif op == '-': return lhs - rhs
    elif op == '*': return lhs * rhs
    elif op == '/': return lhs / rhs
    else: return None

def atomic(x):
    return float(x)

def const_pi():
    return math.pi

def unary_op(op, rhs):
    return -rhs
