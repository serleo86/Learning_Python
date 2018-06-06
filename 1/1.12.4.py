f=str (input())
pi=3.14
if f=='треугольник':
    a = float (input())
    b=float (input())
    c = float (input())
    p=float
    p=(a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif f=='прямоугольник':
    x=float (input())
    y=float (input())
    print (x*y)
elif f=='круг':
    r=float (input())
    print (pi*r**2)
