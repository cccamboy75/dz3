word = 'yes'
while word == 'yes' or word == 'y':
        x = float(input('Введите число '))
        s = input('Выберите действие + , - , * , / ')
        y = float(input('Введите число '))
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

        word = input("введите слово yes или y чтобы продолжить")

