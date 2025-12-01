def check_age(age):
    if age<18:
        raise ValueError("Age must be 18 or above")
    return "Allowed"
print(check_age(28))
#exception triggered this exception should be caught by the func calling check_age

print(check_age(17))