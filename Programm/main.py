import os # Это для красоты
# ДЗ по истории
# Нужно понимать что в семье живет 3 человека

while True: # Программа закроется только через пользователя

    # Доходы
    zp = int(input("Зарплата: "))
    mother_capital = int(input("Материнский капитал: "))
    pension = int(input("Пенсия: "))

    # Расходы
    eat = int(input("Расходы на еду: ")) # Плата за еду
    comm = int(input("Плата за коммунальные услуги: "))
    other = int(input("Прочие расходы: "))

    income = zp + mother_capital + pension # Все доходы вместе взятые
    expenses = eat + comm + other # Все расохды вместе взятые

    def analize(): # Функция анализа полученых данных
        os.system("cls")
        print("Доходы: " + str(income) + "\nРасходы: " + str(expenses))

    if expenses == income:
        analize()
        print("В семье баланс по расохдам и доходам")

        input("Нажмите Enter чтобы продолжить...")
        os.system("cls")

    elif expenses > income:
        analize()
        print("Расходы больше доходов")

        input("Нажмите Enter чтобы продолжить...")
        os.system("cls")

    elif expenses < income:
        analize()
        print("Доходы больше расходов")

        input("Нажмите Enter чтобы продолжить...")
        os.system("cls")

    else:
        print("Вы неправильно ввели числа")

        input("Нажмите Enter чтобы продолжить...")
        os.system("cls")
