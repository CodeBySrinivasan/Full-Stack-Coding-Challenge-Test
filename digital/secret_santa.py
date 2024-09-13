import random

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.secret_child = None

class SecretSantaManager:
    def __init__(self, employees, previous_assignments):
        self.employees = [Employee(name=emp['Employee_Name'], email=emp['Employee_EmailID']) for emp in employees]
        self.previous_assignments = previous_assignments

    def assign_secret_children(self):
        # Shuffle the list of employees
        shuffled_employees = self.employees[:]
        random.shuffle(shuffled_employees)
        
        for i, employee in enumerate(self.employees):
            # Ensure that the employee is not assigned to themselves
            possible_choices = [e for e in shuffled_employees if e != employee]
            
            # Ensure that the employee doesn't get the same secret child as last year
            if employee.name in self.previous_assignments:
                previous_secret_child = self.previous_assignments[employee.name]
                possible_choices = [e for e in possible_choices if e.name != previous_secret_child]
            
            if not possible_choices:
                raise ValueError("No valid assignments available. Check your input data.")
            
            # Assign a secret child
            chosen_child = random.choice(possible_choices)
            employee.secret_child = chosen_child
            shuffled_employees.remove(chosen_child)
