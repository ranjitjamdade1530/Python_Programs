numbers = [10, 20, 30, 20, 40]

# 1. append()
numbers.append(50)
print("After append():", numbers)

# 2. extend()
numbers.extend([60, 70])
print("After extend():", numbers)

# 3. insert()
numbers.insert(1, 15)
print("After insert():", numbers)

# 4. remove()
numbers.remove(20)
print("After remove():", numbers)

# 5. pop()
numbers.pop()
print("After pop():", numbers)

# 6. index()
print("Index of 30:", numbers.index(30))

# 7. count()
print("Count of 20:", numbers.count(20))
 
# 8. sort()
numbers.sort()
print("After sort():", numbers)

# 9. reverse()
numbers.reverse()
print("After reverse():", numbers)

# 10. copy()
new_list = numbers.copy()
print("After copy():", new_list)

# 11. clear()
new_list.clear()
print("After clear():", new_list)