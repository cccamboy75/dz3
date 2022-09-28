def find_unique_value():
    s = []
    for i in numbers:
       if numbers.count(i) == 1:
          s.append(i)
          s = s.pop()
    return (s)

numbers = [5, 5, 5, 0.5]
print(find_unique_value())
