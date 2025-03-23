from itertools import count

while True:
    number = input("Введите число: → ")
    if number == "exit":
        print("Выход из программы...")
        break
    elif not number.isdigit() and not number.lstrip('-').isdigit():
        print("Ошибка: данные не являются числом.")
    elif number.isdigit():
        count = len(number)
        print(f"В этом числе {count} цифры.")
    elif not number.isdigit() and number.lstrip('-').isdigit():
        count = len(number.lstrip('-'))
        print(f"В этом числе {count} цифры.")
    else:
        print("Ошибка: программист не додумался, как получить это сообщение")