import datetime

time = datetime.datetime.now()

users = []
admin_users = []

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

def record_withdrawtransaction(user_id, account_number, amount):
    with open('transactions.txt', 'a') as f:
        f.write(f"{user_id}{account_number},withdrawed:{amount},{datetime.datetime.now()}\n")
def record_deposittransaction(user_id, account_number, amount):
    with open('transactions.txt', 'a') as f:
        f.write(f"{user_id}{account_number},deposited:{amount},{datetime.datetime.now()}\n")

# def transcation_history():
#     file = open("transcation.txt", 'r')
#     file.read()
#     file.close()

def create_acc():

    global users
    
    try:
        with open("users.txt", 'r') as file:
           
            lines = file.readlines()
            if lines:  # If there are any lines in the file
                # Get the last line, split by commas, and retrieve the user_id
                last_line = lines[-1]
                last_user_id = int(last_line.split(',')[0])  
                user_id = last_user_id + 1  
            else:
                user_id = 1  # If the file is empty, start with user_id 1
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
            
            # Write the valid user to the file
            with open("users.txt", 'a') as file:
                file.write(f"{user_id},{username},{password}\n")
            
            print(f"Account created successfully for {username}")
            user_id += 1
            break  # Exit the loop after successful account creation

        



# create_acc()


def user_details():
    acc_num = input("Enter your account number: ")
    address = input("Enter your Address: ")
    phone_nu = input("Enter your phone number: ")
    customer_file = open('customers.txt', 'a')
    customer_file.write[f"{acc_num},{address},{phone_nu}\n"]


# user_details()


def Account_Create():
    i = 1
    account_holder_name = input("Enter Your Full Name: ")
    Account_Number = i
    Initial_Balance = 0

    for i in range(3):
        amount = int(input("Enter the Initial amount: "))
        if amount > 0:
            Balance = Initial_Balance + amount
            print(f"You are Sucessfully depostited {amount}")
            print("Welcome to ABC Bank!! You have sucessfully Created Account.\n Your Account Details as Follows.")
            print(
                f" 1. Account Name: {account_holder_name}\n 2. Accont Number: {Account_Number}\n 3. Current Balance: {Balance}")

            with open('accounts.txt', 'a') as f:
                
                f.write(f"{Account_Number},{current_user},{account_holder_name},{Balance}\n")

                break



        elif amount == 0:
            print("Enter amount Greater than Zero")


        elif amount < 0:
            print("Amount must be positive")
        else:
            print("Enter value in correct format")
    i = i + 1


def deposit_money():
    i = 1

    for i in range(3):
        amount = int(input("Enter the Deposit amount: "))
        if amount > 0:
            Balance = Balance + amount
            print(f"You are Sucessfully depostited {amount}")
            print("Your Current Balance is: ", Balance)
            deposit_time = time
            print(deposit_time)
            record_deposittransaction()
            break

        elif amount == 0:
            print("Enter amount Greater than Zero")


        elif amount < 0:
            print("Amount must be positive")
        else:
            print("Enter value in correct format")
    i = i + 1


def witdraw_money():
    i = 1

    for i in range(3):
        amount = int(input("Enter the Withdrawal amount: "))
        file = open('accounts.txt', 'r')
        acc = file.readlines()
        

        if acc[0] == current_user and amount > 0:
            Balance = Balance + amount
            print(f"You are Sucessfully Withdrawed {amount}")
            print("Your Current Balance is: ", Balance)
            withdrawal_time = time
            print(withdrawal_time)
            record_withdrawtransaction()
            break

        elif amount == 0:
            print("Enter amount Greater than Zero")


        elif amount < 0:
            print("Amount must be positive")
        else:
            print("Enter value in correct format")
    i = i + 1


def check_balance():
    acc_num = input("Enter your Account Number: ")
    file = open ('accounts.txt', 'r')
    check_acc = file.readlines()
    for check in check_acc:
        user_id, full_name, balance = check.split(",")
        print("Your Account Balance is: ", balance)





def main_menu():
    while True:
        choice = input(
            " 1. Create Account\n 2. Check Balance\n 3. Deposit Money \n 4. Withdraw Money\n 5. Transaction History\n 6. Start Menu\n 7. Exit\n")
        if choice == "1":
            Account_Create()
        if choice == "2":
            check_balance()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            witdraw_money()
        elif choice == "5":
            transcation_history()
        elif choice == "6":
            start_menu()
        elif choice == "7":
            break
        else:
            print("Enter valid choice!!")


def login_user():
    global admin_users, users
    with open("admin_users.txt", 'a') as file:
        file.write("admin,admin123\n")
    choice = input("Enter Prefered Number to Enter \n 1. Admin\n 2. Normal User\n 3. Back to Menu\n")
    if choice == "1":
        file = open('admin_users.txt', 'r')
        admins = file.readlines()

        admin_username = input("Enter Admin User Name: ")
        admin_password = input("Enter Admin Password: ")

        # for admin in admins:
        #     admin_username =input("Enter Admin User Name: ")
        #     admin_password = input("Enter Admin Password: ")
        #     default_username, default_Password = admin.strip().split(",")
        #     if default_username == admin_username and default_Password == admin_password:
        #         print("You are sucessfully Logined!")
        #     else:
        #         print("Enter valid credentials!!")

        for admin in admins:


            admin = admin.strip()
            if admin:  # Skip empty lines
                try:
                    user_name, pass_word = admin.split(",")
                    if user_name == admin_username and pass_word == admin_password:
                        print("You are successfully logged in as Admin!\n", main_menu)

                        break
                except ValueError:
                    print(f"Skipping invalid line in users file: {admin}")
                    continue
            else:
                print("Enter correct credentials!")

    elif choice == "2":

        username = input("Enter your user Name: ")
        password = input("Enter your password: ")
        file = open('users.txt', 'r')
        user_credentials = file.readlines()

        for user in user_credentials:
            user = user.strip()
            if user:  # Skip empty lines
                try:
                    user_id, user_name, pass_word = user.split(",")
                    if user_name == username and pass_word == password:
                        print("You are successfully logged in!")
                        main_menu()
                        break
                    # elif user_name != username or pass_word != password:
                    #     print("Enter correct credentials!")
                except ValueError:
                    print(f"Skipping invalid line in users file: {user}")
                    continue
            
            else:
                print("Enter correct credentials!")
    elif choice == "3":
        start_menu()
        current_user = user_id
        return current_user

def start_menu():
    while True:
        choice = input("Welcome to AB Bank!!\n  Choose prefered Number to Enter: \n    1.Login\n    2.Create Account\n")
        if choice == "1":
            login_user()
            break
        elif choice == "2":
            create_acc()
            break
        else:
            print("Please Enter Number 1 or 2!")

start_menu()
