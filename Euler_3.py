def dziel(x, y=2):
    while x > y:
        if x % y == 0:
            x = x / y
        else:
            y += 1
    return x

print(dziel(600851475143))