# Python program to demonstrate modules
  
  
# Defining a function
def sum(a, b):
    s = a + b
    print("Sum of {a} and {b} is {s}".format(a=a,b=b,s=s))
  
# Defining a variable
location = "Kolkata"
  
# Defining a class
class Employee():
      
    def __init__(self, name, position):
        self. name = name
        self.position = position
          
    def show(self):
        print("Employee name:", self.name)
        print("Employee position:", self.position)