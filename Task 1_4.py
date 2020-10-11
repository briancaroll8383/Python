number = int(input("Введите число"))
biggest_digit = number % 10

if number > 0:

    while number // 10 > 0:
        if number % 10 > biggest_digit:
            biggest_digit = number % 10
        number = number // 10

    print(biggest_digit)
else:
    print("Вы ввели отрицательное число")
