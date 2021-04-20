import os
import validation
path = 'users_data/user_info/'


def create(user_account_number, user_details):
    state = False
    try:
        f = open(path + str(user_account_number) + '.txt', 'w')
    except FileExistsError:
        print("user already exist")
    else:
        f.write(str(user_details))
        state = True
    finally:
        f.close()
        return state


def read(user_account_number):
    is_valid_account_number = validation.account_number_validation(user_account_number)
    try:
        if is_valid_account_number:
            f = open(path + str(user_account_number) + '.txt', 'r')
        else:
            f = open(path + user_account_number, 'r')
    except FileNotFoundError:
        print("user not found")
    except FileExistsError:
        print("user is not in our database")
    except TypeError:
        print("Invalid account number")
    else:
        return f.readline()
    return False


def update(username, new_username, detail):
    path = 'users_data/user_info/' + username + '.txt'
    os.replace(path, new_username)


def delete(account_number):
    state = False
    try:
        os.remove(path + str(account_number) + '.txt')
        state = True
    except FileNotFoundError:
        print("The user isn't in our data base")
    finally:
        return state


def does_email_exist(email):
    all_user = os.listdir(path)
    for user in all_user:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):
    all_user = os.listdir(path)
    for user in all_user:
        if user == str(account_number) + '.txt':
            return True
    return False


def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ',')
        if password == user[3]:
            return user
    return False


# delete(731565433)
# print(read('barth'))
