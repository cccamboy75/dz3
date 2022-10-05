def prime_generator(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for y in range(1, 10):
    if prime_generator(y):
        print(y, end=' ')

