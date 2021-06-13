from math import *
from sympy import *

N = 10
epsilon = 0.0001
def function(x):
    return 3 * x - cos(x) - 1

def localisation(a, b, N):
    x0 = a
    x1 = a + (b - a) / N
    while function(x0) * function(x1) >= 0:
        x0 = x1
        x1 += (b - a) / N
        if x1 == b:
            N = 2 * N
            x0 = a
            x1 = a + (b - a) / N
    return {"x0": x0, "x1": x1}

def count_x1(x0):
    return float(x0 - float(function(x0) / (3 + sin(x0))))

def newtons_method(interval):
    a = interval["x0"]
    b = interval["x1"]
    x0 = float(b)
    x1 = count_x1(x0)
    while abs(x1 - x0) >= epsilon:
        x0 = x1
        x1 = count_x1(x0)
    return x1


a = float(1 / 3)
b = float(2 / 3)
print(f'корень уравнения: {newtons_method(localisation(a, b, N))}')
