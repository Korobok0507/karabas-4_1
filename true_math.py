# true_math.py

from math import inf
# Функция деления с вызовом бесконечности
def divide(first, second):
    if second == 0:
        return inf
    return first / second