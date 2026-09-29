students = {}

number = int(input("Enter Number of Students: "))

for i in range(number):
    print("\nStudent", i + 1)

    name = input("Enter Student Name: ")

    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))

    students[name] = (grade1, grade2, grade3)

print("\n====== Student Record ======")

highest = 0
lowest = 100
namehighest = ""
namelowest = ""
tally = 0

for name, grade in students.items():
    average = sum(grade) // len(grade)
    print(name, *grade, "Average:", round(average, 2))
    if average > highest:
        highest = average
        namehighest = name
    elif average < lowest:
        lowest = average
        namelowest = name
    for g in grade:
        if g < 75:
            tally += 1

print(f"Student {namehighest} is highest average: {highest}")
print(f"Student {namelowest} is lowest average: {lowest}")
print(f"There are {tally} grades which are below 75.")
