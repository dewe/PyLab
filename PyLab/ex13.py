from sys import argv

print(argv)
argv.append(input('Another param? '))

# unpack into variables
script, first, second, third = argv

print('The script is called', script)
print('Your first variable is', first)
print('Your second variable is', second)
print('Your third variable is', third)

