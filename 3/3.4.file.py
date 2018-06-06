inf = open ('file.txt', 'r') #если без r. то на чтение. r - указывает тоже на чтение
s1=inf.readline() # чтение первой строки из файла
s2=inf.readline() # чтение второй строки из файла
inf.close() #закрываем файл, когда не требуется работы с ним

# открыть и закрыть файл автоматом для чтения
with open ('text.txt') as inf:
    s1=inf.readline()
    s2=inf.readline()

# функции
s=inf.readline().strip() # strip() - убрать все служебные символы строки
#Пример: '\t abc   \n'.strip() = 'abc'

os.path.join('.', 'dirname', 'filename.txt') #указать путь к файлу

# Построчное чтение файла
with open('file.txt') as inf:
    for i in inf:
        i=i.strip()
        print(i)


ouf = open ('file.txt', 'w') #если без r. то на чтение. w - указывает на запись в файл
ouf.write('Some text\n') # \n надо указат конкретно для перевода курсора в следующую строку
ouf.write(str(25)) # нужно явно указать, что значение должно быть строкой
ouf.close() # закрыть файл

# открыть и закрыть файл автоматом для записи
with open ('text.txt') as ouf:
    ouf.write('Some text\n')
    ouf.write(str(25))

