# n = int(input())
# m = int(input())
# for i in range(2,n):
#     if n % i == 0:
#         print(f'{n} : {i}')
#     i += 1
#
# for j in range(2,m):
#     if m % j == 0:
#         print(f'{m} : {j}')
#     j += 1

n = int(input())
m = int(input())
a = []
for chi in range(n , m + 1):
    b = []
    for i in range(2, chi):
        if chi % i == 0:
            b.append(i)



        i += 1


    chi += 1
    a.append(b)
    a.append(chi)
print(f' :{a}')
