x = input("Введите 4-ох значное число: ")
x = int(x)

n1 = x % 10
x = x // 10
n2 = x % 10
x = x // 10
n3 = x % 10
x = x // 10
n4 = x % 10
x = x // 10

print(n4)
print(n3)
print(n2)
print(n1)
