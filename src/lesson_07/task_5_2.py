# Дано число. Найти сумму и произведение его цифр.

# data inputting
try:
    num = int(input("Enter number, please:"))
except:
    print("Error input data")

str_num = str(num)

# sum
if str_num[0] == "-":
    str_num = str_num[1:]

size = len(str_num)

i = 0
sum_num = 0
while i < size:
    sum_num += int(str_num[i])
    i += 1

print(f"sum = {sum_num}")

# mult
if str_num[0] == "-":
    str_num = str_num[1:]

size = len(str_num)

i = 0
mult_num = 1
while i < size:
    mult_num *= int(str_num[i])
    i += 1

print(f"mult = {mult_num}")
