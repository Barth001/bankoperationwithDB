import random
import database
import validation
balance = 0


def user_status():
    print("Do you have account with us?\n YES, press 1\n NO, press 0")
    user_info = general_integer_validation()
    if user_info == 1:
        login()
    elif user_info == 0:
        register()
    else:
        user_status()


def general_integer_validation():
    try:
        num = int(input(":.."))
        return num
    except ValueError:
        print("It must be an integer value")
        general_integer_validation()


def password_validation():
    try:
        password = int(input("Enter your password( 8 digit number ):.."))
        if len(str(password)) != 8:
            print("Password must be eight digit number")
            password_validation()
        else:
            return password
    except ValueError:
        print("Password must be an integer value")
        password_validation()


def assistance(user):
    print("="*20)
    print("select\n 1, To deposit\n 2, To withdraw\n 3, To check balance\n 4, To quit")
    print("="*20)
    user_input = general_integer_validation()
    if user_input == 1:
        deposit(user)
    elif user_input == 2:
        withdrawal(user)
    elif user_input == 3:
        check_balance(user)
    elif user_input == 4:
        logout()
    else:
        assistance(user)


def deposit(user):
    print("How much do you wish to deposit?")
    amount = general_integer_validation()
    if amount > 99:
        user[-1] = amount
        print("successfully deposited")
        assistance(user)
    else:
        print("Deposit is from 100 dollars and above")
        deposit(user)


def withdrawal(user):
    print("How much do you wish to withdraw")
    amount = general_integer_validation()
    if amount > 1000000:
        print("sorry you can't withdraw more than 1000000 dollars")
        withdrawal(user)
    elif amount >= 100:
        old_balance = user[-1]
        if int(old_balance) >= 100:
            if old_balance >= amount:
                user[-1] = old_balance - amount
                print("successful")
                assistance(user)
            else:
                print("Insufficient fund, please put smaller amount")
                withdrawal(user)
        else:
            print("Insufficient fund, please deposit")
            assistance(user)
    else:
        print("Insufficient fund")
        assistance(user)


def check_balance(user):
    print("You balance is ", user[-1])
    assistance(user)


def account_number_generation():
    account_number = random.randrange(0000000000, 9999999999)
    return account_number


def register():
    print('=' * 10, 'REGISTER', '=' * 10)
    first_name = input("Enter your first name:..")
    last_name = input("Enter your last name:..")
    email = input("Enter your email address:..")
    password = input("Enter your password:..")
    account_number = account_number_generation()
    prepared_user_detail = first_name + ',' + last_name + ',' + email + ',' + password + ',' + str(0)
    is_user_created = database.create(account_number, prepared_user_detail)
    if is_user_created:
        print("Successfully created\nYour account number is ", account_number)
        login()
    else:
        print("Something went wrong, please try again")
        register()


def login():
    print('='*10, 'LOGIN', '='*10)
    account_number_from_user = input("what is your account number:..")
    is_valid_account_number = validation.account_number_validation(account_number_from_user)
    if is_valid_account_number:
        password = input("What is your password:..")
        user = database.authenticated_user(account_number_from_user, password)
        if user:
            print("Welcome ", user[0], user[1])
            assistance(user)
        else:
            print("Invalid account number or password")
            login()
    else:
        print("Account number is invalid")


def logout():
    print("BYE")
    return


user_status()
