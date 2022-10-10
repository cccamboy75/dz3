def p_generator(y):
    for i in range(2, y):
        if y % i == 0:
            break
        else:
            return True


def prime_generator(x):
    for i in range(1, x):
        if p_generator(i):
            yield i

print(list(prime_generator(10)))

