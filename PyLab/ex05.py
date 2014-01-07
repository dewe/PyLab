# use format method instead of % formatting

# preferred
print("This is {} way of formatting, from version {}.".format("preferred", 2.7))

# deprecated
print("Does this %s work in version %r?" % ("even", 3.3))