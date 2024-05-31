# ## Creating Class
# class Student:
#     name = 'karan'

# ## Creating Object (instance / or instances of object)    
# s1 = Student()
# print(s1)
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car:
#     color = 'blue'
#     brand = 'mercedes'
    
# car1 = Car()
# print(car1.color)
# print(car1.brand)

## Constructors
# class Student:
#     college_name = "ABC College"
#     name = "anonymous" # Class Attributes

#     #default Constructors
#     def __init__(self):
#         pass
    
#     #parameterized constructors
#     def __init__(self, fullname, marks): # self is pointing towards s1 object
#         self.name = fullname # name is attributes
#         self.marks = marks
#         print(self)
#         print("Adding new Student in Database...")
    
# s1 = Student('karan', 97)
# print(s1.name, s1.marks)

# s2 = Student('Arjun', 88)
# print(s2.name, s2.marks)
# print(s2.college_name)
# print(Student.college_name)

# s3 = Student('', 58)
# print(s3.name, s3.marks)

## Methods
# class Student:
#     college_name = "ABC College"
    
#     #parameterized constructors
#     def __init__(self, fullname, marks): # self is pointing towards s1 object
#         self.name = fullname # name is attributes
#         self.marks = marks
        
#     def welcome(self):
#         print("Welcome Student,", self.name)
        
#     def get_marks(self):
#         return self.marks

    
# s1 = Student('karan', 97)
# s1.welcome()
# print(s1.get_marks())


### EXERCISE-> Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your AVG. score is:", sum/len(self.marks))
            
        
s1 = Student('Tony Stark', [99, 98, 97])
s1.get_avg()

s1.name = 'Ironman'
s1.get_avg()