a = [int (i) for i in input().split()]
x = int(input())
s=[]
for i in range (len(a)):
    if a[i]==x:
        s+=[str(i)]
if len(s)>0:
    print(" ".join(s))
else:
    print('Отсутствует')








