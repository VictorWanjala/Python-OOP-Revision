class Employee:
    raise_amt = 1.04
    def __init__(self, first,last, pay, email):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = email


    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay
    
class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first,last, pay, email, prog_lang):
        super().__init__(first,last, pay, email)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first,last, pay, email, employees=None):
        super().__init__(first,last, pay, email)
        if  employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp  not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_emp(self):
        for emp in self.employees:
            print(emp.fullname())

    

    



dev_1 = Developer('Victor', 'Wanjala',120000, 'test@gmail.com','Python')
dev_2 = Developer('Jon', 'Doe', 100000, 'h@gmail.com', 'Java')

mgrA = Manager('Sue', 'Smith', 150000,'mgr@gmail.com', [dev_1])
print(mgrA.email)
mgrA.add_emp(dev_2)
mgrA.remove_emp(dev_1)
mgrA.list_emp()

print(dev_1.prog_lang)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)








