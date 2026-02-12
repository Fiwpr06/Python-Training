# Composition and Inheritance
class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary

    def display_info(self):
        """Print employee information."""
        print(f"Name: {self.name}, Salary: {self.salary}")
        
    def __repr__(self):
        """Return a string representation of the Employee object."""
        return f"Employee(name={self.name}, salary={self.salary})"

class IT(Employee):
    def __init__(self, name, salary, skills):
        super().__init__(name, salary)
        self.skills = skills

    def display_info(self):
        """Override the display_info method to include skills."""
        super().display_info()
        print(f"Skills: {', '.join(self.skills)}")
        
    def __repr__(self):
        """Return a string representation of the IT object."""
        return f"IT(name={self.name}, salary={self.salary}, skills={self.skills})"

class HR(Employee):
    def __init__(self, name, salary, region):
        super().__init__(name, salary)
        self.region = region

    def display_info(self):
        """Override the display_info method to include region."""
        super().display_info()
        print(f"Region: {self.region}")
        
    def __repr__(self):
        """Return a string representation of the HR object."""
        return f"HR(name={self.name}, salary={self.salary}, region={self.region})"

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = [IT("Bao", 7000, ["Python", "Django"]), HR("Han", 5000, "Vietnam")]

    def add_employee(self, employee):
        """Add an employee to the company."""
        self.employees.append(employee)

    def display_employees(self):
        """Print information of all employees in the company."""
        print(f"Company: {self.name}")
        for emp in self.employees:
            emp.display_info()
            print()

# Delegation
class Warpper:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        """Delegate attribute access to the wrapped object."""
        print(f"Delegating attribute access: {name}")
        return getattr(self._obj, name)

# Multiple Inheritance
class Logger:
    def log(self, message):
        """Log a message."""
        print(f"Log: {message}")

class Mixin(Employee, Logger):
    pass

if __name__ == "__main__":
    company = Company("TechCorp")
    company.display_employees()

    wrapper = Warpper(company)
    wrapper.display_employees()

    mixin_employee = Mixin("Alice", 6000)
    mixin_employee.display_info()
    mixin_employee.log("This is a log message from the mixin employee.")
    