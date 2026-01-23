# students = ["Abhinash", "Varsha", "Ashutosh", "Ritik", "Bittu"]

# for i in range(len(students)):
#   print( students[i+1])

# size = len(students)
# print(size)

# for i, val in enumerate(['a','b','c']):
#   print(i, val)

# for a, b in zip([1,2, 3], [4,5]):
#     print(a, b)


# p = pow(2,5)
# print(p)

# print(abs(-1))

# print(isinstance(10, int))


students = {
  "Hermione":"Gryffindor",
  "Harry": "Gryffindor", 
  "Ron": "Gryffindor", 
  "Draco": "Slytherin",
}

# print(students["Draco"])

for name in students:
  print(name, students[name], sep=", ")