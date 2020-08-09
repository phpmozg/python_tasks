print('################\nВариант с for\n################')
a = [1, 2, 3, 4, 5, 6]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print('Список a = {}\nСписок b ={}'.format(a, b))
print('Длина строки b:', len(b))
print('################\nВариант с while\n################')
c = [1, 2, 3, 4, 5, 6]
d = []
i = 0
while i < int(len(c)):
    f = c[i]
    if f % 2 == 0:
        d.append(f)
    i += 1
print('Список c = {}\nСписок d ={}'.format(c, d))
print('Длина строки d:', len(d))
