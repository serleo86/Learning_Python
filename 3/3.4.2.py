''''# рабочий код для ввода с экрана
a=input()
s=str()
for i in range(0,len(a),2):

    s+=str(a[i])*int(a[i+1])
print(s)'''

#Рабочий код для файла с одним числом
'''s=str()
with open('C:\work\Python_test\dataset_3363_2.txt') as file:
    s1=file.readline()
    for i in range(0,len(s1)-1,2):
        s+=str(s1[i])*int(s1[i+1])
with open('C:\work\Python_test\Result.txt','w') as itog:
    itog.write(s)'''



a=input()
s=str()
for i in range(0,len(a),2):

    s+=str(a[i])*int(a[i+1])
print(s)
