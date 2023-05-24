

num = int(input('введите трехзначное число:' ))
sum = 0

while num > 0:    
    digit = num % 10
    sum += digit
    num //= 10

print('сумма цифр числа:' , sum)  