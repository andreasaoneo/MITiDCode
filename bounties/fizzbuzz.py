def fizzbuzz(n):
    for i in range(1, 102):
        if (i-1) % 3 == 0:
            n += "fizz"
        if (i-1) % 5 == 0:
            n += "buzz"
        else:
            n += (str(i))
    return n
print(fizzbuzz(""))


def fizzbuzz2():
    for i in range(1, 101):
        if i % 15 == 0:
            print(i, "fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print(i, "buzz")
        else:
            print(i)
fizzbuzz2()