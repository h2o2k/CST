# Importing modules and standard libraries
# Can also use this method to get a function
# from test_module import find_index as fi
# Importing all can be declared by
# from test_module import *

import test_module as tm
import sys
import random
import datetime
import calendar
import os

courses = ['History', 'Math', 'Physics', 'Comp Sci']

index = tm.find_index(courses, 'Math')
print(index)

# Paths that python looks for, local dir and standard library directory
print(sys.path)

# Standard library
random_course = random.choice(courses)
print(random_course)

today = datetime.date.today()
print(today)

print(os.__file__)
