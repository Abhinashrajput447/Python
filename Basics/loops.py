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


# students = {
#   "Hermione":"Gryffindor",
#   "Harry": "Gryffindor", 
#   "Ron": "Gryffindor", 
#   "Draco": "Slytherin",
# }

# print(students["Harry"])

students = [
  {"name": "Ahinash", "house":"Vijayaada", "patronus": "Other"},
  {"name": "Varsha", "house":"Madhuban", "patronus": "Other"},
  {"name": "Ritik", "house":"Sitakund", "patronus": "BPSC"},
  {"name": "Ashutosh", "house":"Chap", "patronus": None},
]

for i, student in enumerate(students):
  print(i, student["name"], student["house"], student["patronus"], sep=", ")