n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

calculate = input('''
For addition, type +
For subtraction, type -
For multiplication, type *
For division, type /
For remainder, type %
''')

if calculate == '+':
    print('{} + {} = '.format(n1, n2))
    print(n1 + n2)

elif calculate == '-':
    print('{} - {} = '.format(n1, n2))
    print(n1 - n2)

elif calculate == '*':
    print('{} * {} = '.format(n1, n2))
    print(n1 * n2)

elif calculate == '/':
    print('{} / {} = '.format(n1, n2))
    print(n1 / n2)

elif calculate == '%':
    print('{} % {} = '.format(n1, n2))
    print(n1 % n2)

else:
    print('You havent typed a number, run the program again')