def generate_cube_numbers(number):
    for i in range(2, number):
        i = i ** 3
        if i < number:
            yield i
        else:
            return

print(list(generate_cube_numbers(int(100))))

