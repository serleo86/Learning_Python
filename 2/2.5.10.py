'''a = [int(i) for i in input().split()]
#a=[1,3,5]
s=0

for i in range(len(a)):
    if i==0:
        s+=a[len(s)]+a[i]]
    elif i==len(a)-1:
        s+=a[i]+a[0]
    else:
        s+=a[i-1]+a[i+1]
print(" ".join(s))
#print (s)'''

s=[]
a=[int(i) for i in input().split()]
x=len(a)
if x==1:
    print (a[0])
if x>1:
    for i in range(x):
        if i==0:
            s+=[str(a[x-1]+a[i+1])]
        elif i==x-1:
            s+=[str(a[i-1]+a[0])]
        else:
            s+=[str(a[i-1]+a[i+1])]
    print(" ".join(s))


'''a = [int(i) for i in input().split()]
#a=[1,3,5]
x=0
y=0
z=0
s=0
for i in a:
    if len(a)==1:
        s=i
    if len(a)==2:
        break
    if len(a)>=3:
        if i==0:
            s=a[1] + a[-1]
        if 1<=i<2:
                    #(len(a)-1):
            s=(a[i-1] + a[i+1])
        if i==(len(a)-1):
            s+=a[0] + a[-2]
    print (s,end=' ')


#print (s)
'''
