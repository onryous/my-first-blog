num = int(input("Введи количество чисел списка: "))
sp = []
for i in range(1,num+1):
     numbers = int(input(f'введите число: '))
     sp.append(numbers)
print("my massiv:", sp)
print(max(sp))
print(min(sp))