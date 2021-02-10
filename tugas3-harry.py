
'''# jawaban no 1
number = ''
size = 5

for i in range(size):
    for j in range(1+i):
        number += '{} '.format(i+1)
    number += '\n'

print(number)
'''

''' #Jawaban no 2
number = ''
size = 5

for i in range(size):
    for j in range(1+i):
        number += '{} '.format(j+1)
    number += '\n'

print(number)
'''

'''# jawaban no 3
number = ' '
size = 5

for i in range(size, 0, -1):
    number += str(i) + ' '
    print(number)
'''

'''# jawaban no 4
number = ''
size = 5
for i in range(size):
    for j in range(size - i):
        number += str(i + 1) + ' '
    number += '\n'
print(number)
'''

''' # jawaban no 5
number = ''
size = 5

for i in range(size):
    for j in range(size - i):
        number += str(j + 1) + ' '
    number += '\n'
print(number)
'''

''' # jawaban no 6
number = ''
size = 5

for i in range(size):
    for j in range(size - i):
        number += str(size - j) + ' '
    number += '\n'
print(number)
'''

# jawaban no 7
# r = 4
# for x in range(r):
#     print('h'*((r+2)-x*2)+'* '*(2*x+1))
# for x in range(r-1, -1, -1):
#     print('h'*((r+2)-x*2)+'* '*(2*x+1))



# ===== Coret Coret
# print('a'*(6-0-0)+'* '*(2*0+1))
# print('a'*(6-1-1)+'* '*(2*1+1))
# print('a'*(6-2-2)+'* '*(2*2+1))
# print('a'*(6-3-3)+'* '*(2*3+1))
# print('a'*(6-3-3)+'* '*(2*3+1))
# print('a'*(6-2-2)+'* '*(2*2+1))
# print('a'*(6-1-1)+'* '*(2*1+1))
# print('a'*(6-0-0)+'* '*(2*0+1))

# aaaaaa*
# aaaa* * *
# aa* * * * *
# * * * * * *
# * * * * * *
# aa* * * * * 
# aaaa* * *
# aaaaaa*

