# Information on functions
# Keep code DRY (Don't repeat yourself)
# Use docstrings to add info about functions
def hello_func(greeting):
    return "Hello {}!".format(greeting)


# Needs the parentheses or it will print memory location
print(hello_func)
print(hello_func('John'))

# *args and **kwargs are used when number of parameters are unknown
# *arguments and keyword arguments


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(*courses, **info)
