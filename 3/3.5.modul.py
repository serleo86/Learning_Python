# Способы вызова модуля или функций из модуля
# import my_module
# my_module.foo() - вызов внутри блока

#from my_module import foo
# foo() - вызов внутри блока

#from my_module import * - импортируем все функции модуля
# foo() - вызываем функцию

# from my_module import foo as my_foo - можно переименовать функцию и вызвать ее под своим именем
# my foo()


# модуль subprocess - вызывает внутри программы другую программу
# Пример : suprrocess.call(['python','-h']) - указывается имя программы и аргумент

import subprocess
subprocess.call(['python','-h'])
