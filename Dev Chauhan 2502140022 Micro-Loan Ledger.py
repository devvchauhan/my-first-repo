'''Mini Project Report: Micro-Loan Ledger & EMI Tracker (M-Project 2)
Name : Dev Chauhan
Enrollment number : 2502140022
B.tech CS, DS, Business'''

import math

# --------------DATA STORAGE---------------
loans={}        # loan_id -> (name, principal, rate, term, emi)
borrowers=set()
payment=[]      # [(payment_id, loan_id, amount, date)]

password='admin'
loan_id_counter = 1
payment_id_counter = 1

# --------------EMI Calculations------------
def calculate_emi(principal, rate, term):
    '''EMI (Equated Monthly Installment)
    EMI = principal * rate * (1+r)^n / ((1+r)^n - 1)
    where r is monthly rate of interest
    and n is the loan tenure in months'''
    monthly_rate=rate/12/100
    emi=principal * monthly_rate * math.pow(1 + monthly_rate, term) / (math.pow(1 + monthly_rate, term) - 1)
    return round(emi, 2)

# --------------CRUD Functions---------------
#CREATE
def add_new_loan():
    global loan_id_counter
    print("\n--- Add New Loan ---")

    name = input("Borrower Name: ")
    principal = float(input("Principal Amount: "))
    rate = float(input("Interest Rate (%): "))
    term = int(input("Loan Term (Months): "))
    emi=calculate_emi(principal,rate,term)
    loan_id=loan_id_counter
    loan_id_counter+=1

    loans[loan_id]=(name,principal,rate,term,emi)
    borrowers.add(name)
    print(f'Loan Added Successfully! Loan ID = {loan_id} and EMI = ₹{emi} per month')

#READ
def view_loan_details():
    print("\n--- View Loan Details ---")
    loan_id=int(input('Enter Loan ID: '))
    if loan_id in loans:
        name,principal,rate,term,emi=loans[loan_id]
        print(f'Borrower: {name}')
        print(f'Principal Amount: ₹{principal}')
        print(f'Rate of Interest: {rate}%')
        print(f'Term: {term} months')
        print(f'EMI = ₹{emi} per month')
    else:
        print('Loan ID not found!')

#UPDATE
def modify_loan():
    print('\n--- Modify Loan ---')
    loan_id=int(input('Enter Loan ID: '))

    if loan_id not in loans:
        print('Loan ID not found!')
        return

    (name,principal,rate,term,emi)=loans[loan_id]

    print("1. Update Interest Rate")
    print("2. Update Loan Term")
    choice = int(input("Select option: "))
    while choice!=1 and choice!=2:
        print("Invalid option! Try Again")
        choice = int(input("Select option: "))

    if choice == 1:
        rate = float(input("Enter New Interest Rate: "))
    elif choice == 2:
        term = int(input("Enter New Loan Term (Months): "))

    #New EMI
    emi = calculate_emi(principal,rate,term)

    loans[loan_id] = name,principal,rate,term,emi
    print("Loan updated successfully!")

#DELETE
def delete_loan():
    print('\n--- Delete Loan ---')
    loan_id=int(input('Enter Loan ID: '))
    if loan_id in loans:
        name=loans[loan_id][0]
        del loans[loan_id]
        if name not in [loan[0] for loan in loans.values()]:           #Checks if there is no other loan in the
            borrowers.discard(name)                                    #name of the borrower which is being deleted.
                                                                       #if True (no other loan) we can safely delete
                                                                       #it from the set borrowers
        print('Loan deleted successfully!')
    else:
        print('Loan ID not Found')

# -------------------- Reports --------------------
def borrower_report():
    print("\n--- Borrower Report ---")
    for name in borrowers:
        print(name)


def loan_report():
    print("\n--- Loan Status Report ---")
    for loan_id, item in loans.items():
        (name, principal, rate, term, emi) = item
        print(f"Loan ID: {loan_id}, Name: {name}, EMI: ₹{emi}/month")


# -------------------- Authentication --------------------
def login():
    attempt = input("Enter Password: ")
    if attempt == password:
        return True
    else:
        print("Wrong password! Try again...")
        return False


# -------------------- Main Menu --------------------
def main():
    if not login():
        return

    while True:
        print("\n====== Micro-Loan & EMI Tracker ======")
        print("1. Add New Loan")
        print("2. View Loan Details")
        print("3. Modify Loan")
        print("4. Delete Loan")
        print("5. Borrower Report")
        print("6. Loan Status Report")
        print("7. Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            add_new_loan()
        elif choice == 2:
            view_loan_details()
        elif choice == 3:
            modify_loan()
        elif choice == 4:
            delete_loan()
        elif choice == 5:
            borrower_report()
        elif choice == 6:
            loan_report()
        elif choice == 7:
            print("Exiting Program! Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

main()
#Thank You