import sys
import CRUD
import DB
import os

# Global variable
isAdmin = False


def show_main_menu():
    os.system('cls')
    print("\n================================== Welcome to School DBMS =================================================")
    print("1. Student Menu")
    print("2. Teacher Menu")
    print("3. Principal Menu")
    print("4. Login As Admin")
    print("5. Admin Menu")
    print("6. Exit")

def show_student_menu():
    global isAdmin
    os.system('cls')
    print("\n--- Welcome to Student Menu ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    match choice:
        case '1': 
            if(isAdmin == True):
                CRUD.create_student()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '2': 
            CRUD.read_students()
        case '3':
            if(isAdmin == True):
                CRUD.update_student()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '4':
            if(isAdmin == True):
                CRUD.delete_student()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '5':             
            print("======= Thanks for using =======")
            sys.exit(0)
        case _:
            input("Please select a valid option!!! Press ENTER to continue...")
            show_student_menu()

def show_teacher_menu():
    global isAdmin
    os.system('cls')
    print("\n---------------------------------> Teacher Menu <------------------------------------")
    print("1. Add Teacher")
    print("2. View All Teachers")
    print("3. Update Teacher by ID")
    print("4. Delete Teacher")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    match choice:
        case '1': 
            if(isAdmin == True):
                CRUD.create_teacher()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '2': 
            CRUD.read_teacher()
        case '3':
            if(isAdmin == True):
                CRUD.update_teacher()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '4':
            if(isAdmin == True):
                CRUD.delete_teacher()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '5':             
            print("============================ Thanks for using ===================================")
            sys.exit(0)
        case _:
            input("Please select a valid option!!! Press ENTER to continue...")
            show_teacher_menu()


def show_principal_menu():
    global isAdmin
    os.system('cls')
    print("\n---------------------------------> Principal Menu <------------------------------------")
    print("1. Add Principal")
    print("2. View All Principal")
    print("3. Update Principal by ID")
    print("4. Delete Principal")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    match choice:
        case '1': 
            if(isAdmin == True):
                CRUD.create_principal()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '2': 
            CRUD.read_principal()
        case '3':
            if(isAdmin == True):
                CRUD.update_principal()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '4':
            if(isAdmin == True):
                CRUD.delete_principal()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '5':             
            print("============================ Thanks for using ===================================")
            sys.exit(0)
        case _:
            input("Please select a valid option!!! Press ENTER to continue...")
            show_principal_menu()

def show_admin_menu():
    global isAdmin
    os.system('cls')
    print("\n---------------------------------> Admin Menu <------------------------------------")
    print("1. Add Admin")
    print("2. View All Admins")
    print("3. Update Admin by ID")
    print("4. Delete Admin")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    match choice:
        case '1': 
            if(isAdmin == True):
                CRUD.create_admin()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '2': 
            if(isAdmin == True):
                CRUD.read_admin()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '3':
            if(isAdmin == True):
                CRUD.update_admin()
            else:
                print('You don\'t have priviledge to perform this operation')
                input("Press Enter to continue...")
        case '4':
            if(isAdmin == True):
                CRUD.delete_admin()
            else:
                print('You don\'t have priviledge to perform this operation')
        case '5':             
            print("============================ Thanks for using ===================================")
            sys.exit(0)
        case _:
            input("Please select a valid option!!! Press ENTER to continue...")
            show_admin_menu()

def authenticate_admin():
    global isAdmin
    os.system('cls')
    print("=========================== Enter Credentials ============================")
    username = input("Enter username: ")
    password = input("Enter Password: ")
    if( CRUD.checkAdminCred(username, password) ):
        isAdmin = True
        return True
    else:
        isAdmin = False
        return False

def main():
    global isAdmin
    while True:
        show_main_menu()
        choice = input("Select an option (1-5): ")

        match choice:
            case '1':
                show_student_menu()
            case '2':
                show_teacher_menu()
            case '3':
                show_principal_menu()
            case '4':
                authenticate_admin()
                if isAdmin:
                    show_main_menu()
                else:
                    input("Invalid Credentials!!! PLease try again... \nPress ENTER to continue...")
            case '5':
                if isAdmin:
                    show_admin_menu()
                else:
                    print("Only Admins can access this page!!!!")
                    input("Press ENTER to continue....")            
            case '6':
                print("======================== Thanks for using =============================")                                
                DB.connection.close()
                sys.exit(0)
            case _:
                input("Please select a valid option!!! Press ENTER to continue...")


# Run the application
if __name__ == "__main__":
    main()