def check(b):
    for i in range(11, 21):
        if b % i != 0:
            return False
    return True

b = 100
while True:
    if check(b):
        break
    else:
        b = b + 1
print(b)
