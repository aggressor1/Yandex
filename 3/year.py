a = int(input())
if ((a % 4 == 0) and (not a % 100 == 0)) or (a % 400 == 0):
    print("Високосный")
else:
    print("Не високосный")