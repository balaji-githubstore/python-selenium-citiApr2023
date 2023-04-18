class Employee:
    company_name = None
    company_location = None

    # constructor - called whenever object is created
    def __init__(self,emp_id=None):
        self.emp_id = emp_id
        self.emp_name = None
        self.emp_salary = None

    @staticmethod
    def app_desc():
        print("Employee Class - handles employee template")

    def print_employee_detail(self):
        print(self.emp_id)
        print(self.emp_name)
        print(50 * "-")

    #get property
    @property
    def get_emp_name(self):
        return str(self.emp_name).upper()