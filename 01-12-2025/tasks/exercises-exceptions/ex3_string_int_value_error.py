# Write a function that converts a string to integer and handles invalid inputs.
def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        print("The value cannot be converted to an integer.")

print(string_to_int("0"))
print(string_to_int("1a"))