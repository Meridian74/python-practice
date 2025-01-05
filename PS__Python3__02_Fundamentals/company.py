from employee import Employee


class Company:
   def __init__(self):
      self.employees = []

   def add_employee(self, new_employee):
      self.employees.append(new_employee)

   def display_employee(self):
      print("Current employees:")   
      print("------------------")  
      for employee in self.employees:
         print (employee.first_name, employee.last_name)

   def pay_employees(self):
      print("Paying empoloyees:")
      print("------------------")
      for employee in self.employees:
         print("Paycheck for:", employee.first_name, employee.last_name)
         print(f"Amount: ${employee.calculate_paycheck():,.2f}")
         print("--------------------------")


def main():
   my_company = Company()
   employee1 = Employee('Sarah', 'Hess', 50000)
   my_company.add_employee(employee1)
   employee2 = Employee('Lee', 'Smith', 25000)
   my_company.add_employee(employee2)
   employee3 = Employee('Bob', 'Brown', 60000)
   my_company.add_employee(employee3)
   
   my_company.display_employee()
   my_company.pay_employees()


main()