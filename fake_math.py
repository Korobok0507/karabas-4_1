# fake_math.py
# Функция деления с запретом делить на 0
def divide(first, second):
    if second == 0:
        return 'Ошибка'
    return first / second