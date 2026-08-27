def fibnaccy(iterations):
    a = 1
    b = 1
    print(a)
    print(b)
    for _ in range(iterations):
        c = a + b
        a = b
        b = c
        print(c)


fibnaccy(10)
