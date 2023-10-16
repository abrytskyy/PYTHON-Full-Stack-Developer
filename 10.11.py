#Task 1:
# Declare a class named TravelBlog and declare an attribute in it:
# total_blogs: 0
# Create an instance of this class named tb1 and create two local properties in it:
# name: 'France'
# days: 6
# Increase the value of the total_blogs attribute of the TravelBlog class by one.
# Create another instance of the TravelBlog class named tb2 and create two local properties in it:
# name: 'Italy'
# days: 5
# Increase the value of the total_blogs attribute of the TravelBlog class by one.

class TravelBlog:
    total_blogs = 0

tb1 = TravelBlog()
tb1.name = 'France'
tb1.days = 6

TravelBlog.total_blogs += 1

tb2 = TravelBlog()
setattr(tb2,"name", "Italy")
setattr(tb2, "days", 5)

TravelBlog.total_blogs += 1

print(TravelBlog.__dict__)
print(tb1.__dict__)
print(tb2.__dict__)

# Task 2:
# Declare a class named Figure with two attributes:
# type_fig: 'ellipse'
# color: 'red'
# Create an instance of this class named fig1 and add the following local attributes to it:
# start_pt: (10, 5)
# end_pt: (100, 20)
# color: 'blue'
# Remove the color property from the class instance and display a list of all local properties (without values)
# of the fig1 object in one line separated by spaces, in the order specified in the task.

class Figure:
    type_fig = 'ellipse'
    color = 'red'

fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

del fig1.color
print(fig1.__dict__)



# Task 3:
# Declare a class named Person with attributes:
# name: 'First Last'
# job: 'Programmer'
# city: 'City'
# Create an instance named p1 of this class and check if it has a local property with the name 'job'. Print True if
# it is present in the p1 object and False if it is absent.

class Person:
    name = 'First Last'
    job = 'Programmer'
    city = 'City'

p1 = Person()

print(hasattr(p1,'job'))



# Task 4:
# Task 1:
# Declare a class named Student and declare an attribute in it:
# total_students: 0
# Create an instance of this class named student1 and create two local properties in it:
# name: 'Ivan'
# age: 20
# Increase the value of the total_students attribute of the Student class by one.

class Student:
    total_students = 0

student1 = Student()
student1.name = 'Ivan'
setattr(student1, "age", 20)

Student.total_students += 1

# print all class:
print(Student.__dict__)
#print student1:
print(student1.__dict__)
#check available properties(attributes):
print(hasattr(student1, "name"))
#get available properties(attributes)
print(getattr(student1, "name", False))
#delete attribute:
delattr(student1, "name")
print(hasattr(student1, "name"))
print(getattr(student1, "name", False))
# print Student:
print(getattr(Student, "total_students", False))



# Task 5:
# Define a class named Dog and declare an attribute in it:
# total_dogs: 0
# Create an instance of the class named dog1 and set two local properties:
# name: 'Baron'
# age: 3
# Increase the value of the total_dogs attribute of the Dog class by one.

class Dog:
    total_dogs = 0

dog1 = Dog()
dog1.name = 'Baron'
dog1.age = 3

Dog.total_dogs += 1

print(Dog.total_dogs)
print(getattr(Dog, "total_dogs", False))
print(getattr(dog1, "name", False))
print(hasattr(Dog, "total_dogs"))
print(hasattr(dog1, "total_dogs"))
print(getattr(dog1, "total_dogs", False))
print(dog1.__dict__)
#change to 16:
dog1.total_dogs = 8
print(dog1.__dict__)
print(Dog.__dict__)
#delete local:
del dog1.age
print(dog1.__dict__)
# delattr(dog1, "total_dogs")
# print(dog1.__dict__)
# print(Dog.__dict__)

#comment 3 lines and run again with 3 lines down:
delattr(Dog, "total_dogs")  #same   #del Dog.total_dogs
print(dog1.__dict__)
print(Dog.__dict__)
