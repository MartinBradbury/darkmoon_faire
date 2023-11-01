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


user = SHEET.worksheet('user')

data = user.get_all_values()

def create_user():
    """
    Create a username and password and store in google sheets
    """
    print("Welcome, would you like to:")
    print("[1] Login: ")
    print("[2] Create Account: ")
    print("Please select [1] or [2]")
    selection = input(": ")
    while selection != int(1):
        print(f"you selected {selection}")
        if selection == '1':
            print("create account")
            break
        if selection == '2':
            print("login")
            break        
        else:
            print("please select 1 or 2")
            selection = input(": ")
            



create_user()
