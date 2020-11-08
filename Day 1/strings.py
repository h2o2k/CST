# Printing "Hello World!"
message = 'Hello World!'
print(message)

# Avoiding ending a string early
message = "Hello's World!"
print(message)

# Another way to deal with ending a string early
message = 'Hello\'s World!'
print(message)

# Counting the length of the string
message = 'Hello World!'
print(len(message))

# Slicing the string
message = 'Hello World!'
print(message[0:5])

# Using pre-existing methods on the string
message = 'Hello World!'
print(message.upper())
print(message.lower())
print(message.title())
print(message.count('l'))
print(message.find('World'))

# Replacing sections of the string
message = 'Hello World!'
message = message.replace('World', 'Universe')
print(message)

# Concatenating strings and fstrings in 3.6+
greeting = "Hello"
name = "John"
message = f"{greeting}, {name.upper()}. Welcome!"
print(message)

# Gets methods we can use on strings
print(dir(name))
print(help(str.lower))
