while True:
    balocachar = input("Enter character: ")
    balocaletter = input("Enter a character to search for: ")

    balocafound = False

    for balocachar in balocachar:
        if balocachar.lower() == balocaletter.lower():
            balocafound = True
            break

    if balocafound:
        print("Character found.")
    else:
        print("Character is not found.")

    again = input("Do you want to try again? (Y/N): ")
    if again.upper() != "Y":
        break
