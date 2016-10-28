from sys import stdin

print('Enter a number: ', end='', flush=True)
line = stdin.readline()
n1 = int(line)

print('Enter another number: ', end='', flush=True)
line = stdin.readline()
n2 = int(line)

print('The sum of', n1, 'and', n2, 'is', n1+n2)
stdin.readline()
