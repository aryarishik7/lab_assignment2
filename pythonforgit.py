#I am using oops to do the assignment
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} - {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def display_table(self):
        for employee in self.employees:
            print(employee)

    def sort_table(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter. Please choose 1, 2, or 3.")

# data as provided by ma'am
employees_data = [
    Employee("161E90", "Ramu", 35, 59000),
    Employee("171E22", "Tejas", 30, 82100),
    Employee("171G55", "Abhi", 25, 100000),
    Employee("152K46", "Jaya", 32, 85000),
]

# object from employeetable
employee_table = EmployeeTable(employees_data)

# input for sorting
sorting_param = int(input("Choose the sorting parameter (1. Age, 2. Name, 3. Salary): "))

# Sorting and displaying the table
employee_table.sort_table(sorting_param)
print("\nSorted Employee Table:")
employee_table.display_table()
