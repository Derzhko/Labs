from sympy import *

x, y = symbols('x y')
epsilon = 0.0001
import numpy as np
import math

f1 = sin(x - 1) + y - 1.3
f2 = x - sin(y + 1) - 0.8

def function1(x0, y0):
    return math.sin(x0 - 1) + y0 - 1.3

def function2(x0, y0):
    return x0 - math.sin(y0 + 1) - 0.8


x0 = -1
y0 = 1.5

k = 0
diff1_x = diff(f1, x).subs(x, x0).subs(y, y0).evalf()
diff1_y = diff(f1, y).subs(x, x0).subs(y, y0).evalf()
diff2_x = diff(f2, x).subs(x, x0).subs(y, y0).evalf()
diff2_y = diff(f2, y).subs(x, x0).subs(y, y0).evalf()
A = np.array([[diff1_x, diff1_y], [diff2_x, diff2_y]], dtype='float')
B = np.array([(-1) * function1(x0, y0), (-1) * function2(x0, y0)], dtype='float')
X = np.linalg.solve(A, B)
delta_x = X[0]
delta_y = X[1]
x0 += delta_x
y0 += delta_y
print(f'x{k}: {x0} y{k}: {y0}')
k += 1
while abs(delta_x) >= epsilon:
    diff1_x = diff(f1, x).subs(x, x0).subs(y, y0).evalf()
    diff1_y = diff(f1, y).subs(x, x0).subs(y, y0).evalf()
    diff2_x = diff(f2, x).subs(x, x0).subs(y, y0).evalf()
    diff2_y = diff(f2, y).subs(x, x0).subs(y, y0).evalf()
    A = np.array([[diff1_x, diff1_y], [diff2_x, diff2_y]], dtype='float')
    B = np.array([(-1) * function1(x0, y0), (-1) * function2(x0, y0)], dtype='float')
    X = np.linalg.solve(A, B)
    delta_x = X[0]
    delta_y = X[1]
    x0 = x0 + delta_x
    y0 = y0 + delta_y
    print(f'x{k}: {x0} y{k}: {y0}')
    k += 1
print(f'answer: ({x0}; {y0})')