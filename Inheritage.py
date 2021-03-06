class Employee:
    
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =  first + '.' + last + '@company.com'
    

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lan):
        super().__init__(first, last, pay)
        self.prog_lan = prog_lan

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.empoyees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
              self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())                                     

dev_1 = Developer('Corey', "Schafer", 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 900000, [dev_1])


print(isinstance(mgr_1, Manager))
# print(issubclass(Manager, Employee))
# print(issubclass(Manager, Developer))
# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
  
# print(dev_1.email)
# print(dev_2.prog_lan)

# print(isinstance())

