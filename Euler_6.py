def main():
    a = range(1, 101)
    b = 0
    c = 0
    for i in a:
        b += (i ** 2)
    for n in a:
        c += n
    c = c ** 2
    d = c - b
    return print(d)


main()
