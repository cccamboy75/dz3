spisok1 = [1, 2, 3, 4, 5]
spisok2 = list()
if len(spisok1) % 2 == 0:
    x = len(spisok1) // 2
    spisok2.extend([spisok1[:x], spisok1[x:]])
    print(spisok1, " => ", spisok2)
else:
    y = len(spisok1) // 2
    spisok2.extend([spisok1[:y + 1], spisok1[y + 1:]])
    print(spisok1, " => ", spisok2)
    print(y)



