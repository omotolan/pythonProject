class Employee:
    first_name = ""
    last_name = ""
    monthly_salary = 0

    def set_first_name(self, f_name):
        self.first_name = f_name

    def set_last_name(self, l_name):
        self.last_name = l_name

    def set_monthly_salary(self, salary):
        self.monthly_salary = salary

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_monthly_salary(self):
        return self.monthly_salary

    def employee_details(self, first_name, second_name, monthly_salary, annual_salary):
        print(f"full name: {first_name}  {second_name}")
        print(f"monthly salary is {monthly_salary}")
        print(f"annual salary is {annual_salary}")


employee_one = Employee()


def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
monthly_salary = int(input("Enter monthly salary: "))

employee_one.set_first_name(first_name)
employee_one.set_last_name(last_name)
employee_one.set_monthly_salary(monthly_salary)

annual_salary = calculate_annual_salary(employee_one.get_monthly_salary())

print(employee_one.__dict__)
print(f"annual salary is {annual_salary}")
employee_one.employee_details()