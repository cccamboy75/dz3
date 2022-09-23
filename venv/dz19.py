import random

spisok1 = []
spisok2 = []

a = random.randint(0, 30)
b = random.randint(0, 30)
print(a)
print(b)
c = 3
d = 5

for i in  range(a):
    spisok1.append(c)
    c += 3
for i in  range(b):
    spisok2.append(d)
    d += 5


x = set(spisok1)
y = set(spisok2)
z = x.intersection(y)

print(x)
print(y)
print(z)

