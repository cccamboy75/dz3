def second_index(x,y):

   return x.find(y, x.find(y) + 1) if x.count(y) > 1 else None

print(second_index("sims", "s"))

print(second_index("find the river","e"))

print(second_index("hi","h"))