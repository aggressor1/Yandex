# Ввести количество терпения учителя
a = int(input())
# количество правильных и неправильных попыток
s = 0
sn = 0
# оставшееся терпение учителя
# проверка раз два три
# проверка правильно неправильно
for i in range(a):
    while 1:
        a1 = input()
        if a1 == 'раз':
            s += 1
        else:
            print('Правильных отсчётов было ' + str(s) + ', но теперь вы ошиблись.')
            s = 0
            break
        a2 = input()
        if a2 == 'два':
            s += 1
        else:
            print('Правильных отсчётов было ' + str(s) + ', но теперь вы ошиблись.')
            s = 0
            break
        a3 = input()
        if a3 == 'три':
            s += 1
        else:
            print('Правильных отсчётов было ' + str(s) + ', но теперь вы ошиблись.')
            s = 0
            break
        a4 = input()
        if a4 == 'четыре':
            s += 1
        else:
            print('Правильных отсчётов было ' + str(s) + ', но теперь вы ошиблись.')
            s = 0
            break
print('На сегодня хватит.')