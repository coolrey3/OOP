#python OOP

class Employee:

    raise_amount = 1.04

    def __init__(self,first,last,pay, company, healthcare = "BCBS"):
        self.first = first
        self.last = last
        self.email = first + last + '@' + company + '.com'
        self.pay = pay
        self.company = company
        self.healthcare = healthcare

    def fullname(self):
        return('{} {} '.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


employee_1 = Employee('Ray','Mercedes',65000,'Mite')
employee_1.healthcare = "Humana"
employee_2 = Employee('Mel','Mursuli',60000,'Mite')

#print(employee_2.fullname())

print(Employee.fullname(employee_1))

print(employee_1.pay)
employee_1.apply_raise()
print(employee_1.pay)

print(employee_1.__dict__)
print(employee_2.__dict__)
