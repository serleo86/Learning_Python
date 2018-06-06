#Рабочий код без файла
'''a=input().lower().split()
x=0
b=0
d={}
s=[]
r=[]
z=[]
for i in a:
    y=a.count(i)
    d[i]=y
    s+=[y]
    b=max(s)
for x,y in d.items():
    if y==b:
        r+=[x]
        z=min(r)
print(z,b)'''
x=0
b=0
d={}
e=[]
r=[]
z=[]
f=str()
s1=str()
with open('C:\work\Python_test\dataset_3363_3.txt') as file: #открываем файл
    for i in file: #бежим по всем строкам
        i=i.strip().lower().split()
        for j in i: #определяем количество повторений каждого слова
            y=i.count(j)
            d[j]=y #делаем словарь со словами
            e+=[y] #далем список со количеством повторений
        b=max(e) #определяем максимальное значение
for x,y in d.items(): #идем в словарь
    if y==b: #сраниваем значение с максимальным
        r+=[x] #делаем новый список с максимальными значениями
        z=min(r) #выбираем из него первое
print(z,b)









