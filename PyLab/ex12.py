# raw_input() was renamed to input(). That is, the new input() function 
# reads a line from sys.stdin and returns it with the trailing newline stripped

age = input("How old are you? ")
height = input("How tall are you? ")

print("So you're {0} old and {1} tall.".format(age, height))

print("Dat: {0!r}".format(input("Wat? ")))
