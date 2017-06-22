#!/usr/bin/python
print('Content-type: text/html\r\n\r')

for x in range(1, 101):
    if x % 15 == 0:
        print('CracklePop')
    elif x % 3 == 0:
        print('Crackle')
    elif x % 5 == 0:
        print('Pop')
    else:
        print(x)

print('Thank you and good bye!')
