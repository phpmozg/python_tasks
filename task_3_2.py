people = int(input('Сколько человек будет на свадьбе?\n'))
if people > 50:
    print('Берем ресторан!')
elif people >= 20 and people <= 50:
    print('Берем кафе!')
else:
    print('Можно и дома отпраздновать...')
