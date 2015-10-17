from soduku import *

path = '/home/arnold-hu/garage/soduku/test_soduku.txt'

soduku = init_soduku(path)

if type(soduku) == str:
    print soduku
else:
    print_soduku(soduku)



soduku= simple_process(soduku)
print '################################'
if type(soduku) == str:
    print soduku
else:
    print_soduku(soduku)

display(soduku)
