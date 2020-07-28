a = 'rg t r regher ergherh ehth erhe erh'
b = a.split(' ')
c = len(b)
print(b)
i = 0
while i < len(b):
    temp = b[i]
    b[i] = b[c-1]
    b[c-1] = temp
    if i >= (len(b)/2):
        break
    i += 1
    c -= 1
print(b)



