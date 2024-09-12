import time

print("Please insert your card")
time.sleep(2)  # Adjust the sleep time as needed

password = 9078
balance = 10000

pin = int(input("Enter your PIN: "))

if pin == password:
    while True:
        print("""
        1. Check Balance
        2. Withdraw Balance
        3. Deposit Balance
        4. Exit
        """)
        
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue
        
        if option == 1:
            print(f"Your current balance is {balance}")
        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw amount: "))
            if withdraw_amount > balance:
                print("Insufficient balance")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your updated balance is {balance}")
        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")
        elif option == 4:
            print("Thank you for using our service!")
            break
        else:
            print("Invalid option, please try again")
else:
    print("Wrong PIN, please try again")