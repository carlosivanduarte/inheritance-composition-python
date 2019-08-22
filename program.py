from hr import PayrollSystem, HourlyPolicy
from productivity import ProductivitySystem
from employees import EmployeeDatabase, Employee

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
from employees import EmployeeDatabase


def print_dict(d):
    print(json.dumps(d, indent=2))


for employee in EmployeeDatabase().employees:
    print_dict(employee.to_dict())
