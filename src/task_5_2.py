a = int(input())
e = 0
d = 1
while a > 0:
    b = a % 10
    a = a // 10
    d *= b
    e += b



print(d)
print(e)