# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


arr = []
n = int(input("Введите кол-во чисел в списке "))
for i in range(n):
    arr.append(float(input("Введите число ")))
print(arr) 

i = 0
max = arr[i] - int(arr[i])
min = arr[i] - int(arr[i])

while i < len(arr)-1:
    if arr[i+1]-int(arr[i+1]) > max:
        max = arr[i+1]-int(arr[i+1])
    if arr[i+1]-int(arr[i+1]) < min:
        min = arr[i+1]-int(arr[i+1])
    i += 1

print(round((max-min), 2))           