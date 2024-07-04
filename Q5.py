# function to get account balance
def get_balance(account_number):
    with open('accounts.txt', 'r') as file:
        for line in file:
            acc_num, balance = line.strip().split(',')
            if acc_num == account_number:
                return float(balance)
    return None

#update function
def update_account(account_number, balance):
    lines = []
    with open('accounts.txt', 'r') as file:
        lines = file.readlines()

    with open('accounts.txt', 'w') as file:
        for line in lines:
            acc_num, _ = line.strip().split(',')
            if acc_num == account_number:
                file.write(f"{account_number},{balance}\n")
            else:
                file.write(line)

#deposit function
def deposit(account_number, amount):
    balance = get_balance(account_number)
    if balance is not None:
        balance += amount
        update_account(account_number, balance)

# withdraw function
def withdraw(account_number, amount):
    balance = get_balance(account_number)
    if balance is not None and balance >= amount:
        balance -= amount
        update_account(account_number, balance)
    elif balance is not None:
        print("Insufficient funds")
    else:
        print("Account not found")

# Statements and Operations

print(get_balance('12345')) 
deposit('12345', 500)
print(get_balance('12345')) 
withdraw('12345', 200)
print(get_balance('12345')) 
withdraw('12345', 2000)   
