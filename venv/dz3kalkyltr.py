print("Выберете действие")
if True:
    s = input("Введите знак (+,-,*,/): ")
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print (x+y)
        elif s == '-':
            print(x-y)
        elif s == '*':
            print(x*y)
        elif s == '/':
            if y != 0:
                print (x/y)
            else:
                print("Деление на ноль запрещенно!")
    else:
        print("Неверный знак операции!")

