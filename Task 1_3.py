number=int(input("Введите число от 0 до 9"))

if 0 <= number < 10:
    result=number*100+number*10+number
    print(result)
else:
    print("Вы ввели не то число")