def difference(*number):
    if len(number) == 0:
        print("0")
    else:
        print(round(max(number)-min(number),2))
difference(5, -5)