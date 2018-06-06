a = int (input())
b = int(input())
#a,b = (int (i) for i in input ().split())
s=0
x=0
for i in range (a,b+1):
    if i%3==0:
        s+=i
        x+=1

print (s/x)
