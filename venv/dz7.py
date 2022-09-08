#a = [0, 1, 0, 3, 12]
#a = [0]
a = [1, 0, 3, 0, 0, 0, 5]
#a = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for i in range(len(a) - 1, -1, -1):
    if a[i] == 0:
        print(i)
        a.append(a.pop(i))
print(a)