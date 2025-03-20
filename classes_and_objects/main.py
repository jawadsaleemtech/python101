class Employee:
	def __init__(self, ID=None, salary=None, department=None):
		self.ID = ID
		self.salary = salary
		self.department = department
	
	def tax(self):
		return (self.salary * 0.2)
	
	def salaryPerDay(self):
		return (self.salary / 30)
	

Steve = Employee(123,3000,"HR")

print("ID = ",Steve.ID)
print("salary = ",Steve.salary)
print("Department = ",Steve.department)
print("Tax  = ",Steve.tax())
print("Sal per day  = ",Steve.salaryPerDay())