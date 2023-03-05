# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# um = a
# def step(a,b, um):
#     if b > 1:
#         return step(a * um , b-1, um)
#     else:
#         return a
    
# print(step(a,b, um))

# a = int(input("Enter number: "))
# b = int(input("Enter number: "))

# def step(a,b):
#     if b > 1:
#         return a * step(a, b-1)
#     else:
#         return a
    
# print(step(a,b))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

# a = int(input("Enter number: "))
# b = int(input("Enter number: "))

# def summ(a, b):
#     if b > 0:
#         return summ(a + 1, b - 1)
#     else:
#         return a
# print(summ(a, b))
