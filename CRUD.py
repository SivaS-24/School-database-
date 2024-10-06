import os
import DB

DB.cursor.execute('''
        INSERT INTO admin (username, password)
        VALUES ('sudo', 'admin')
        ''')
DB.connection.commit()

# Student CRUD Operations

def create_student():
    os.system('cls')
    print("----------------------------------------> Enter Student Details <-------------------------------------------------")
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    sex = input("Enter student's sex(M/F/Other): ")
    clas = input("Enter student's class: ")
    fees = input("Enter student's fees: ")
    rank = int(input("Enter student's rank: "))
    eng_mark = int(input("Enter student's english mark: "))
    python_mark = int(input("Enter student's python mark: "))
    math_mark = int(input("Enter student's maths mark: "))
    class_teacher = input("Enter Class Teacher name: ")
    
    DB.cursor.execute('''
        INSERT INTO students (name, age, sex, class, fees, rank, english_mark, python_mark, math_mark, class_teacher)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, age, sex, clas, fees, rank, eng_mark, python_mark, math_mark, class_teacher))
    
    DB.connection.commit()
    print(f"Student '{name}' added successfully!\n")
    input("press ENTER to continue....")

def read_students():
    os.system('cls')
    DB.cursor.execute('SELECT * FROM students')
    students = DB.cursor.fetchall()
    
    if students:
        print("\n---------------------------------------------> List of Students <--------------------------------------------")
        print("                                                          __________________________")
        print(" ________________________________________________________|            Marks         |________________________ ")
        print("| ID |\t Name\t | Age | Sex | Class | Fees\t | Rank  | English | Python | Maths | Class Teacher\t ")
        print(" ```````````````````````````````````````````````````````````````````````````````````````````````````````````` ")
        for s in students:
            print(f"| {s[0]} | \t{s[1]}\t |  {s[2]} |  {s[3]}  |  {s[4]}    | {s[5]}\t | {s[6]}\t |    {s[7]}   |   {s[8]}   |   {s[9]}  | {s[10]}")
    else:
        print("\nNo students found.")
    
    input("\nPress ENTER to continue....")


def update_student():

    os.system('cls')
    print("\n-----------------------------------------> Update Student Details <--------------------------------------------")
    student_id = int(input("Enter the ID of the student to update: "))
    
    # Check if student exists
    DB.cursor.execute('SELECT * FROM students WHERE sno = ?', (student_id,))

    student = DB.cursor.fetchone()
    
    if student:
        name = input(f"Update name (current: {student[1]}): ") or student[1]
        age = input(f"Update age (current: {student[2]}): ") or student[2]
        sex = input(f"Update sex (current: {student[3]}): ") or student[3]
        clas = input(f"Update class (current: {student[4]}): ") or student[4]
        fees = input(f"Update fees (current: {student[5]}): ") or student[5]
        rank = input(f"Update rank (current: {student[6]}): ") or student[6]
        eng_mrk = input(f"Update english mark (current: {student[7]}): ") or student[7]
        py_mrk = input(f"Update python mark (current: {student[8]}): ") or student[8]
        math_mrk = input(f"Update maths mark (current: {student[9]}): ") or student[9]
        teach = input(f"Update class teacher (current: {student[10]}): ") or student[10]

        DB.cursor.execute('''
            UPDATE students
            SET name = ?, age = ?, sex = ?, class = ?, fees= ?, rank = ?, english_mark = ?, python_mark = ?, math_mark = ?, class_teacher = ?
            WHERE sno = ?
        ''', (name, age, sex, clas, fees, rank, eng_mrk, py_mrk, math_mrk, teach, student_id))
        DB.connection.commit()
        print(f"Student ID {student_id} updated successfully!\n")
    else:
        print(f"No student found with ID {student_id}\n")

    input("\nPress ENTER to continue....")


def delete_student():

    os.system('cls')
    print("\n----------------------------------------------> Delete Student by ID <---------------------------------------------")
    student_id = int(input("Enter the ID of the student to delete: "))
    
    # Check if student exists
    DB.cursor.execute('SELECT * FROM students WHERE sno = ?', (student_id,))
    student = DB.cursor.fetchone()    

    if student:
        choice = input("Are you sure you want to delete Student named: " + student[1] + " (y/n)?")

        if( choice == 'y' or choice == 'Y' ):
            DB.cursor.execute('DELETE FROM students WHERE sno = ?', (student_id,))
            DB.connection.commit()
            print(f"Student ID {student_id} deleted successfully!\n")
        else:
            print(f"Student named: {student[1]} isn't deleted!!!")
    else:
        print(f"No student found with ID {student_id}\n")

    input("press ENTER to continue...")




# CRUD Operation on Teacher

def create_teacher():
    os.system('cls')
    print("----------------------------------------> Enter Teacher Details <-------------------------------------------------")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    sex = input("Enter sex: ")
    salary = int(input("Enter salary: "))
    class_teacher_class = input("Enter Class Teacher\'s class : ")
    
    DB.cursor.execute('''
        INSERT INTO teachers (name, age, sex, salary, class_teacher_class)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, age, sex, salary, class_teacher_class))
    
    DB.connection.commit()
    print(f"Teacher '{name}' added successfully!\n")
    input("press ENTER to continue....")

def read_teacher():
    os.system('cls')
    DB.cursor.execute('SELECT * FROM teachers')
    students = DB.cursor.fetchall()
    if students:
        print("\n---------------------------------------------> List of Teachers <--------------------------------------------")
        print()
        print(" _______________________________________________________")
        print("| ID |\t Name\t | Age | Sex | Salary | Class Teacher Of")
        print(" ```````````````````````````````````````````````````````` ")
        for s in students:
            print(f"| {s[0]} | \t{s[1]}\t |  {s[2]} |  {s[3]}  | {s[4]}\t    | {s[5]}")
    else:
        print("\nNo teacher found...")
    input("\nPress ENTER to continue....")


def update_teacher():

    os.system('cls')
    print("\n-----------------------------------------> Update Teacher Details <--------------------------------------------")
    teacher_id = int(input("Enter the ID of the Teacher: "))
    
    # Check if teacher exists
    DB.cursor.execute('SELECT * FROM teachers WHERE sno = ?', (teacher_id,))

    teacher = DB.cursor.fetchone()
    if teacher:
        name = input(f"Enter new name (current: {teacher[1]}): ") or teacher[1]
        age = input(f"Enter new age (current: {teacher[2]}): ") or teacher[2]
        sex = input(f"Enter new sex (current: {teacher[3]}): ") or teacher[3]
        salary = input(f"Enter new salary (current: {teacher[4]}): ") or teacher[4]
        class_teacher_class = input(f"Enter new Class Teacher of Class (current: {teacher[5]}): ") or teacher[5]

        DB.cursor.execute('''
            UPDATE teachers
            SET name = ?, age = ?, sex = ?, salary = ?, class_teacher_class= ?
            WHERE sno = ?
        ''', (name, age, sex, salary, class_teacher_class, teacher_id))
        DB.connection.commit()
        print(f"Teacher ID {teacher_id} updated successfully!\n")
    else:
        print(f"No teacher found with ID {teacher_id}\n")

    input("\nPress ENTER to continue....")


def delete_teacher():

    os.system('cls')
    print("\n----------------------------------------------> Delete Teacher by ID <---------------------------------------------")
    teacher_id = int(input("Enter the ID of the teacher to delete: "))
    
    # Check if teacher exists
    DB.cursor.execute('SELECT * FROM teachers WHERE sno = ?', (teacher_id,))
    teacher = DB.cursor.fetchone()    

    if teacher:
        choice = input("Are you sure you want to delete teacher named: " + teacher[1] + " (y/n)? ")

        if( choice == 'y' or choice == 'Y' ):
            DB.cursor.execute('DELETE FROM teachers WHERE sno = ?', (teacher_id,))
            DB.connection.commit()
            print(f"Teacher ID-{teacher_id} : Name-{teacher[1]} deleted successfully!\n")
    else:
        print(f"No teacher found with ID {teacher_id}\n")

    input("press ENTER to continue...")



    
# CRUD Operation on Principal

def create_principal():
    os.system('cls')
    print("----------------------------------------> Enter principal Details <-------------------------------------------------")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    sex = input("Enter sex: ")
    salary = int(input("Enter salary: "))
    
    DB.cursor.execute('''
        INSERT INTO principal (name, age, sex, salary)
        VALUES (?, ?, ?, ?)
        ''', (name, age, sex, salary))
    
    DB.connection.commit()
    print(f"Principal '{name}' added successfully!\n")
    input("press ENTER to continue....")

def read_principal():
    os.system('cls')
    DB.cursor.execute('SELECT * FROM principal')
    principal = DB.cursor.fetchall()
    if principal:
        print("\n---------------------------------------------> List of Principal <--------------------------------------------")
        print()
        print(" _______________________________________________________")
        print("| ID |\t Name\t | Age | Sex | Salary ")
        print(" ```````````````````````````````````````````````````````` ")
        for s in principal:
            print(f"| {s[0]} | \t{s[1]}\t |  {s[2]} |  {s[3]}  | {s[4]}")
    else:
        print("\nNo principal found...")
    input("\nPress ENTER to continue....")


def update_principal():

    os.system('cls')
    print("\n-----------------------------------------> Update principal Details <--------------------------------------------")
    principal_id = int(input("Enter the ID of the principal: "))
    
    # Check if principal exists
    DB.cursor.execute('SELECT * FROM principal WHERE sno = ?', (principal_id,))

    principal = DB.cursor.fetchone()
    if principal:
        name = input(f"Update name (current: {principal[1]}): ") or principal[1]
        age = input(f"Update age (current: {principal[2]}): ") or principal[2]
        sex = input(f"Update sex (current: {principal[3]}): ") or principal[3]
        salary = input(f"Update salary (current: {principal[4]}): ") or principal[4]

        DB.cursor.execute('''
            UPDATE principal
            SET name = ?, age = ?, sex = ?, salary = ?
            WHERE sno = ?
        ''', (name, age, sex, salary, principal_id))
        DB.connection.commit()
        print(f"Principal ID {principal_id} updated successfully!\n")
    else:
        print(f"No principal found with ID {principal_id}\n")

    input("\nPress ENTER to continue....")


def delete_principal():

    os.system('cls')
    print("\n----------------------------------------------> Delete Principal by ID <---------------------------------------------")
    principal_id = int(input("Enter the ID of the principal to delete: "))
    
    # Check if principal exists
    DB.cursor.execute('SELECT * FROM principal WHERE sno = ?', (principal_id,))
    principal = DB.cursor.fetchone()    

    if principal:
        choice = input("Are you sure you want to delete principal named: " + principal[1] + " (y/n)? ")

        if( choice == 'y' or choice == 'Y' ):
            DB.cursor.execute('DELETE FROM principal WHERE sno = ?', (principal_id,))
            DB.connection.commit()
            print(f"Principal ID-{principal[0]} : Name-{principal[1]} deleted successfully!\n")
    else:
        print(f"No Principal found with ID {principal_id}\n")

    input("press ENTER to continue...")


    
# CRUD Operation on Admin

def create_admin():
    os.system('cls')
    print("----------------------------------------> Enter Admin Details <-------------------------------------------------")
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    
    DB.cursor.execute('''
        INSERT INTO admin (username, password)
        VALUES (?, ?)
        ''', (user_name, password))
    
    DB.connection.commit()
    print(f"Admin with Username: '{user_name}' added successfully!\n")
    input("press ENTER to continue....")

def read_admin():
    os.system('cls')
    DB.cursor.execute('SELECT * FROM admin')
    admin = DB.cursor.fetchall()
    if admin:
        print("\n---------------------------------------------> List of Admins <--------------------------------------------")
        print()
        print(" ______________________________________")
        print("| ID |\t UserName\t | Password ")
        print(" ``````````````````````````````````````")
        for s in admin:
            print(f"| {s[0]} | \t{s[1]}\t |  {s[2]}")
    else:
        print("\nNo admin found...")
    input("\nPress ENTER to continue....")


def update_admin():

    os.system('cls')
    print("\n-----------------------------------------> Update admin Details <--------------------------------------------")
    aid = int(input("Enter the ID of the admin: "))
    
    # Check if admin exists
    DB.cursor.execute('SELECT * FROM admin WHERE sno = ?', (aid,))

    adm = DB.cursor.fetchone()
    if adm:
        un = input(f"Update Username (current: {adm[1]}): ") or adm[1]
        password = input(f"Update password (current: {adm[2]}): ") or adm[2]

        DB.cursor.execute('''
            UPDATE admin
            SET username = ?, password = ?
            WHERE sno = ?
        ''', (un, password, aid))
        DB.connection.commit()
        print(f"Admin ID {aid} updated successfully!\n")
    else:
        print(f"No Admin found with ID {aid}\n")

    input("\nPress ENTER to continue....")


def delete_admin():

    os.system('cls')
    print("\n----------------------------------------------> Delete Admin by ID <---------------------------------------------")
    aid = int(input("Enter the ID of the Admin to delete: "))
    
    # Check if admin exists
    DB.cursor.execute('SELECT * FROM admin WHERE sno = ?', (aid,))
    admin = DB.cursor.fetchone()    

    if admin:
        choice = input("Are you sure you want to delete admin with username: " + admin[1] + " (y/n)? ")

        if( choice == 'y' or choice == 'Y' ):
            DB.cursor.execute('DELETE FROM admin WHERE sno = ?', (aid,))
            DB.connection.commit()
            print(f"Admin ID ID-{admin[0]} deleted successfully!\n")
    else:
        print(f"No Admin found with ID {aid}\n")

    input("press ENTER to continue...")


def checkAdminCred(un, password):
    DB.cursor.execute('SELECT * FROM admin where username = ? AND password = ?', (un, password))
    admin = DB.cursor.fetchone()

    if admin:
        return True
    else: 
        return False