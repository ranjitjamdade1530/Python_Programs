msg = input("Enter a string: ")

upper = 0
lower = 0

for ch in msg:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower) 