m = int(input('Введите порядковый номер месяца : '))
while not 1 <= m <= 12:
    print('Нет месяца с порядковым номером ', m)
    m = int(input('Введите порядковый номер месяца : '))
t=list['месяц', 'Февраль', 'Март', 'Апрель', 'Март', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
print('Порядковый номер месяца соответствует времени года: ', t[m])
