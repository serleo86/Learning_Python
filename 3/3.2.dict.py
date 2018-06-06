dict,{}
d={'a':239, 10:100,'t':10,'G':18}
#print(d[10])
#print('b' in d) # Проверить, есть ли значение в словаре
#print('a' in d) # Проверить, есть ли значение в словаре
#d['c']=666 # Добавить значение в словарь
#print(d['d']) # ЕСли нет значения, то ошибка
#print(d.get('c')) # ЕСли нет значения, то none
#print(d)
#del d['b'] #удалить значение

#for key in d:
#    print(key, end=' ')
#for i in d.values():
#    print(i, end=' ')
#for i in d:
#   print(i, end=' ')
for a,b in d.items():
    if a=='t':
        print(a,b,end='; ')
