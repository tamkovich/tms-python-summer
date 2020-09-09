
while True:

    x = int(input())
    y = int(input())
    b = input()
    if y == 0:
        break
    if b == '*' or '/' or '+' or '-':
        if b == '*':
            z = x * y
            print(z)
        elif b == '/':

            z = x/y
            print(z)
        elif b == '+':
            z = x + y
            print(z)
        else:
            z = x - y
        print(z)
else:
    print()

