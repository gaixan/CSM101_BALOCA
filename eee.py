classrecord = {
    "Liza": {
        "ShdID": "5001",
        "Grade": [90, 85, 86, 82, 89, 90, 92]
    },
    "Jeremy": {
        "ShdID": "5002",
        "Grade": [72, 75, 69, 80, 84, 75, 85]
    }
}

name = input("Enter student name: ")

if name in classrecord:

    student = classrecord[name]
    grades = student["Grade"]

    # 1. Display student information
    print("Student found!")
    print("Student ID:", student["ShdID"])
    print("Grades:", grades)

    # 3. Calculate the average
    average = sum(grades) / len(grades)
    print("Average:", average)

    # 4. Check if there is a grade below 60
    if any(grade < 60 for grade in grades):
        print("Candidate for intervention")

    # 5. Display highest and lowest grade
    print("Highest grade:", max(grades))
    print("Lowest grade:", min(grades))

else:
    print("Student not found.")
