a=int(input("enter the coefficient of a:"))
b=int(input("enter the coefficient of b:"))
c=int(input("enter the coefficient of c:"))
if a == 0:
    print(round(-c / b, 2))
else:
    d = b * b - 4 * a * c
    if d < 0:
        print('no roots')
    elif d == 0:
        print(round(-b / 2 / a, 2))
    else:
        print(round((-b - d ** 0.5) / 2 / a, 2))
        print(round((-b + d ** 0.5) / 2 / a, 2))