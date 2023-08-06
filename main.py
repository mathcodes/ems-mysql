# Employee Management System using MySQL with Python

from os import system # this is to execute the system commands
import re # this is for regular expressions
import mysql.connector # this is for MySQL database connection

# making a connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "employee"
)

# Function to Add_Employee
def Add_Employee():
    print("{:>60}".format("Enter Employee Details"))



# FIRST EXECUTION
# # Create Database
# mycursor = mydb.cursor()
# mycursor.execute("""
#                  CREATE TABLE employee (Id INT(11) PRIMARY KEY,
#                  Name VARCHAR(1000),
#                  Email_Id TEXT(1000),
#                  Phone_no INT(11),
#                  Address TEXT(1000),
#                  Post TEXT(1000),
#                  Salary BIGINT(20))
#                  """)

# Menu Function to display menu
def menu():
    system("cls") # this is to clear the screen
    print("{:^80}".format("Employee Management System")) # here the {:^80} is used to print the text in the center of 80 spaces
    print("{:>60}".format("Menu")) # Here the {:>60} is used to print the text in the right of 60 spaces
    print("{:>60}".format("1. Add Employee"))
    print("{:>60}".format("2. Display Employee and Record"))
    print("{:>60}".format("3. Update Employee Record"))
    print("{:>60}".format("4. Promote Employee"))
    print("{:>60}".format("5. Remove Employee and Record"))
    print("{:>60}".format("6. Search For Employee"))
    print("{:>60}".format("7. Exit\n"))
    print("{:>60}".format("Enter your choice: 1, 2, 3, 4, 5, 6 or 7?"))

    choice = int(input("Enter your choice: "))
    if (choice == 1):
        system("cls")
        Add_Employee()
    else:
        print("Wrong Choice.... Try Again")
        press = input("Press any key to continue...")
        menu()

menu() # calling menu function

# Function to Add_Employee
def Add_Employee():
    print("{>:60}".format("Enter Employee Details"))
    id = input("Enter Employee ID: ")
    # Check it id exists
    if (check_employee(id)  == True):
        print("Employee ID already exists \n Try another ID please...")
        press = input("Press any key to continue...")
        menu()
    Name = input("Enter Employee Name: ")
    # Check if name is valid
    if (check_name(Name) == True):
        print("Employee NAME already exists \n Try again...")
        press = input("Press any key to continue...")
        Add_Employee()
    Email_Id = input("Enter Employee Email ID: ")
    if(re.fullmatch(regex, Email_Id)):
      print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press any key to continue...")
        Add_Employee()
    Phone_No = input("Enter Employee Phone Number: ")
    if(re.fullmatch(regex1, Phone_No)):
      print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press any key to continue...")
        Add_Employee()
    Address = input("Enter Employee Address: ")
    # Check if address is valid
    if (check_address(Address) == True):
        print("Employee ADDRESS already exists \n Try again...")
        press = input("Press any key to continue...")
        Add_Employee()
    Salary = input("Enter Employee Salary: ")
    # Check if salary is valid
    if (check_salary(Salary) == True):
        print("Employee SALARY already exists \n Try again...")
        press = input("Press any key to continue...")
        Add_Employee()
    # Inserting data into table
    mycursor = mydb.cursor()
    sql = "INSERT INTO employee (id, Name, Email_Id, Phone_No, Address, Salary) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id, Name, Email_Id, Phone_No, Address, Salary)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    press = input("Press any key to continue...")
    menu()

# Function to View_Employee

