#a=5
#while a>0:
#    print (a, end=' ')
#    a -=1
'''
a=5
while a <=55:
    print(a)
    a +=2'''
'''a = '*'
n = int (input())
c = 1
while c<=n:
    print (a*c)
    c +=1'''

'''n = int (input())
stars ='*'
while len (stars) <=n:
    print (stars)
    stars +='*'''''
'''s = 0
a = int (input())
b = int (input())
while a<=b:
    s +=a
    a +=1
print (s)'''
'''i=0
while i<5:
    a = int (input())
    b=int (input())
    if (a==0) and (b==0):
        break
    if (a==0) or (b==0):
        continue
    print (a*b)
    i +=1
else:
    print ('выведено 5 чисел')'''
'''i = int ()
for i in range (10):
    print (i*i)'''
'''n = int (input())
for i in  range (n):
    print ('*'*n)'''
'''n = int (input())
for i in range (n):
    for j in range (n):
        print ('*', end='')
    print ()'''


'''a, b = input ().split ()
a = int (a)
b = int (b)
s = 0
for i in range (a, b+1):
    if i%2==1:
        s+=i
print (s)'''


'''a, b = input ().split ()
a = int (a)
b = int (b)
s = 0
if a%2==0:
    a=a+1
for i in range (a, b+1, 2):
    s+=i
print (s)'''

'''a,b = (int(i) for i in input().split())
s = 0
if a%2==0:
    a=a+1
for i in range (a, b+1, 2):
    s+=i
print (s)'''

'''genome = 'ATGG'
i=0
print (genome[i])'''

'''genome = 'ATGG'
for c in genome:
    print (c)
'''

'''spartak = input()
c=0
for i in spartak:
    if i=='C':
        c+=1
print (c)'''

'''spartak = input()
print (spartak.count('C'))'''

''''dna ='ABCDEFJKBBJHBEF'
print(dna[1:-1:2])'''


'''s = input()
i = 0
j = len(s)-1
a = True
while i<j:
    if s[i]!=s[j]:
        a = False
    i+=1
    j-=1
if a:
    print ('YES')
else:
    print ('NO')'''

s=['Sasha','Ivan','Masha']
p=sorted(students)
print(p)



