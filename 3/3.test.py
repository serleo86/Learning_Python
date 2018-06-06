'''def my_range(start, stop, step=1):
    res=[]
    if step>0:
        x=start
        while x<stop:
            res+=[x]
            x+=step
    elif step<0:
        x=start
        while x>stop:
            res+=[x]
            x+=step
    return res


#print(my_range(1,9))

print(my_range(step=2, stop=20, start=10))
'''

'''def init():
    a=100
    return a'''

'''def zero(xs):
    xs.append(19457534)
    xs=[100]
a=[8]
zero(a)
print(a)'''

'''def print_value():
    print(b)
    a=100
    print(a)

b=4567
print_value()'''

'''a = [int (i) for i in input().split()]
for i in range (len(a)):
    if a[i]%2==1:
        print('нечетное')
    else:
        print('четное')'''

import os
x=os.path.join('.','dirname','filename.txt')
print(x)


