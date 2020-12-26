rev = int(input("Введите сумму выручки: "))
cost = int(input("Введите сумму издержек: "))
finres = rev - cost
if finres > 0:
    print("Прибыль: ", finres)
    profit = finres / rev * 100
    print(f"Рентабельность составляет: {profit:.2f} %")
    employees = int(input("Введите численность сотрудников фирмы: "))
    n = finres / employees
    print(f"Прибыль в расчете на одного сотрудника:  {n:.2f}")
else:
    print("Убыток")
