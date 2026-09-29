while True:
    balocaname = input("Enter your name: ")
    balocaposition = input("Enter Job Position (Janitor, Clerk, Cashier, Manager): ").lower()
    balocahr = float(input("Enter Hours Worked: "))

    match balocaposition:
        case "janitor":
            balocamonthly = 18000
        case "clerk":
            balocamonthly = 22000
        case "cashier":
            balocamonthly = 40000
        case "manager":
            balocamonthly = 50000
        case _:
            balocamonthly = 0

    if balocamonthly > 0:
        balocabasic = balocamonthly / 2
        balocarate = balocabasic / 88

        if balocahr < 88:
            balocaabsent = 88 - balocahr
            balocaabsence = balocaabsent * balocarate
            balocaover = 0
            balocaoverpay = 0

        else:
            balocaabsent = 0
            balocaabsence = 0
            balocaover = balocahr - 88
            balocarate = balocarate * 1.25
            balocaoverpay = balocaover * balocarate

        balocanet = balocabasic - balocaabsence + balocaoverpay

        print("======================")
        print("HALF MONTH PAYROLL")
        print("======================")

        print("\nEmployee: ", balocaname)
        print("Job Position: ", balocaposition)
        print("Job Hours: ", balocahr)
        print("Monthly Pay: ", balocamonthly)
        print("Basic Half Month Pay: ", balocabasic)
        print("Hours Salary: ", round(balocahr, 2))
        print("Absence Hours: ", balocaabsent)
        print("Absence Deduction: ", round(balocaabsence, 2))
        print("Overtime Hours: ", balocaover)
        print("Overtime Pay: ", round(balocaoverpay, 2))
        print("Half Month Salary: ", round(balocanet, 2))

    else:
        print("Invalid Job Position")

    again = input("\nWould you like to continue Y/N: ")

    if again.upper() != "Y":
        print("Thank you for your time.")
        break
