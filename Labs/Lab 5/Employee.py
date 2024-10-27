class Employee:
    def __init__(self,name: str,id:int,departement:str) -> None:
        self.name=name
        self.id=id
        self.departement=departement
    
    def assign_departement(self,new_departement:str) -> None:
        self.departement=new_departement
    
    def print_employee_details(self):
        print(f"The Employee's name is {self.name}, their ID number is {self.id}, and their departement is {self.departement}")
        
    def calculate_emp_salary(self,salary:int,hours_worked:int) -> int:
        return salary*hours_worked
    
    def get_departement(self):
        return self.departement
    
    


x= Employee("Josh",3,"Sales")

(x.print_employee_details())
(x.assign_departement("Math"))
print(x.get_departement())
print(x.calculate_emp_salary(15,200))