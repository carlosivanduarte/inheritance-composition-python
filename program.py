# productivity_system = ProductivitySystem()
# payroll_system = PayrollSystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees
# manager = employees[0]
# manager.payroll = HourlyPolicy(55)
# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)
#
# em = Employee(1, 2, 3, 4, 5)

import json

from hr import calculate_payroll, LTDPolicy
from productivity import track
from employees import employee_database, Employee


def print_dict(d):
    print(json.dumps(d, indent=2))


employees = employee_database.employees

sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)

track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print('Temporary Secretary:')
print_dict(temp_secretary.to_dict())
