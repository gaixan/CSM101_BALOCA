while True:
    name = input("Enter your name: ")
    print("Hello", name)

    again = input("Do you want to continue (y/n)? ")

    if again == "n":
        print("Thank you for your time")
        break
