a = int (input())#сколько надо спать в сутки
b = int (input())#не более этого спать
h = int (input())#сколько спит
if a<=h<=b:
    print ('Это нормально')
elif h<a<=b:
    print('Недосып')
elif a<=b<h:
    print('Пересып')
else:
    print('Неверные значения')

