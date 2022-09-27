import string
string.punctuation
def isPalindrome(x):
    w =  x.lower()
    b = w
    for i in range(len(x)):
        if x[i] in string.punctuation or x[i] in " ":
            b = b.replace(x[i], "")
    if b[::-1].startswith(b):
        return True
    else:
        return False
print(isPalindrome(input("Введите строку:")))
