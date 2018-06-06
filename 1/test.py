result="программист"
n =int(input())
if (n%100 in range(11,15)):
    result = str(n)+" "+result+"ов"
elif (n%10==1):
    result = str(n)+" "+result
elif (n%10 in range(2,5)):
    result = str(n)+" "+result+"а"
else:
    result = str(n)+" "+result+"ов"
print(result)
