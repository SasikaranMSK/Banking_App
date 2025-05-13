import datetime
import random

time = datetime.datetime.now()

users = []
admin_users = []
current_user = None  # Track current login user
current_admin = False  # Track current admin


def generate_account_number():
    try:
        with open('accounts.txt', 'r') as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                last_account_number = int(last_line.split(',')[0])
                return f"{last_account_number + 1:06d}"
    except FileNotFoundError:
        pass
    return "000001"


def check_existing_account(user_id):
    try:
        with open('accounts.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 2 and parts[1] == str(user_id):
                    return True
    except FileNotFoundError:
        pass
    return False


def get_last_user_id():
    try:
        with open("users.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                last_id = int(last_line.split(",")[0])
                return last_id
    except FileNotFoundError:
        pass
    return 0


def record_transaction(user_id, account_number, transaction_type, amount):
    with open('transactions.txt', 'a') as f:
        f.write(f"{user_id},{account_number},{transaction_type},{amount},{datetime.datetime.now()}\n")


def transaction_history(user_id=None, account_number=None):
    try:
        with open("transactions.txt", 'r') as file:
            print("\nTransaction History:")
            for line in file:
                parts = line.strip().split(',')
                # If user id provided filter by user id
                if user_id and parts[0] != str(user_id):
                    continue
                # If account number provided filter by account number
                if account_number and parts[1] != account_number:
                    continue
                print(f"Account: {parts[1]}, Type: {parts[2]}, Amount: {parts[3]}, Time: {parts[4]}")
    except FileNotFoundError:
        print("No transaction history found.")


def create_acc():
    global users

    try:
        with open("users.txt", 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                last_user_id = int(last_line.split(',')[0])
                user_id = last_user_id + 1
            else:
                user_id = 1
    except FileNotFoundError:
        user_id = 1

    for i in range(3):
        username = input("Create a user Name: ")

        if not username:
            print("User name can't be empty!!")
            continue

        password = input("Create a password: ")

        if not password:
            print("Password can't be empty!!")
            continue

        elif len(password) < 6:
            print("Password must be more than six characters!!")
            continue

        else:
            users.append([user_id, username, password])

            with open("users.txt", 'a') as file:
                file.write(f"{user_id},{username},{password}\n")

            print(f"Account created successfully for {username}")
            return user_id  # Return the new user ID

    print("Failed to create account after 3 attempts.")
    return None


def user_details(user_id):
    acc_num = input("Enter your account number: ")
    address = input("Enter your Address: ")
    phone_nu = input("Enter your phone number: ")
    nic = input("Enter your NIC Number: ")
    with open('customers.txt', 'a') as customer_file:
        customer_file.write(f"{user_id},{acc_num},{address},{phone_nu}\n")


def get_account_balance(user_id, account_number):
    try:
        with open('accounts.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    if parts[0] == account_number and parts[1] == str(user_id):
                        return float(parts[3])
    except FileNotFoundError:
        pass
    return None


def get_all_accounts():
    accounts = []
    try:
        with open('accounts.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    accounts.append({
                        'account_number': parts[0],
                        'user_id': parts[1],
                        'account_name': parts[2],
                        'balance': parts[3]
                    })
    except FileNotFoundError:
        pass
    return accounts


def get_all_users():
    users = []
    try:
        with open('users.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    users.append({
                        'user_id': parts[0],
                        'username': parts[1],
                        'password': parts[2]
                    })
    except FileNotFoundError:
        pass
    return users


def get_user_details(user_id):
    try:
        with open('customers.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if parts[0] == str(user_id):
                    return {
                        'user_id': parts[0],
                        'account_number': parts[1],
                        'address': parts[2],
                        'phone': parts[3]
                    }
    except FileNotFoundError:
        pass
    return None


def update_account_balance(user_id, account_number, new_balance, account_name):
    accounts = []
    updated = False

    try:
        with open('accounts.txt', 'r') as f:
            accounts = f.readlines()
    except FileNotFoundError:
        pass

    with open('accounts.txt', 'w') as f:
        for account in accounts:
            parts = account.strip().split(',')
            if len(parts) >= 4 and parts[0] == account_number and parts[1] == str(user_id):
                f.write(f"{account_number},{user_id},{account_name},{new_balance}\n")
                updated = True
            else:
                f.write(account)

        if not updated:
            f.write(f"{account_number},{user_id},{account_name},{new_balance}\n")


def change_admin_password(username, new_password):
    admins = []
    updated = False

    try:
        with open('admin_users.txt', 'r') as f:
            admins = f.readlines()
    except FileNotFoundError:
        pass

    with open('admin_users.txt', 'w') as f:
        for admin in admins:
            parts = admin.strip().split(',')
            if parts[0] == username:
                f.write(f"{username},{new_password}\n")
                updated = True
            else:
                f.write(admin)

        if not updated:
            f.write(f"{username},{new_password}\n")


def admin_menu():
    global current_admin

    while True:
        print("\nAdmin Menu")
        print("1. View All User Accounts")
        print("2. View Account Balances")
        print("3. View Transaction History")
        print("4. Change Admin Password")
        print("5. Create New Bank Account for User")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAll User Accounts:")
            users = get_all_users()
            for user in users:
                print(f"User ID: {user['user_id']}, Username: {user['username']}")
                details = get_user_details(user['user_id'])
                if details:
                    print(f"  Account Number: {details['account_number']}")
                    print(f"  Address: {details['address']}")
                    print(f"  Phone: {details['phone']}")
                print("--------------------")

        elif choice == "2":
            print("\nAll Account Balances:")
            accounts = get_all_accounts()
            for account in accounts:
                user_details = get_user_details(account['user_id'])
                username = next((u['username'] for u in get_all_users() if u['user_id'] == account['user_id']),
                                "Unknown")
                print(f"Account: {account['account_number']} ({account['account_name']})")
                print(f"  User: {username} (ID: {account['user_id']})")
                print(f"  Balance: {account['balance']}")
                print("--------------------")

        elif choice == "3":
            print("\nTransaction History Options:")
            print("1. View All Transactions")
            print("2. View Transactions for Specific Account")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                transaction_history()
            elif sub_choice == "2":
                account_number = input("Enter account number: ")
                transaction_history(account_number=account_number)
            else:
                print("Invalid choice!")

        elif choice == "4":
            new_password = input("Enter new admin password: ")
            if len(new_password) < 6:
                print("Password must be at least 6 characters!")
                continue

            confirm_password = input("Confirm new password: ")
            if new_password != confirm_password:
                print("Passwords don't match!")
                continue

            change_admin_password("admin", new_password)
            print("Admin password changed successfully!")

        elif choice == "5":
            user_id = input("Enter user ID for the new account: ")
            account_name = input("Enter account holder name: ")
            account_number = generate_account_number()
            initial_balance = float(input("Enter initial balance: "))

            update_account_balance(user_id, account_number, initial_balance, account_name)
            print(f"New account created for user {user_id}")
            print(f"Account Number: {account_number}")
            print(f"Initial Balance: {initial_balance}")

        elif choice == "6":
            current_admin = False
            print("Logging out from admin account...")
            break

        else:
            print("Invalid choice! Please try again.")


def Account_Create(user_id):
    if check_existing_account(user_id):
        print("You already have a bank account!")
        return

    account_holder_name = input("Enter Your Full Name: ")
    account_number = generate_account_number()

    for i in range(3):
        try:
            amount = float(input("Enter the Initial amount: "))
            if amount > 0:
                update_account_balance(user_id, account_number, amount, account_holder_name)
                print(f"You have successfully deposited {amount}")
                print("Welcome to ABC Bank!! You have successfully created an account.")
                print(f"1. Account Name: {account_holder_name}")
                print(f"2. Account Number: {account_number}")
                print(f"3. Current Balance: {amount}")
                record_transaction(user_id, account_number, "deposit", amount)
                break
            elif amount == 0:
                print("Enter amount greater than zero")
            else:
                print("Amount must be positive")
        except ValueError:
            print("Please enter a valid number")
    else:
        print("Failed to create account after 3 attempts.")


def deposit_money(user_id):
    account_number = input("Enter your account number: ")
    current_balance = get_account_balance(user_id, account_number)

    if current_balance is None:
        print("Account not found!")
        return

    for i in range(3):
        try:
            amount = float(input("Enter the Deposit amount: "))
            if amount > 0:
                new_balance = current_balance + amount
                update_account_balance(user_id, account_number, new_balance, "")
                print(f"You have successfully deposited {amount}")
                print("Your Current Balance is: ", new_balance)
                record_transaction(user_id, account_number, "deposit", amount)
                break
            elif amount == 0:
                print("Enter amount greater than zero")
            else:
                print("Amount must be positive")
        except ValueError:
            print("Please enter a valid number")
    else:
        print("Transaction cancelled after 3 attempts.")


def withdraw_money(user_id):
    account_number = input("Enter your account number: ")
    current_balance = get_account_balance(user_id, account_number)

    if current_balance is None:
        print("Account not found!")
        return

    for i in range(3):
        try:
            amount = float(input("Enter the Withdrawal amount: "))
            if amount > 0:
                if amount <= current_balance:
                    new_balance = current_balance - amount
                    update_account_balance(user_id, account_number, new_balance, "")
                    print(f"You have successfully withdrawn {amount}")
                    print("Your Current Balance is: ", new_balance)
                    record_transaction(user_id, account_number, "withdrawal", amount)
                    break
                else:
                    print("Insufficient funds!")
            elif amount == 0:
                print("Enter amount greater than zero")
            else:
                print("Amount must be positive")
        except ValueError:
            print("Please enter a valid number")
    else:
        print("Transaction cancelled after 3 attempts.")


def check_balance(user_id):
    try:
        with open('accounts.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 4 and parts[1] == str(user_id):
                    print(f"Account Number: {parts[0]}")
                    print(f"Account Name: {parts[2]}")
                    print(f"Current Balance: {parts[3]}")
                    return
        print("No account found for this user!")
    except FileNotFoundError:
        print("No accounts exist yet!")


def main_menu(user_id):
    while True:
        print("\nMain Menu")
        choice = input(
            "1. Create Bank Account\n2. Check Balance\n3. Deposit Money\n4. Withdraw Money\n5. Transaction History\n6. Logout\n")

        if choice == "1":
            Account_Create(user_id)
        elif choice == "2":
            check_balance(user_id)
        elif choice == "3":
            deposit_money(user_id)
        elif choice == "4":
            withdraw_money(user_id)
        elif choice == "5":
            transaction_history(user_id)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")


def login_user():
    global current_user, current_admin

    while True:
        choice = input("\n1. Admin\n2. Normal User\n3. Back to Menu\n")

        if choice == "1":
            with open("admin_users.txt", 'a') as file:  # Create file if not exists
                file.write("admin,admin123\n")

            admin_username = input("Enter Admin User Name: ")
            admin_password = input("Enter Admin Password: ")

            with open('admin_users.txt', 'r') as file:
                for admin in file:
                    admin = admin.strip()
                    if admin:
                        try:
                            user_name, pass_word = admin.split(",")
                            if user_name == admin_username and pass_word == admin_password:
                                print("You are successfully logged in as Admin!")
                                current_admin = True
                                admin_menu()
                                return
                        except ValueError:
                            continue
            print("Invalid admin credentials!")

        elif choice == "2":
            username = input("Enter your user Name: ")
            password = input("Enter your password: ")

            try:
                with open('users.txt', 'r') as file:
                    for user in file:
                        user = user.strip()
                        if user:
                            try:
                                user_id, user_name, pass_word = user.split(",")
                                if user_name == username and pass_word == password:
                                    print("You are successfully logged in!")
                                    current_user = int(user_id)
                                    main_menu(current_user)
                                    return
                            except ValueError:
                                continue
                print("Invalid username or password!")
            except FileNotFoundError:
                print("No users found. Please create an account first.")

        elif choice == "3":
            return
        else:
            print("Invalid choice!")


def start_menu():
    while True:
        print("\nWelcome to AB Bank!")
        choice = input("1. Login\n2. Create Account\n3. Exit\n")

        if choice == "1":
            login_user()
        elif choice == "2":
            user_id = create_acc()
            if user_id:
                print("Account created successfully! Please login.")
        elif choice == "3":
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3!")


if __name__ == "__main__":
    start_menu()