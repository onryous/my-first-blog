'''number1 = int(input("первое число: "))
number2 = int(input("второе число: "))
number3 = int(input("третье число: "))


if (number1 > number2 or number1 > number2):
    print(number1)
elif (number2 > number3):
    print(number2)
else:
    print(number1)'''

'''passshel = input("Введите пороль: ")
password = 'alik212'

if (passshel == password):
    print("Вы вошли")
else:
    print("Не получилось")'''

'''num = int(input("Введите число: "))

for i in range(1, 10):
    print(f'{num} * {i] = {num * i}')'''


'''num = int(input("Введите число: "))
result = 0
for i in range(1, num+1):
    result += 1'''

wrod = input('введите слово: ')
result = 0
symbol = 'a'
for i in wrod:
    if(symbol == i):
        result += i
print(result)