import sqlite3

connection = sqlite3.connect("company.db")

get_employee = input("Enter a EmployeeID to be Updated? ")

get_employeeName = input("Enter Employee New Name: ")
get_employeeDesig = input("Enter Employee New Designation: ")
get_employeeSalary = input("Enter Employee New Salary: ")
get_employee_companyName = input("Enter New Employee's Company Name: ")
get_employeeMobile = input("Enter Employee's New Mobile No: ")

connection.execute("Update Employees \
Set EmployeeName= '"+get_employeeName+"', EmployeeDesingnation= '"+get_employeeDesig+"', EmployeeSalary= "+get_employeeSalary+",\
EmployeeCompanyName= '"+get_employee_companyName+"', EmployeeMobileNumber= "+get_employeeMobile+"" )

result = connection.execute("Select * From Employees")

for i in result:
    print("EmployeeID", i[0])
    print("EmployeeName", i[1])
    print("EmployeeDesingnation", i[2])
    print("EmployeeSalary", i[3])
    print("EmployeeCompanyName", i[4])
    print("EmployeeMobileNumber", i[5])