share_capital = float(input("Enter share capital: "))
term = int(input("Enter loan term (3, 6, or 12 months): "))

# Loan amount
if share_capital > 100000:
    loan_amount = share_capital * 2
else:
    loan_amount = share_capital * 1.5

# Interest rate using for loop
terms = [3, 6, 12]
rates = [0.05, 0.07, 0.10]

interest_rate = 0

for i in range(3):
    if term == terms[i]:
        interest_rate = rates[i]

# Calculations
service_fee = 200
advance_interest = loan_amount * interest_rate
take_home_loan = loan_amount - advance_interest - service_fee
monthly_due = loan_amount / term

# Display
print("\n===== A-LENDING INC. =====")
print("Loan Amount:", loan_amount)
print("Term:", term, "months")
print("Interest Rate:", interest_rate * 100, "%")
print("Service Fee:", service_fee)
print("Advance Interest:", advance_interest)
print("Take Home Loan:", take_home_loan)
print("Monthly Due:", monthly_due)
