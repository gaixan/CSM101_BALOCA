while True:
    print("W = Warrior")
    print("M = Mage")
    print("H = Healer")
    print("T = Tank")

    balocusername = input("Enter Username: ")
    baloccharacter = input("Select your Profession: ")
    balocaletter = input("Enter the Key word: ")
    balocafound = False

    roles = "W", "M", "H", "T"

    for baloccharacter in roles:
        if baloccharacter.lower() == balocaletter.lower():
            balocafound = True
            break

    if balocafound:
        print("Role has been selected.")
    else:
        print("Role is not found. \n Please choose W (Warrior), M(Mage), H
