x = [10, 12, 3, 4, ]
y = len(x)
if y >= 1:
    n = x.pop()
    x.insert(0, n)
    print(x)
if y == 0:
    print(x)