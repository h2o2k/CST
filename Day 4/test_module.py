# Module designed to show importing
print("Importing module...")


def find_index(to_search, target):
    '''Finds the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
