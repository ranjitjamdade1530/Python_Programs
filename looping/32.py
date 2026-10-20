base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1
i = 0

while i < exponent:
    result *= base
    i += 1

print("Power =", result)