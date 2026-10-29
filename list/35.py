numbers = [10, 15, 20, 25, 30, 35, 40]

odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print("Original List:", numbers)
print("List After Removing Even Numbers:", odd_numbers)