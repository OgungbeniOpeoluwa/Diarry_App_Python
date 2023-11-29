from diary import DiaryLockException
from diary.diary_ import Diary


def display():
    print("""
    =====================================
    press
    1. Add entry
    2. Unlock diary 
    3. Lock diary
    4. Find Entry by Id
    5. Update Entry
    6. Delete Entry
    7  Read Entry
    press any number to exist====""")

    return input("Enter a number: ")


print(""""
    WELCOME TO MY SECRETE DIARY,KINDLY SET UP YOUR ACCOUNT
    """)
username = input("Enter your username: ")
password = input("Enter your password: ")
print("Setup Successful")
diary = Diary(username, password)


def add_entry():
    title = input("Enter title of entry: ")
    body = input("Enter body of entry: ")
    try:
        diary.create_entry(title, body)
        print("Entry Saved")
        main_menu()
    except ValueError:
        print("Diary is locked,Kindly unlock your diary")
        unlock_diary()


def unlock_diary():
    password = input("Enter your password: ")
    try:
        diary.unlock_diary(password)
        print("Diary unlock")
        main_menu()
    except ValueError:
        print("Invalid pin")
        main_menu()


def lock_diary():
    diary.lock_diary()
    print("Diary Locked")


def find_entry_by_id():
    inputs = input("Enter Entry number: ")
    try:
        entry = diary.find_entry_by_id(inputs)
        print(entry.__str__())
        main_menu()
    except ValueError:
        print("Entry Id doesn't exist")
        add_entry()


def update_entry():
    inputs = input("Enter Entry: ")
    title = input("Enter title: ")
    body = input("Enter Entry body: ")
    try:
        diary.update_entry(inputs, title, body)
        print(diary.find_entry_by_id(inputs).__str__())
        print("Update saved")
        main_menu()
    except ValueError:
        print("Entry doesnt exist")
        add_entry()


def delete_entry():
    inputs = input("Enter Entry number:")
    try:
        diary.delete_entry(inputs)
        print("Deleted successfully")
        main_menu()
    except ValueError:
        print("Entry doesnt exist")
        add_entry()


def exit_app():
    print("you have successfully Logged out")
    exit(4)


def read_diary():
    pin = input("Enter password: ")
    inputs = input("Enter Entry number:")
    try:
        diary.unlock_diary(pin)
        entry = diary.find_entry_by_id(inputs)
        print(entry.__str__())

    except ValueError:
        print("Entry Id doesnt exist")
        main_menu()



def main_menu():
    inputs = display()
    match inputs:
        case '1':
            add_entry()
        case '2':
            unlock_diary()
        case '3':
            lock_diary()
        case '4':
            find_entry_by_id()
        case '5':
            update_entry()
        case '6':
            delete_entry()
        case '7':
            read_diary()
        case _:
            exit_app()


print(main_menu())
