from employee_package.employee_module import Employee

Employee.company_name="Citi"
Employee.company_location="Pune"

Employee.company_location="Chennai"


emp1=Employee(101)
emp2=Employee(102)
emp3=Employee(103)
emp4=Employee()

emp1.emp_id=101
emp1.emp_name="john"
emp1.emp_salary=9000

emp2.emp_id=102
emp2.emp_name="saul"
emp2.emp_salary=7000

print(Employee.company_name)
print(emp2.emp_id)


Employee.app_desc()

emp2.print_employee_detail()

emp1.print_employee_detail()

emp3.print_employee_detail()

name=emp1.get_emp_name
print(name)

print(emp1.get_emp_name)
print(emp2.get_emp_name)