import sqlite3

details = sqlite3.connect("company.db")  # creating a database

# details.execute('''   Create Table Employees(
#                       EmployeeID Integer Primary Key Autoincrement,
#                       EmployeeName Text,
#                       EmployeeDesingnation Text,
#                       EmployeeSalary Integer,
#                       EmployeeCompanyName Text,
#                       EmployeeMobileNumber Integer
# );     ''')
print("Table Created Successfully")

# get_employeeID = input("Enter Id of an Employee: ")
get_employeeName = input("Enter Employee Name: ")
get_employeeDesig = input("Enter Employee Designation: ")
get_employeeSalary = input("Enter Employee Salary: ")
get_employee_companyName = input("Enter Employee's Company Name: ")
get_employeeMobile = input("Enter Employee's Mobile No: ")

details.execute("Insert Into Employees(EmployeeName, EmployeeDesingnation, EmployeeSalary, EmployeeCompanyName, EmployeeMobileNumber) \
                Values ('"+get_employeeName+"','"+get_employeeDesig+"',"+get_employeeSalary+",'"+get_employee_companyName+"',"+get_employeeMobile+")")
details.commit()
details.close()
print("Inserted Successfully")
