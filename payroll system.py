
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        pass

class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission):
        super().__init__(emp_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        base_salary = super().calculate_payroll()
        return base_salary + self.commission
# Create a SalaryEmployee
salary_employee = SalaryEmployee(1, 'Maureen', 10000)
print('Salary Employee Payroll:', salary_employee.calculate_payroll())

# Create an HourlyEmployee
hourly_employee = HourlyEmployee(2, 'Maina', 50, 20)
print('Hourly Employee Payroll:', hourly_employee.calculate_payroll())

# Create a CommissionEmployee
commission_employee = CommissionEmployee(3, 'Molly', 2000, 1000)
print('Commission Employee Payroll:', commission_employee.calculate_payroll())
