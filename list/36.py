numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Original List:", numbers)
print("List After Removing Odd Numbers:", even_numbers)