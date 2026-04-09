# A set is a collection data type in Python that is:
# Unordered → items do not have a fixed position
# Unindexed → you cannot access elements using index
# Mutable → you can add or remove items
# Unique → duplicate values are not allowed

# example of set
# s={1, 2, 3, 4, 4, 5}
# print(type(s))
# print(s)

# How to Create a Set
# s1 = {1, 2, 3 }  # method 1
# s2 = ([4, 5, 6])  # method 2
# s3 = set()   # method 3

# set methods  
# 1. add() : Adds one element
# s = {1, 2, 3}
# s.add(4)
# print(s)

# 2. update() : Adds multiple elements
# s = {1, 2, 3}
# s.update([3, 4, 5])
# print(s)

# 3. remove() : Removes element (error if not found)
# s = {1, 2, 3}
# s.remove(1)
# print(s)

# 4. discard() : Removes element (no error if not found)
# s = {1, 2, 3}
# s.discard(10)
# print(s)

# 5. pop() : Removes random element
# s = {1, 2, 3}
# s.pop()
# print(s)

# 6. clear() : Removes all elements
# s = {1, 2, 3}
# s.clear()
# print(s)

# 7. union() : combines two sets
# s1 = {1, 2}
# s2 = {3, 4}
# print(s1.union(s2))

# 8. intersection() : duplicate/ comman elements
# a = {1, 2}
# b = {2, 4}
# print(a.intersection(b))

# 9. difference() : Elements in first but not in second 
# a = {1, 2}
# b = {6, 4}
# print(a.difference(b))

# 10. symmetric_difference() : Elements not common in both
# a = {1, 2}
# b = {6, 4}
# print(a.symmetric_difference(b))

# Take 5 numbers from user and store in set
# number = set()
# for i in range(5):
#     num=int(input(f"enter elements {i+1}: "))
#     number.add(num)
# print("set is", number)    
    

