revenue = int(input("Введите выручку"))
costs = int(input("Введите издержки"))

if revenue > costs:
    print("ваша прибыль: " + str(revenue - costs))
    print("Ваша рентабельность: ")
    print("%.d"%(revenue/costs*100)+"%")

    number_of_employees = int(input("введите кол-во сотрудников"))
    print("Прибыль на одного сотрудника составила:")
    print("%d"%((revenue-costs)/number_of_employees)+"%")
else:
    print("ваш убыток: " + str(revenue - costs))
