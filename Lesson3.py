x = int(input("Введите первое число"))   # пример: x = int("10")
is_operation = input("Введите знак")     # is_operation = "+"
y = int(input("Введите второе число"))   # y = int("5")

if is_operation == "/" and y == 0:
    print("На ноль делить нельзя")
else:
    if is_operation == "-":
        print(x-y)
    elif is_operation == "+":
        print(x+y)
    elif is_operation == "*":
        print(x * y)
    elif is_operation == "/":
        print(x / y)

