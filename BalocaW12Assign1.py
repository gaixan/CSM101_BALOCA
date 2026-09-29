patients = {
    "Ana": [80, 50, 150, 90, 140],
    "Ben": [130, 140, 135, 90, 140],
    "Carlo": [90, 100, 95, 90, 140]
}

print(patients)
print()

for key, values in patients.items():
    print("\nPatient:", key)
    print("---Blood Sugar Summary---")

    for item in values:
        if item <= 70:
            print(item, "= Low blood sugar")
        elif item <= 120:
            print(item, "= Normal blood sugar")
        else:
            print(item, "= High blood sugar")

for name, values in patients.items():
    maximum = max(values)
    minimum = min(values)
    average = sum(values) / len(values)
    difference = maximum - minimum

    print("\nPatient:", name)
    print("Blood sugar:", values)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Average:", round(average, 2))
    print("Difference:", difference)
