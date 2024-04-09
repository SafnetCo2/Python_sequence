def print_fibonacci(length):
    fibonacci_sequence=[0,1]
    while len(fibonacci_sequence)<length:
        next_num=fibonacci_sequence[-1]+fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    print('Fibonacci sequence')
    for num in fibonacci_sequence:
        print(num, end=" ")
print_fibonacci(10)

class Employee:
    def __init__(self, name, emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def salary_update(self,new_salary):
        self.salary = new_salary
    def get_details(self):
        return f"The new employee {self.name} identification {self.emp_id} earns {self.salary}"
emp=Employee("John ","Eml001", 60000)
print(emp.get_details())
emp.salary_update(65000)
print(emp.get_details())
        

    