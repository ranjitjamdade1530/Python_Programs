text = input("Enter a string: ")
sub = input("Enter a substring: ")

if text.startswith(sub):
    print("String starts with the given substring")
else:
    print("String does not start with the given substring")