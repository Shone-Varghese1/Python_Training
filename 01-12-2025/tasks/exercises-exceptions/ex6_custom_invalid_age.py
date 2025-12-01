# Create a function that raises a custom exception InvalidAgeError if age < 18.
class InvalidAge(Exception):
    pass
def check_age(age):
    if age < 18:
        raise InvalidAge("Age is less than 18")
    return "valid age"
print(check_age(18))
print(check_age(14))
