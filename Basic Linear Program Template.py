# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:06:07 2019

@author: KENZO
"""

#f = -1x[0] + 4x[1]
#s.t:
#-3x[0] + 1x[1] <= 6
#1x[0] + 2x[1] <= 4
#          x[1] >= -3
#  -inf <= x[0] <= inf

from scipy.optimize import linprog

# c = coefficient for objective function
# A = coefficient for constraint
# b = RHS value for constraint

# Parameters
c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]

# Variables Constraint
x0_bounds = (None, None)
x1_bounds = (-3, None)

# Linear Programming
# ub = upper bound
# eq = equality
res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds), options={"disp": True})

# Results
print(res)

# Interpreting output
# x0 = 10, x1 = -3