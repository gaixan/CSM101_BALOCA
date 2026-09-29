pizza = [
    ("Hawaiian", "Small", 250),
    ("Hawaiian", "Medium", 350),
    ("Hawaiian", "Large", 450),

    ("Pepperoni", "Small", 250),
    ("Pepperoni", "Medium", 350),
    ("Pepperoni", "Large", 450),
]

print("======Welcome to Pizzaria======")
print("Select your pizza:")
print("1. Hawaiian Pizza")
print("2. Pepperoni Pizza")
print("3. Cheese Pizza")

flavor = input("Enter flavor: ")

if flavor == "1":
    flavor = "Hawaiian"
elif flavor == "2":
    flavor = "Pepperoni"
elif flavor == "3":
    flavor = "Cheese"
else:
    print("Invalid flavor")
    flavor = ""

if flavor != "":
    print()
    print("Choose size:")
    print("1. Small")
    print("2. Medium")
    print("3. Large")

    size = input("Enter size: ")

    if size == "1":
        size = "Small"
    elif size == "2":
        size = "Medium"
    elif size == "3":
        size = "Large"
    else:
        print("Invalid size")
        size = ""

    if size != "":
        for pizza in pizza:
            if pizza[0] == flavor and pizza[1] == size:
                price = pizza[2]

print ()
print("=====ORDER SUMMARY=====")
print("Flavor: ", flavor)
print("Size: ", size)
print("Price: ", price)
