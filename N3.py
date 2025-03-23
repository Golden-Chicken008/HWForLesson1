age = input("Введите ваш возраст: ")
if not age.isdigit() and age.lstrip('-').isdigit():
    print("Ошибка: возраст не может быть отрицательным")
elif not age.isdigit() and not age.lstrip('-').isdigit():
    print("Ошибка: введено не число")
elif int(age) >= 18:
    print("Вы совершеннолетний")
elif int(age) < 18:
    print("Вы несовершеннолетний")
else:
    print("Ошибка: программист не додумался, как получить это сообщение")