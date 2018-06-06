'''n = int (input())
s=[]
for i in range (n):
    s+=i*[i]
print(s[0:n])
'''

n = int (input())
s=[]
for i in range (n+1):
    for j in range(i):
        if (len(s)<n):
            s+=[str(i)]
print(" ".join(s))
