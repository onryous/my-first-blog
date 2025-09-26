'''num = int(input('Введите количество элементов списков: '))
sp = []
'''
'''while True:
    num = int(input("Введите число: "))
    if num ==0:
        break
    sp.append(num)'''

'''for j in range(1,num+1):
    num = int(input('введите число:'))
    sp.append(num)
print('mass: ', sp)
'''
'''rs = 0
for j in range(len(sp)):
    rs += sp[j]
print(f'сумма списка: {rs}' )'''

'''num = input('введите число: ')

numbers = [int(i) for i in num]

result = sum(numbers)

print('цифры: ', numbers)
print('Ответ: ',  result)'''

num = int(input('введите числа'))

digits = list(str(num))
digits = [int(d) for d in digits]

razryady = ['тысяч','сотен','десятков','единиц']

for i,d in enumerate(reversed(digits)):
  if d >0:
    if i ==0:
       print(f'{d} единиц' )
    elif i ==1:
       print(f'{d} десятков' )
    elif i == 2:
       print(f'{d} сотен' )
    elif i == 3:
       print(f'{d} тысяч' )