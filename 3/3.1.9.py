#рабочий код
'''l=[int(i) for i in input().split()]
s=[]
b=[]
x=[]
for i in range(len(l)):
    if l[i]%2==0:
        s+=str(l[i])
for j in range(len(s)):
    x=int(s[j])//2
    b+=[(x)]
l=b
print(l)'''

#рабочий код 2
'''l = [10, 5, 8, 3]
s=[]
b=[]
x=[]
for i in l:
    if int(i)%2==0:
         s+=[i]
for j in range(len(s)):
    x=int(s[j])//2
    b+=[(x)]
l=b
print(l)'''

def modify_list(l):
    s=[]
    b=[]
    for i in l:
        if int(i)%2==0:
            s+=[i]
    for j in range(len(s)):
        x=int(s[j])//2
        b+=[(x)]
    l.clear()
    l+=b
    #print(l)

lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)






