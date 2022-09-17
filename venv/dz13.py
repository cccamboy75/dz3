from string import ascii_letters

a, c, b = input(( "введите две буквы через дефис -"))

print(ascii_letters[ascii_letters.index(a):ascii_letters.index(b) + 1])

