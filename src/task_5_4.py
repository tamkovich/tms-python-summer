n = int(input("Enter a natural number:"))
if n == 0:
    print("Error")  # исключаем деление на ноль

summ = 0
for i in range(1, abs(n) + 1):
    k = 1 / i
    summ += k

print(summ)
