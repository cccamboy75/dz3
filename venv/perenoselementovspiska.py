x = [12, 3, 4, 10]
y = len(x)
if y == 4:
    n = x.pop()
    x.insert(0, 10)
    print(x)
if y == 1:
    n = x.pop()
    x.insert(0, 1)
    print(x)
if y == 0:
    print(x)







