def palin():
    x = []
    for b in range(100, 1000):
        for a in range(100,1000):
            c = a * b
            if str(c) == str(c)[::-1]:
                x.append(c)
    return max(x)

print(palin())