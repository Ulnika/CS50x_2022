from validator_collection import validators, errors

inp = input("What's your email addresse? ")

try:
    validator = validators.email(inp)
    print("Valid")
except (errors.EmptyValueError, errors.InvalidEmailError):
    print("Invalid")