# module_4_1.py

# Импортируем функции из модулей, используя оператор 'as' для уникальности имен
from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Вызов функций с различными значениями
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

# Вывод результатов на экран
print(result1)
print(result2)
print(result3)
print(result4)  