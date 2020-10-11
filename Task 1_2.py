time_in_second = int(input("Введите время в секундах"))

if time_in_second > 0:
    hour = time_in_second // 3600
    minute = (time_in_second - hour * 3600) // 60
    second = time_in_second - hour * 3600 - minute * 60

    print(f"{hour:02}:{minute:02}:{second:02}")




else:
    print("Введите время больше 0")
