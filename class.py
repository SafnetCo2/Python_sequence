# and objects
#a blue print to create objects
#object has data(attributes)+methods
#class
#create class with an name
#initialize its attributes with __init__ methods 
#create the methods or function
#initialize it
#access the attributes and methods
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width *self.height
    def perimeter(self):
        return 2*(self.width +self.height)
    
rect= Rectangle(2,4)
print('width:',rect.width)
print('height:',rect.height)
print('area:',rect.area())
print('perimeter:',rect.perimeter())

def fibonacci_sequence(length):
    fibonacci_sequence =[0,1]
    
    while len(fibonacci_sequence)< length:
        next_num =fibonacci_sequence[-1]+ fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    print("Fibonacci sequence")
    for num in fibonacci_sequence:
        print(num, end=" ")
fibonacci_sequence(10)
            
