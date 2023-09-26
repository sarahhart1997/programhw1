# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:42:11 2023

@author: rutkowsk
"""

#==============================================================
# BACK END PARSER (ACTION RULES)
#==============================================================

def binary_op(op, lhs, rhs):
    return lhs + ' ' + rhs + ' ' + op

def atomic(x): # should test for valid number or identifier
    return x

def const_pi():
    return 'PI'

def unary_neg(x):
    return '~'