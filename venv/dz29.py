def generate_cube_numbers(number):
    i = 2
    while i ** 3 <= number:
        print(i ** 3, end= " ")
        i += 1
generate_cube_numbers(100)

