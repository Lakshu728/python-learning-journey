# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "BCA"
# }
# How to Access Data
# print(student)
# print(student["age"])
# print(student.get("name"))

# Adding / Updating Data
# student["marks"] = 89
# student['id'] = 34
# print(student)

# Deleting Data
# del student["course"]     # Remove key
# student.pop("age")        # Remove and return value
# student.clear()           # Empty dictionary
# print(student)

# mportant Dictionary Methods
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}


# 1. keys() : Returns all keys
# print(student.keys())

# 2. values() : Returns all values
# print(student.values())

# 3. items() : Returns key-value pairs
# print(student.items())

# 4. get() : Safe way to access value
# print(student.get("marks","not found"))
# print(student.get("name"))

# 5. update() : Update dictionary
# student.update({'age' : 34, 'course' : 'python'})
# print(student)

# 6. pop() : Removes specific key
# student.pop("age")
# print(student)

# 7. popitem() : Removes last inserted item
# student.popitem()
# print(student)

# 8. copy() : copy dictionary
# new_student = student.copy()
# print(new_student)

# 9. setdefault() : Returns value, if not present then adds key
# student.setdefault("grade", "A")
# print(student)

# Looping in Dictionary
# student = {"name": "Rahul", "age": 20}
# for key in student:
#     print(key, student[key])




