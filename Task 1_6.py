distance_initial = int(input("Введите дистанцию в первый день: "))
distance_aim = int(input("Введите целевую дистанцию"))
day = 1


while distance_initial < distance_aim:
    distance_initial = distance_initial * 1.1
    day = day + 1

print("Результат будет достигнут" + day)
