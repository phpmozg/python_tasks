run = True
print('Меню:\n')
print('0. Выход...\n1. Дюймы в сантиметры\n2. Сантиметры в дюймы\n3. Мили в километры\n4. Километры в мили')
print('5. Фунты в килограммы\n6. Килограммы в фунты\n7. Унции в граммы\n8. Граммы в унции')
print('9. Галлон в литры\n10. Литры в галлоны\n11. Пинты в литры\n12. Литры в пинты\n')


def convert(men, num):
    if men == 1:
        return num * 2.54
    elif men == 2:
        return num * 0.39
    elif men == 3:
        return num * 1.61
    elif men == 4:
        return num * 0.62
    elif men == 5:
        return num * 0.45
    elif men == 6:
        return num * 2.2
    elif men == 7:
        return num * 28.35
    elif men == 8:
        return num * 0.035
    elif men == 9:
        return num * 4.55
    elif men == 10:
        return num * 0.22
    elif men == 11:
        return num * 0.57
    elif men == 12:
        return num * 1.76


while run:
    men = int(input('Введите от 0 до 12:'))
    if men in [i for i in range(13)]:
        if men == 0:
            print('Выход...')
            run = False
        else:
            num = int(input('Введите значение: '))
            print(convert(men, num))
