n = int(input("Введите целое положительное число: "))
s = str(n)
i = 0
x = 0
while i < len(s):
    m = n % 10
    if m > x:
        x = m
    n = n // 10
    i += 1
print (x)


