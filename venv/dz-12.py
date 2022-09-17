#a = 'Python Community' #-> #PythonCommunity

#a = 'i like python community!' #-> #ILikePythonCommunity

a = 'Should, I. subscribe? Yes!' #-> #ShouldISubscribeYes

import string
string.punctuation

for p in string.punctuation:
    a = a.replace(p, '')    #замена символа в строке

b = a.split()                   # разбиваем строку на подстроки
c = ''.join(b)                   # объединяем строку
x = '#'
f = c[:139]

print(x + f)

