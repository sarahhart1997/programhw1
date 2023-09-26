# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:29:33 2023

@author: rutkowsk
"""

#==============================================================
# BACK END PARSER (ACTION RULES)
#==============================================================

def binary_op(op, lhs, rhs):
    return '(' + op + ' ' + lhs + ' ' + rhs + ')'

def atomic(x):
    return x

def const_pi():
    return 'PI'

def unary_op(op, x):
    return '(NEG ' + x + ')'