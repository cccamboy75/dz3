import keyword
import string

x = input('введите имя')
a = len(x)
y = True
if x.count('_') > 1:
    y = False
if x.isdigit():
    y = False
if x[0] in string.digits:
    y = False
if x in keyword.kwlist:
    y = False

for i in range(a):
    if x[i] in string.ascii_uppercase:
        okvar = False
    elif x[i] in string.punctuation and '_' not in x[i]:
        y = False
print(y)