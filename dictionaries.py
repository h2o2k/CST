# Dictionaries Also known as hash maps or associative arrays
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Comp Sci']}
print(student)

# Accessing
print(student['name'])
print(student['courses'])

# Method for accessing data in the dict
print(student.get('name'))
print(student.get('phone', 'Not found'))

# Adding to the dict
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student.get('name'))
print(student.get('phone'))

# Updating the dict
student.update({'name': 'Doe', 'age': 21})
print(student)

# Deleting a key, can also use pop here similar to lists
del student['age']
print(student)

# Showing the contents of a dict
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# Looping through a dict
for key, value in student.items():
    print(key, value)
