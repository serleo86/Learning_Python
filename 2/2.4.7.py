s = input()
result=''
x=1
if len(s)==1:
    result=s+str(1)
if len(s)>1:
    for i in range (0,len(s)):
        if i==len(s)-2:
            if s[i]==s[i+1]:
                x+=1
                result+=s[i]+str(x)
            else:
                result+=s[i]+str(x)
                result+=s[i+1]+str(1)
            break
        else:
            if s[i]==s[i+1]:
                x+=1
            else:
                result+=s[i]+str(x)
                x=1

print(result)
