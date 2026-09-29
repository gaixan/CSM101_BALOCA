students = {
    "Ana": 89,
    "Ben": 90,
    "Carlo": 91,
    "Diana": 89,
}
print("Students Grade")
print("==============")
print("Ana:", students["Ana"])
print("Ben:", students["Ben"])
# Add a new student
students["Ella"] = 88
#update a student's grade
students["Carlo"] = 87
students["Diana"] = 88
name1 = input("Student Name: ")
grade1 = input("Grade : ")
students[name1] = grade1
print(students)
print("\nUpdated Student Grade")
print("==============")
for name, grade in students.items():
    print(name, ":", grade)
# search for a student
search = input("\nEnter Student Name to Search: ")
if search in students:
    print(search, " is in Grade: ", students[search])
else:
    print(search, "is not found: ", students[search])