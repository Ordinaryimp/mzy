#倒三角
for i in range(1,6):
    for j in range(1,7-i):
        print('*', end='')
    print()

print('--------------')

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()

