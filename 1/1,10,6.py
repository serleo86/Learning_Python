a = int (input())#год
if 1900<=a<=3000 and a%4==0 and a%100!=0 or a%400==0:
    print ('Високосный')
elif 1900<=a<=3000 and a%4!=0 or a%100==0:
    print ('Обычный')
