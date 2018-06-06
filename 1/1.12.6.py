result='программист'
a=int (input())
b=str
if a>=0:
    if a%10==1 and 0<=a<10:
        b=''
    elif a%10==1 and 20<a<100:
        b=''
    elif a%10==2 or a%10==3 and a<10:#and a>20
        b='а'
    elif a%10==2 or a%10==3 and 20<a<100:
        b='а'
    elif a%10==4 and a<10:#and a>20
        b='а'
    elif a%10==4 and 20<a<100:#and a>20
        b='а'
    else:
        b='ов'
    print (a,result + b)


