text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("String is a palindrome")
else:
    print("String is not a palindrome")