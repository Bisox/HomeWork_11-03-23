# Задача 3:  
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

num = int(input('Введите шестизначное число: '))
a = str(num)
total1 = int(a[0]) + int(a[1]) + int(a[2])
total2 = int(a[3]) + int(a[4]) + int(a[5])

if total1 == total2:
    print('YES')
else:
    print('NO')