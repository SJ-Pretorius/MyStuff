def abc(a):
    a
    b = 'hi'
    return a, b

while True:
    x = input('Choose: ')
    z, y = abc(x)
    print(z)
    print(y)
    continue