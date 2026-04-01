# Task 5.2

while True:
    a = float(input("Введите первое число: "))
    op = input("Введите операцию (+,-,*,/):")
    b = float(input("Введите другое число"))

    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b !=0:
            print("Результат:", a / b)
        else:
            print("Ошибка: деление на ноль!")
    else:
        print("Неизвестная операция")

    cont = input("Продолжить? (y/n): "). lower()

    if cont != "y":
        print("Калькулятор завершил работу.")
        break
