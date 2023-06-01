# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов
# N = int(input('Введите N: '))

# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n-1) * n
# print(factorial(N))
# def triangle(x):
#     if x == 1:
#         return 1
#     return x + triangle(x - 1)

# print(triangle(N))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
A = int(input('Введите a: '))
B = int(input('Введите b: '))
def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)
print(sum(A,B))