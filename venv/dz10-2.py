import keyword
import string

w = ('_') #=> True
#w = ('x') #=> True
#w = ('get_value') #=> True
#w = ('Get_value') #=> False
#w = ('get_Value') #=> False
#w = ('getValue') #=> False
#w = ('3m') #=> False

#w = input('введите имя')
a = len(w)
y = True
if w.count('_') > 1:
    y = False
if w.isdigit():
    y = False
if w[0] in string.digits:
    y = False
if w in keyword.kwlist:
    y = False

for i in range(a):
    if w[i] in string.ascii_uppercase:
        y = False
    elif w[i] in string.punctuation and '_' not in w[i]:
        y = False
print(y)