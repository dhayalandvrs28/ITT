employees = []
def calculate_salary(bp):
   hra = bp*0.20
   da = bp*0.10
   pf = bp*0.12
   gross = bp+hra+da
   net = gross-pf
   return gross,net

def add_employee():
   emp_id = int(input("Employee ID:"))
   for emp in employees:
      if emp["id"] == emp_id:
         print("Employee ID not exist")
         return
   name = input("Name :")
   role = input("Role :")
   bp = float(input("Basic Pay:"))
   gross,net = calculate_salary(bp)
   employees.append({ "id": emp_id,"name":name,"role":role,"bp":bp,"gross":gross,"net":net})
   print("Employee Added Successfully")

def search_employee():
   emp_id = int(input("Employee ID :"))
   for emp in employees:
      if emp["id"]==emp_id:
         print("ID :",emp["id"], "\n Name :", emp["name"],"\n Role :" ,emp["role"], "\n BP :" ,emp["bp"], "\n Gross :", emp["gross"] ,"\n Net :",emp["net"])
         return
      print("Employee Not Found")

def delete_employee():
   emp_id = int(input("Employee ID:"))
   for emp in employees:
      if emp["id"] == emp_id:
         employees.remove(emp)
         print("Employee Deleted")
         return

      print("Employee Not Found")

def view_employees():
   for emp in employees:
      print("ID :",emp["id"], "\n Name :", emp["name"],"\n Role :" ,emp["role"], "\n BP :" ,emp["bp"], "\n Gross :" ,emp["gross"] ,"\n Net :",emp["net"])
      print("-------------------------------------")


while True:
   print("\n 1.Add \n 2.Delete \n 3.View \n 4.Search \n 5.Exit")
   choice = input("Enter your Choice :")

   if choice=="1":
      add_employee()

   elif choice =="2":
      delete_employee()

   elif choice =="3":
      view_employees()

   elif choice =="4":
      search_employee()

   elif choice =="5":
      break

   else:
      print("Invalid Choice")