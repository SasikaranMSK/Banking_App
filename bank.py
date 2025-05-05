import datetime
time = datetime.datetime.now()
def create_acc():
    username = input("Create a user Name: ")
    password = input("Create a password: ")
    file = open("users.txt", 'a')
    
    file.write(f"{username}:{password}\n")
    file.close()

#create_acc()

def user_details():
    acc_num = input("Enter your account number: ")
    address = input("Enter your Address: ")
    phone_nu = input("Enter your phone number: ")
    customer_file = open('customers.txt', 'a')
    customer_file.write[f"{acc_num},{address},{phone_nu}\n"]
# user_details()

def login():
    
    file = open("admin_users.txt", 'a')
    file.write[f"admin,admin123\n"]
    choice = input("Enter Prefered Number to Enter \n 1. Admin\n 2. Normal User\n")
    if choice == "1":
        admins = open('admin_users.txt', 'r')
        users = admins.readlines()
        for admin in admins:
            admin_username =input("Enter Admin User Name: ")
            admin_password = input("Enter Admin Password: ")
            default_username, default_Password = admin[0].strip().split(":")
            if default_username == admin_username and default_Password == admin_password:
                print("You are sucessfully Logined!")
            else:
                print("Enter valid credentials!!")
    elif choice == "2":
        file = open('users.txt', 'r')
        file.read()
        users = file.readlines()
        for user in users:
            username = input("Enter your user Name: ")
            Password = input("Enter your password: ")
            saved_username, saved_Password = user.strip().split(":")
            if username == saved_username and Password == saved_Password:
                menu()
            else:
                print("Enter correct crdentials!")

login()
        
        
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
def transcation_history():
    file = open("transcation.txt", 'r')
    file.read()
    file.close()
def menu():
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
        

            
    