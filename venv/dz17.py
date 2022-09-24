def correct(str):
    str = str.strip(".")                #удаляем элемент
    x = f"{str[0].upper()}{str[1:]}."
    return x

s = input("Введите строку:")
print(correct(s))