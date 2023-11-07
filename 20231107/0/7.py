while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Вы ввели не целое число. Попробуйте снова.")

print("Вы ввели целое число:", number)
