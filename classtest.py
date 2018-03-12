

class employee:
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first.lower() + '.' + last.lower() + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.last)


emp1 = employee('Kelvin', 'Thomas', 100000)
emp2 = employee('Andrew', 'Stover', 80000)

print(emp1.email)
print(emp2.email)

print(emp1.fullname())

