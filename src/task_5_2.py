"""Дано число. Найти сумму и произведение его цифр."""

intenger = str(int(input("Enter intenger:")))  # ввести произвольнео число с клавиатуры
"""int - для предотвращения ввода букв с клавиатуры"""

total = 0
multi = 1

for i in intenger:
    total += int(i)
    multi *= int(i)

print(f"сумма цифр:{total}")
print(f"произведение цифр:{multi}")
