def euler2(x):
    a = [1,2]
    b = []

    while a[-1] <= x:
        a.append(a[-1] + a[len(a) -2])
    del a[-1]
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return sum(b)


print(euler2(4000000))