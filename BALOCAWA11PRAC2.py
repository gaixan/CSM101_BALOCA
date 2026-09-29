students = {"Ana":[90,85,82],
            "Kirk":[72,73,78]}

students = {"Ana":(90,85,82),
            "Kirk":(72,73,78)}

for name, grade in students.items():
    print(name,*grade)
