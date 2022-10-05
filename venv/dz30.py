def is_even(number: int):
    number = str(number)
    if number[-1] == "0" or number[-1] == "2" or number[-1] == "4" or number[-1] == "6" or number[-1] == "8":
        return True
    else:
        return False
print(is_even(2494563894038**2))
print(is_even(1056897**2))
print(is_even(24945638940387**3))


