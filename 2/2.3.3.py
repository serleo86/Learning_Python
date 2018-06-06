a = int (input())
b = int (input())
c = int (input())
d = int (input())
s=""
for i in range (c, d+1):
    s+="\t" +str(i)
print(s)
for i in range (a,b+1):
    print (i, end='\t')
    for j in range (c,d+1):
        print (i*j, end='\t')
    print ()
