a = input()
s = 0
ns = 0
for i in a:
    if ord('0') <= ord(i) <= ord('9'):
        s += 1
    elif ord(i) == ord('_'):
        s += 1
    elif ord('a') <= ord(i) <= ord('z'):
        s += 1
    else:
        ns = i
        break
if s == len(a):
    print('OK')
else:
    print('Неверный символ:', ns)
