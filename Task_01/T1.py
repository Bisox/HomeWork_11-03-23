# Задача 1: Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

num = int(input("Введите трехзначное число: "))
total = 0
for i in range(3):
    last_num = num % 10
    total += last_num
    num //= 10
print(total) 
