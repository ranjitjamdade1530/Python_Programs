num = int(input("Enter a number: "))

total = 0

for digit in str(num):
    fact = 1

    for i in range(1, int(digit) + 1):
        fact *= i

    total += fact

if total == num:
    print("Strong Number")
else:
    print("Not a Strong Number")