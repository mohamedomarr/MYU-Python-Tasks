"""The main Names list"""
Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']

"""Task 1: Transform all names to uppercase"""
def uppercase_names():
    print("Task 1 - Normal List:")
    upper_names_normal = []
    for name in Names:
        upper_names_normal.append(name.upper())
    print(upper_names_normal)

    print("Task 1 - List Comprehension:")
    upper_names_list_comprehension = [name.upper() for name in Names]
    print(upper_names_list_comprehension)

    print("Task 1 - Functional Programming:")
    upper_names_functional = list(map(str.upper, Names))
    print(upper_names_functional)
    print('-'*40)

"""Task 2: Get the names that contains 'a' """
def names_with_a():
    print("Task 2 - Normal List:")
    names_with_a_normal = []
    for name in Names:
        if 'a' in name:
            names_with_a_normal.append(name)
    print(names_with_a_normal)

    print("Task 2 - List Comprehension:")
    names_with_a_list_comprehension = [name for name in Names if 'a' in name]
    print(names_with_a_list_comprehension)

    print("Task 2 - Functional Programming:")
    names_with_a_functional = list(filter(lambda name: 'a' in name, Names))
    print(names_with_a_functional)
    print('-'*40)

"""Task 3: Get the names that starts with 't'"""
def names_starting_with_t():
    print("Task 3 - Normal List:")
    names_with_t_normal = []
    for name in Names:
        if name.startswith('t'):
            names_with_t_normal.append(name)
    print(names_with_t_normal)

    print("Task 3 - List Comprehension:")
    names_with_t_list_comprehension = [name for name in Names if name.startswith('t')]
    print(names_with_t_list_comprehension)

    print("Task 3 - Functional Programming:")
    names_with_t_functional = list(filter(lambda name: name.startswith('t'), Names))
    print(names_with_t_functional)
    print('-'*40)

"""Task 4: Get the names that contains 2 or more 'a' letter"""
def names_with_2_or_more_a():
    print("Task 4 - Normal List:")
    names_with_2a_normal = []
    for name in Names:
        if name.count('a') >= 2:
            names_with_2a_normal.append(name)
    print(names_with_2a_normal)

    print("Task 4 - List Comprehension:")
    names_with_2a_list_comprehension = [name for name in Names if name.count('a') >= 2]
    print(names_with_2a_list_comprehension)

    print("Task 4 - Functional Programming:")
    names_with_2a_functional = list(filter(lambda name: name.count('a') >= 2, Names))
    print(names_with_2a_functional)
    print('-'*40)

"""Task 5: Print a list contains the len of each word in the list"""
def name_lengths():
    print("Task 5 - Normal List:")
    lengths_normal = []
    for name in Names:
        lengths_normal.append(len(name))
    print(lengths_normal)

    print("Task 5 - List Comprehension:")
    lengths_list_comprehension = [len(name) for name in Names]
    print(lengths_list_comprehension)

    print("Task 5 - Functional Programming:")
    lengths_functional = list(map(len, Names))
    print(lengths_functional)
    print('-'*40)

"""Task 6, 7, 8, 9: Unpack the list in a,b"""
def unpack_list():
    print("Task 6, 7, 8, 9: Unpack the list in a,b")
    """Task 7 - a= the first index , b = rest of the list"""
    print("Task 7 - a= the first index , b = rest of the list")
    a, *b = Names
    print("a:", a)
    print("b:", b)
    print('-'*40)

    """Task 8 - a = the first index , b = the last index"""
    print("Task 8 - a = the first index , b = the last index")
    a, *_, b = Names
    print("a:", a)
    print("b:", b)
    print('-'*40)

    """Task 9 - a = the first index , b = the second index"""
    print("Task 9 - a = the first index , b = the second index")
    a, b, *_ = Names
    print("a:", a)
    print("b:", b)
    print('-'*40)

# Test the functions
print(f"The original list: {Names}")
print('-'*40)
uppercase_names()
names_with_a()
names_starting_with_t()
names_with_2_or_more_a()
name_lengths()
unpack_list()
