import random
answers = ["вы суровая, сильная личность",
           "вы сильная личность, но иногда можете разжалобиться",
           "вы личность с очень разными интересами",
           "вы сентиментальная личность",
           "ваш расцвет ещё впереди",
           "сейчас вы в полном расцвете сил, но все ещё впереди",
           "вы нежная, сентиментальная личность",
           "впредь остерегайтесь конфликтов они могут огорчить вас",
           "вы экстраординарная личность",
           "у вас направленные интересы"]
seasons = ["Зима", "Весна", "Лето", "Осень"]
answer = random.choice(answers)
print("Отвечайте на вопросы. Пишите ответы с большой буквы.")
print("Какое ваше любимое время года?")
a = input()
if a in seasons:
    print("В какое время года вы родились")
    b = input()
    if b in seasons:
        print(answer)
    else:
        print("Выберите одно: " + ", ".join(map(str, seasons)))
else:
    print("Выберите одно: " + ", ".join(map(str, seasons)))
