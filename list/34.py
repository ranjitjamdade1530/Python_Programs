list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common_elements = []

for num in list1:
    if num in list2:
        common_elements.append(num)

print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", common_elements)