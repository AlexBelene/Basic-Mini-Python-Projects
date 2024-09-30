# 💳 Bank Account Management System with Loan Feature

<img width="443" alt="370693523-4288cbcb-3108-41c6-b0e8-6753b302d3e5-2" src="https://github.com/user-attachments/assets/1a578d79-3e79-46ea-bc9a-7518af3eb278">


## 🌟 Overview
This project is designed to manage bank accounts with the following capabilities:
- **Create accounts** for users.
- **Deposit** and **withdraw** funds.
- **Check balances** and **view transaction histories**.
- **Transfer funds** between accounts.
- **Manage loans** of up to **10,000 leva** with a **3% interest rate**.

## 📋 Features Explained

1. **Create Account** 🆕
   - Allows users to create a new bank account.
   - Stores the account holder's name, balance, transaction history, and loan information.

2. **Deposit Money** 💵
   - Users can deposit money into their accounts.
   - Updates the account balance and logs the transaction in the history.

3. **Withdraw Money** 💸
   - Users can withdraw money from their accounts.
   - Checks for sufficient funds before allowing the withdrawal and logs the transaction.

4. **Check Balance** 📊
   - Displays the current balance of a specified account holder.

5. **List Accounts** 📋
   - Displays all accounts along with their balances and outstanding loans.

6. **Transfer Funds** 🔄
   - Allows users to transfer money between two accounts.
   - Validates both accounts and ensures the sender has sufficient funds.

7. **View Transaction History** 📜
   - Displays a history of transactions for a specific account holder.

8. **Display Total Funds** 💰
   - Shows the total balance across all accounts in the system.

9. **Delete Account** ❌
   - Allows users to delete their accounts, including all associated data.

10. **Apply for Loan** 🏦
    - Users can apply for a loan up to 10,000 leva.
    - If approved, the loan amount (plus interest) is added to their balance, and the outstanding loan amount is updated.

11. **Repay Loan** 💳
    - Users can make repayments on their loans.
    - Updates both the account balance and the outstanding loan amount.

12. **Exit** 🚪
    - Exits the system.

## 📜 Code Implementation

```python
# Enhanced Bank Account Management System with Loan Feature

# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():

 acc_name = input('New account name:')
 account_holders.append(acc_name)
 balances.append(0)
 transaction_histories.append(0)
 loans.append(0)
 print(f'Account successfully created!')
                                        
 print(f'Your index is:{account_holders.index(acc_name)} ')

def deposit():

 acc_name = input('Enter Account name:')
 if acc_name in account_holders:
     deposit_amount = float(input('Enter deposit amount:'))
     balances[account_holders.index(acc_name)] += deposit_amount
     print(f'You\'r new balance is: {balances[account_holders.index(acc_name)]}')
     transaction_histories[account_holders.index(acc_name)] += 1
 else:
    print('Account does not exist!')

def withdraw():

   acc_name = input('Enter Account name:')
   if acc_name in account_holders:
      withdraw_amount = float(input('Enter withdraw amount:'))
      if withdraw_amount <= balances[account_holders.index(acc_name)]:
         balances[account_holders.index(acc_name)] -= withdraw_amount
         print(f'You\'r new balance is: {balances[account_holders.index(acc_name)]}')
         transaction_histories[account_holders.index(acc_name)] += 1

   else:
      print('Account does not exist!')


def check_balance():

    acc_name = input('Enter Account name:')
    if acc_name in account_holders:
        print(f'You\'r new balance is: {balances[account_holders.index(acc_name)]}')
    else:
       print('Account does not exist!')

def list_accounts():

   if account_holders:
      for account in range(len(account_holders)):
          print(f'{account_holders[account]}\n '
                f'Has a balance of: {balances[account]}\n '
                f'Has a loan of: {loans[account]}')
   else:
       print(f'There are no accounts registered!')

def transfer_funds():

   sender = input()
   recipient = input()
   if sender and recipient in account_holders:
      transfer_amount = float(input('Enter the transfer amount:'))
      if transfer_amount <= balances[account_holders.index(sender)]:
         balances[account_holders.index(sender)] -= transfer_amount
         balances[account_holders.index(recipient)] += transfer_amount
         print(f'{transfer_amount} successfully transferred to {recipient}.')
         transaction_histories[account_holders.index(sender)] += 1
         transaction_histories[account_holders.index(recipient)] += 1
      else:
          print(f'Incufficient funds to transfer')
   else:
       print(f'Not a valid sender or recipient account!')

def view_transaction_history():

    acc_name = input('Enter Account name:')
    if acc_name in account_holders:
        index = account_holders.index(acc_name)
        if transaction_histories[index] == 0:
            print(f'There have been 0 transactions for {acc_name}!')
        else:
            print(f'The transaction history of {acc_name} is {transaction_histories[index]}')
        print('Account does not exist!')

def apply_for_loan():
    name = input("Enter the account holder's name: ")

    if name in account_holders:
        index = account_holders.index(name)


        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))


        if loan_amount <= MAX_LOAN_AMOUNT:

            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)

            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    name = input("Enter the account holder's name: ")

    if name in account_holders:
        index = account_holders.index(name)

        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))

        if repayment_amount <= loans[index]:
            balances[index] -= repayment_amount
            loans[index] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    choice = int(input("Enter your choice: "))
    return choice


def main():
    while True:
        choice = display_menu()

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
```

## 📌 Prerequisites
Python 3.x installed on your system.
