
def print_integers(tuple1):
    for item in tuple1:
        if isinstance(item, int):
            print(item)
        elif isinstance(item, tuple):
            print_integers(item)


nested_tuple = (10, (20, 30), (40, (50, 60)))
print_integers(nested_tuple)
