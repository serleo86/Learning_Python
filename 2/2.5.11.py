s=[]
a=[int(i)  for  i  in  input().split()]
for  i  in  a:
        if  (a.count(i)>1)  and  (str(i)  not in  s):
                s+=[str(i)]
print(" ".join(s))
