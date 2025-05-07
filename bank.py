import datetime
time = datetime.datetime.now()


users = []
admin_users = []
def create_acc():
    user_id = 1
    i=0
    global users
    for i in range(3):
        username = input("Create a user Name: ")
        if not username:
            print("User name can't be empty!!")
            
        # else:
            #continue
        password = input("Create a password: ")
        if not password:
            print("Password can't be empty!!")
            # continue
        elif len(password)<6:
            print("Password must be more than six charactors!!")
            # continue
        else:
            users.append([user_id, username, password])

            with open("users.txt", 'a') as file:
                for user in users:
                # file.write(f"{user[0]},{user[1]},{user[2]}\n")
                    last_user_id = user[0]
                    user_id = int(last_user_id) + 1

                
                
                file.write(f"{user_id},{username},{password}\n")
            break
        i += 1
    # users =[username, password]
    
    

    
    # file = open("users.txt", 'a')
    # file.writelines()
    
    
    

create_acc()

def user_details():
    acc_num = input("Enter your account number: ")
    address = input("Enter your Address: ")
    phone_nu = input("Enter your phone number: ")
    customer_file = open('customers.txt', 'a')
    customer_file.write[f"{acc_num},{address},{phone_nu}\n"]
# user_details()

def login_user():
    global admin_users, users
    with open("admin_users.txt", 'a') as file:
        file.write("admin,admin123\n")
    choice = input("Enter Prefered Number to Enter \n 1. Admin\n 2. Normal User\n")
    if choice == "1":
        file = open('admin_users.txt', 'r')
        admins = file.readlines()

        admin_username =input("Enter Admin User Name: ")
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

            main_menu = main_menu()
            admin = admin.strip() 
            if admin:  # Skip empty lines
                try:
                    user_name, pass_word = admin.split(",")
                    if user_name == admin_username and pass_word == admin_password:
                        print("You are successfully logged in as Admin!\n",main_menu)
                        
                        break
                except ValueError:
                    print(f"Skipping invalid line in users file: {admin}")
                    continue
        print("Enter correct credentials!")

    elif choice == "2":
        
        username = input("Enter your user Name: ")
        password = input("Enter your password: ")
        file = open('users.txt', 'r')
        user_credentials = file.readlines()

        # for user in user_credentials:
        #     user_id, user_name, pass_word = user.split(",")

        #     if user_name == username and pass_word == password:
        #         current_user = user
        #         menu()
        #     else:
        #         print("Enter correct crdentials!")

        for user in user_credentials:
            user = user.strip()
            if user:  # Skip empty lines
                try:
                    user_id, user_name, pass_word = user.split(",")
                    if user_name == username and pass_word == password:
                        print("You are successfully logged in!")
                        main_menu()
                        break
                except ValueError:
                    print(f"Skipping invalid line in users file: {user}")
                    continue
        print("Enter correct credentials!")

# login_user()
        
        
def Account_Create():
    i= 1
    accout_holder_name = input("Enter Your Full Name: ")
    Account_Number = i
    Initial_Balance = 0
    
    
    for i in range (3):
        amount = int(input("Enter the Initial amount: "))
        if  amount >0:
            Balance = Initial_Balance + amount
            print(f"You are Sucessfully depostited {amount}")
            print("Welcome to ABC Bank!! You have sucessfully Created Account.\n Your Account Details as Follows.")
            print(f" 1. Account Name: {accout_holder_name}\n 2. Accont Number: {Account_Number}\n 3. Current Balance: {Balance}")
            
            with open('accounts.txt', 'a') as f:
                f.write(f"{account_number},{account_holder_name},{balance}\n")
                break
            
            
            
        elif amount == 0 :
            print("Enter amount Greater than Zero")
        
            
        elif amount<0:
            print("Amount must be positive")
        else:
            print("Enter value in correct format")
    i=i+1      
        



def deposit_money():
    i= 1
    
    for i in range (3):
        amount = int(input("Enter the Deposit amount: "))
        if  amount >0:
            Balance = Balance + amount
            print(f"You are Sucessfully depostited {amount}")
            print("Your Current Balance is: ", Balance)
            deposit_time = time
            print(deposit_time)
            break
                
        elif amount == 0 :
            print("Enter amount Greater than Zero")
        
            
        elif amount<0:
            print("Amount must be positive")
        else:
            print("Enter value in correct format")
    i=i+1      

def witdraw_money():
    i= 1
    
    for i in range (3):
        amount = int(input("Enter the Withdrawal amount: "))
        if  amount >0:
            Balance = Balance + amount
            print(f"You are Sucessfully Withdrawed {amount}")
            print("Your Current Balance is: ", Balance)
            withdrawal_time = time
            print(withdrawal_time)
            break
                
        elif amount == 0 :
            print("Enter amount Greater than Zero")
        
            
        elif amount<0:
            print("Amount must be positive")
        else:
            print("Enter value in correct format")
    i=i+1      
def check_balance():
    acc_num = input("Enter your Account Number: ")
    print("Your Account Balance is: ", )

def record_transaction(account_number, transaction_type, amount):
    with open('transactions.txt', 'a') as f:
        f.write(f"{account_number},{transaction_type},{amount},{datetime.datetime.now()}\n")

def transcation_history():
    file = open("transcation.txt", 'r')
    file.read()
    file.close()

def main_menu():
    while True:
        choice = input(" 1. Create Account\n 2. Check Balance\n 3.Deposit Money \n 4.Withdraw Money\n 5.Transaction History\n 6. Exit")
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
            break
        else:
            print("Enter valid choice!!")
        

            
    