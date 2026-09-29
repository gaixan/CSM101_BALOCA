balocaclassrecord = {"Liza": {"ShdID": "5001", "Grade": [90, 85, 86, 82, 89, 90, 92]},"Jeremy": {"ShdID": "5002", "Grade": [72, 75, 69, 80, 84, 75, 85]}
}
balocaname = input("Enter Student Name: ").lower()
for name in balocaclassrecord:
    if balocaname == name.lower():

        balocastudent = balocaclassrecord[name]
        balocagrades = balocastudent["Grade"]
        print()
        print("==============")
        print("Student found!")
        print("Student ID:", balocastudent["ShdID"])
        print("Grades:", balocagrades)
        average = sum(balocagrades) // len(balocagrades)
        print("Average:", average)

        if any(grade < 60 for grade in balocagrades):
            print("Candidate for intervention")

        print("Highest grade:", max(balocagrades))
        print("Lowest grade:", min(balocagrades))
        break
else:
    print("Student not found.")
