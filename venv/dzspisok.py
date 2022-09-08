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
    # y = len(x)  len функция определяет колличество элементов списка
    # если нужно удалить del(название списка[индекс])
    # pop удаляет последний элемент из списка и запоминает его х.pop()
    # x.insert(0, n)  insert добавляет элемент в сиписок x нужный список
    # exntnd расширяет создает список пример:
    myList = ["Lion", "Tiger", "Bear", "Cheetah", "Puma"]
    listToAdd = ["Leopard", "Lynx"]
     myList.extend(listToAdd)
    print(myList)
    ['Lion', 'Tiger', 'Bear', 'Cheetah', 'Puma', 'Leopard', 'Lynx']
    ### добавляем строку в список
    myList = ['X', 'Y', 'Z']
    myList.extend('abcd')
    print(myList)
    # ['X', 'Y', 'Z', 'a', 'b', 'c', 'd']


