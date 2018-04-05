


class Employee:

    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_3 = Employee('Ayush', 'Agarwal', 500)
emp_4 = Employee('vivek', 'garg', 1000)


print(emp_3.email)
print(emp_4.email)
print(emp_3.pay)

emp_3.apply_raise()

print(emp_3.pay)

print(Employee.raise_amount)
print(emp_3.raise_amount)
print(emp_3.raise_amount)


print(emp_3.__dict__)

print(Employee.__dict__)

Employee.raise_amount = 1.5
#emp_1 = Employee()
#emp_2 = Employee()

#print(emp_1)
#print(emp_2)


#emp_1.first = 'sumit'
#emp_1.last = 'kedia'

#emp_2.first = 'Amit'
#emp_2.last = 'kedia'


#print(emp_1.first)
#print(emp_2.first)
