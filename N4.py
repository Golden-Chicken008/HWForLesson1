while True:
    number = input("Введите число: → ")
    if number == "exit":
        print("Выход из программы...")
        break
    elif not number.isdigit() and not number.lstrip('-').isdigit():
        print("Ошибка: данные не являются целым числом.")
    elif number.isdigit():
        number_of_digits = len(number)
        print(f"В этом числе {number_of_digits} цифры.")
    elif not number.isdigit() and number.lstrip('-').isdigit():
        number_of_digits = len(number.lstrip('-'))
        print(f"В этом числе {number_of_digits} цифры.")
    else:
        print("Ошибка: программист не додумался, как получить это сообщение")