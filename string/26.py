text = input("Enter a string: ")
ch = input("Enter a character to find: ")

first = text.find(ch)
last = text.rfind(ch)

print("First occurrence index:", first)
print("Last occurrence index:", last) 