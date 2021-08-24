# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import random
from functools import reduce


number_list = [random.randint(100, 1001) for i in range(10)]
new_list = [i for i in number_list if i%2 == 0]
print(number_list)
print(new_list)
multi = lambda x, y: x * y
reduce(multi, new_list)
a = 1
for i in new_list:
   a = (a * i)
   print(a)



# def my_funk(i, new_list ):
#     return  i + new_list
# print(list(reduce(my_funk, new_list[1], i)))







#print(sum(new_list))
















