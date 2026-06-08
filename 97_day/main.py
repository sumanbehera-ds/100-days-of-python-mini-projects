# Employee Salary System With Inheritance
class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Base Salary:", self.base_salary)


class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, bonus):
        super().__init__(name, employee_id, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

    def display_details(self):
        super().display_details()
        print("Bonus:", self.bonus)
        print("Total Salary:", self.calculate_salary())


developer = Developer("Suman", "DEV101", 40000, 10000)
developer.display_details()