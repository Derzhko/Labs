from sympy import *
x, y = symbols('x y')
epsilon = 0.0001
import numpy as np
import math


def function1(x0, y0):
    return math.sin(2*x0 - y0) -1.2*x0 - 0.4
def function2(x0, y0):
    return 0.8*x0**2 + 1.5*y0**2 - 1
# def function1(x0, y0):
#     return math.sin(x0 - 1) + y0 - 1.3
# def function2(x0, y0):
#     return x0 - math.sin(y0 + 1) - 0.8


# x0 = 0.4
# y0 = -0.75
# k = 0
# diff1_x = diff(sin(2 * x - y) - 1.2 * x - 0.4, x).subs(x, x0).subs(y, y0).evalf()
# diff1_y = diff(sin(2 * x - y) - 1.2 * x - 0.4, y).subs(x, x0).subs(y, y0).evalf()
# diff2_x = diff(0.8 * pow(x, 2) + 1.5 * pow(y, 2) - 1, x).subs(x, x0).subs(y, y0).evalf()
# diff2_y = diff(0.8 * pow(x, 2) + 1.5 * pow(y, 2) - 1, y).subs(x, x0).subs(y, y0).evalf()
# A = np.array([[diff1_x, diff1_y], [diff2_x, diff2_y]], dtype='float')
# B = np.array([(-1) * function1(x0, y0), (-1) * function2(x0, y0)], dtype='float')
# X = np.linalg.inv(A).dot(B)
# print(X)
# print(X[0], X[1])
# delta_x = X[0]
# delta_y = X[1]
# x0 += delta_x
# y0 += delta_y
# print(f'x{k}: {x0} y{k}: {y0}')
# k += 1
# while abs(delta_x) >= epsilon:
#     diff1_x = diff(sin(2 * x - y) -1.2 * x - 0.4, x).subs(x, x0).subs(y, y0).evalf()
#     diff1_y = diff(sin(2 * x - y) -1.2 * x - 0.4, y).subs(x, x0).subs(y, y0).evalf()
#     diff2_x = diff(0.8 * pow(x, 2) + 1.5 * pow(y, 2) - 1, x).subs(x, x0).subs(y, y0).evalf()
#     diff2_y = diff(0.8 * pow(x, 2) + 1.5 * pow(y, 2) - 1, y).subs(x, x0).subs(y, y0).evalf()
#     A = np.array([[diff1_x, diff1_y], [diff2_x, diff2_y]], dtype = 'float')
#     B = np.array([(-1) * function1(x0, y0), (-1) * function2(x0, y0)], dtype = 'float')
#     X = np.linalg.inv(A).dot(B)
#     print(X)
#     print(X[0], X[1])
#     delta_x = X[0]
#     delta_y = X[1]
#     x0 = x0 + delta_x
#     y0 = y0 + delta_y
#     print(f'x{k}: {x0} y{k}: {y0}')
#     k += 1
x0 = 1.79999
y0 = 0.5827
k = 0
diff1_x = diff(sin(x - 1) + y - 1.3, x).subs(x, x0).evalf()
diff1_y = diff(sin(x - 1) + y - 1.3, y).subs(y, y0).evalf()
diff2_x = diff(x - sin(y + 1) - 0.8, x).subs(x, x0).evalf()
diff2_y = diff(x - sin(y + 1) - 0.8, y).subs(y, y0).evalf()
A = np.array([[diff1_x, diff1_y], [diff2_x, diff2_y]], dtype = 'float')
B = np.array([(-1) * function1(x0, y0), (-1) * function2(x0, y0)], dtype = 'float')
X = np.linalg.solve(A, B)
print(X)
print(X[0], X[1])
delta_x = X[0]
delta_y = X[1]
x0 += delta_x
y0 += delta_y
print(f'x{k}: {x0} y{k}: {y0}')
k += 1
while abs(delta_x) >= epsilon:
    diff1_x = diff(sin(x - 1) + y - 1.3, x).subs(x, x0).evalf()
    diff1_y = diff(sin(x - 1) + y - 1.3, y).subs(y, y0).evalf()
    diff2_x = diff(x - sin(y + 1) - 0.8, x).subs(x, x0).evalf()
    diff2_y = diff(x - sin(y + 1) - 0.8, y).subs(y, y0).evalf()
    A = np.array([[diff1_x, diff1_y], [diff2_x, diff2_y]], dtype = 'float')
    B = np.array([(-1) * function1(x0, y0), (-1) * function2(x0, y0)], dtype = 'float')
    X = np.linalg.solve(A, B)
    print(X)
    print(X[0], X[1])
    delta_x = X[0]
    delta_y = X[1]
    x0 += delta_x
    y0 += delta_y
    print(f'x{k}: {x0} y{k}: {y0}')
    k += 1



