try:
    value=int("50")
except ValueError:
    print("invalid conversion")
else:
    print("conversion successful",value)