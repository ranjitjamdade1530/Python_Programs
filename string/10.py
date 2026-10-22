text = input("Enter a string: ")
ch = input("Enter a character: ")

if ch in text:
    print("Index of character =", text.index(ch))
else:
    print("Character not found") 