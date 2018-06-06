#s=['Sasha','Masha','Ivan']

'''for i in s:
    print ("Hello, " + i + "!")'''
'''print (s[1])'''
'''print(len(s))'''
#t=['Oleg','Alex']
'''print (s+t)'''
'''print(s*3)'''
'''s[1]='Oleg'
print (s)'''
#s.append('Olga')
#s+=['Olga']
#s+=['Boris','Sergei']
#s.insert(1,'Olga')
#s.remove('Sasha')
#del s [1]

#if 'Ivan' in s:
#if 'Ann' not in s:
'''ind=s.index('Sasha')
print(ind)'''
#os=sorted(s)
#s.sort()
#s.reverse()
#print (s)

'''a=[1,'A',2]
b=a
print(b)'''
#a=[0]*5
#a=[0 for i in range (5)]
#a=[i * i for i in range (5)]
'''a=[int (i) for i in input().split()]

print (a)'''


'''a=[[1,2,3],[4,5,6],[7,8,9]]
print (a[0][2])'''

'''
n=3
a=[[0]*n]*n
a[0][0]=5
print(a)'''

n=int(input())
#a=[[0]*n for i in range(n)]
a=[[0 for j in range(n)] for i in range (n)]
a[0][0]=7
print(a)
