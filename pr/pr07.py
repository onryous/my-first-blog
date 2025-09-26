'''text = input("пробелы:")
count_spaces = text.count(" ")

print(f"Количество пробелов: {count_spaces}")'''

'''word = input("Ведите слово: ")

for i in range(len(word), 0, -1):
    print(word[:i])

for i in range(2,len(word) + 1):
    print(word[:i])'''

'''text = input("подчеркеванье:")
count_spaces = text.count("_")

print(f"Количество пробелов: {count_spaces}")'''

numbers = list(map(int,input('Введите числы: ').split()))

min_num = min(numbers)
max_num = max(numbers)

print('Список:', numbers)
print('Минимум:',min_num)
print('Максимум:', max_num)