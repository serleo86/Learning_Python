# работающий код на цикл
'''d={2:[-1]}
key=int(input())
value=int(input())
if key in d:
    d[key]+=[value]
elif 2*key in d:
    d[2*key]+=[value]
else:
    d[2*key]=[value]
print(d)'''

def update_dictionary(d,key,value):
    if key in d:
        d[key]+=[value]
    elif 2*key in d:
        d[2*key]+=[value]
    else:
        d[2*key]=[value]


