def add_one(x):
    y = (int(''.join(map(str,x))))+1
    z = [int(a) for a in str(y)]
    print(z)

#add_one([1, 2, 3, 4]) #возвращает [1, 2, 3, 5]
#add_one([9, 9, 9, 9]) #возвращает [1, 0, 0, 0, 0]
add_one([0]) #возвращает [1]
#add_one([9]) #возвращает [1, 0]