strr = input('Введите строку:\n')
s = int(len(strr) / 2)
print('Средняя буква равна:\n', strr[s])
if strr[0] == strr[s]:
    print('Первый символ равен среднему! Поэтому:\n', strr[1:-1])
