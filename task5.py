# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input("Введите N => "))

a0 = 1
a1 = -1

arr = [a0, a1]

for i in range(n-2):
    a = a0 - a1
    temp = a1
    a1 = a
    a0 = temp
    arr.append(a)
arr.reverse()


a0 = 0
a1 = 1
arr.append(a0)
arr.append(a1)
for i in range(n-1):
    a = a0 + a1
    temp = a1
    a1 = a
    a0 = temp
    arr.append(a)
print(arr)
