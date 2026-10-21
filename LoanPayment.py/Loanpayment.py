#Loanpayment.py

"""recieves loan principle, annual interest rate, numer of years, and returns the monthly loan payment. It then tells the user the ramaining ballance after monthly payments and creates a table."""

def loan_payment(P, i, t):
    total = (P * (i / 12)) / (1 - (1 + (i / 12)) ** (-12 * t))
    return total

def table_print(M, I, P, R):
   table = print(f"{M:>5} {I:>14.2f} {P:>16.2f} {R:>28.2f}")
   return table

P = float(input("Enter loan amount: "))

i = float(input("Enter interest rate as a decimal: "))

t = float(input("Enter number of years: "))

monthly_payment = loan_payment(P, i, t)

month = 1

total_payment = monthly_payment * 12 * t

total_interest = total_payment - P
print()
print(f"The monthly payment will be ${monthly_payment:.2f}")
print(f"The total payments over 30 years will be ${total_payment:.2f}")
print(f"The total interest paid over 30 years will be ${total_interest:.2f}")
print("\n")
print("Loan Amorization Table:\n")
print("Month\t\tInterest\t\tPrinciple\t\tRemaining Loan Balance")

while not month > 12 * t:
   interest = P * i * (1/12)
   principle = monthly_payment - interest
   P = P - principle
   table_print(month, interest, principle, P)
   month +=1