# Lists and working with lists (mutable)
# Use extend if you want to insert multiple values into a list
courses = ['History', 'Math', 'Physics']
print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])  # Negative indexing
print(courses[0:2])  # Index slicing

# Adding to a list (at the end)
courses.append('Art')
print(courses)

# Adding to a list at a certain point
courses.insert(0, 'Comp Sci')
print(courses)

# Removing from the list
courses.remove('Math')
print(courses)

# Popping the last value out
popped = courses.pop()
print(popped)

# Reversing a list
courses.reverse()
print(courses)

# Sorting a list in ascending order, add reverse parameter if wanted
courses.sort()
print(courses)

# Temp sorting a list
print(sorted(courses))

# Functions
nums = [1, 2, 3, 4, 5]
print(min(nums))
print(max(nums))
print(sum(nums))

# Finding an index
print(courses.index('History'))

# Return true or false
print('Art' in courses)

# for loop
for index, course in enumerate(courses):
    print(index, course)

# Seperating the values
course_str = ' - '.join(courses)
print(course_str)


# Tuples (immutable - don't change)
tuple_1 = ('History', 'Math', 'Physics')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)


# Sets are unordered and no duplicates are allowed
cs_course = {'History', 'Math', 'Physics'}
print(cs_course)
print('Math' in cs_course)

# Creating empty lists, tuples and sets
empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
empty_set = set()
