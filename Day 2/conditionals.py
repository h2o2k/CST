# IF, ELSE and ELIF statements
#
# Comparison operators
# Equal: 3 == 2
# Not equal: 3 != 2
# Greater than: 3 > 2
# Less than: 3 < 2
# Greater or equal: 3 >= 2
# Less than or equal: 3 =< 2
# Object indentity: is
#
# False values include False, None, 0 and any empty variable(List, string, dict)
if True:
    print('Conditional was True')

language = 'Python'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('Unknown language')

# AND, OR, NOT
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Welcome Admin!')
else:
    print('Error: 404')

# Object indentity, testing if same slot in memory
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)
