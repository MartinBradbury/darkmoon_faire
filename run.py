# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('data')










def main():
    """
    Create a username and password and store in google sheets
    """
    print("Welcome, would you like to:")
    print("[1] Login: ")
    print("[2] Create Account: ")
    print("Please select [1] or [2]")
    selection = input(": ")
    while selection != int():
        if selection == '1':
            print("create account")
            break
        if selection == '2':
            print("login")
            break        
        else:
            print("please select 1 or 2")
            selection = input(": ")





def get_data():
    """
    Get Username and password data
    """
    while True:
        print("please enter your username")

        data_str = input("username: ")
        username = data_str
        validate_data(username)

        if validate_data(username):
            print("data is valid")
            break
    return username

def get_password():
    """
    get password
    """
    while True:
        print("please enter your password")
        data_pw = input("password: ")
        password = data_pw
        validate_data(password)
        if validate_data(password):
            print("password is valid")
            break
    return password

def validate_data(values):
    """
    Vaidate username with google sheets and if true move on to
    password. If false it will raise a valueerror
    """
    try:
        [str(value) for value in values]
        if len(values) == 0:
            raise ValueError(f"Please type your username")
    

    except ValueError as e:
        print(f"invalid data as{e}, please try again.")
        return False

    return True


def update_username(data):
    """
    update username on the google sheet
    """
    print("Updating Username....\n")
    username_worksheet = SHEET.worksheet('username')
    username_worksheet.append_row(data)
    print("Username accepted")


def update_password(pw):
    """
    update password
    """
    print("updating password....\n")
    password_worksheet = SHEET.worksheet('password')
    password_worksheet.append_row(pw)
    print("password accepted")



data = get_data()
pw = get_password()
get_data = [str(value) for value in data]
get_password = [str(value) for value in pw]
update_username(get_data)
update_password(get_password)


print(get_data)

#validate data for username with try and if etc