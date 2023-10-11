#1.
# Declare a class named DataBase that would store the following information:
#
# pk: 1
# title: "Classes and Objects"
# author: "First Name Last Name"
# views: 14356
# comments: 12
#
# Use the same variable names (class attributes) with their corresponding values.

class DataBase:
    pk = 1
    title = "Classes and Objects"
    author = "First Name Last Name"
    views = 14356
    comments = 12

print(DataBase.pk)
print(DataBase.title)




#2.  Declare a class named Goods and define the following attributes (variables) within it:
#
# title: "Ice Cream"
# weight: 154
# type: "Food"
# price: 1024
#
# Then, after declaring the class, change its price attribute to the value 2048 and add one more attribute:
# inflation: 100

class Goods:
    title = "Ice Cream"
    weight = 154
    type = "Food"
    price = 1024
Goods.price = 2048
Goods.inflation = 100

print(Goods.__dict__)


#3.  Declare an empty class named Car. Use the setattr() function to add the following attributes to this class:
#
# model: "Toyota"
# color: "Pink"
# number: "P111UU77"
#
# Print the value of the color attribute to the screen using the dictionary of the Car class.

class Car:
    pass
setattr(Car, 'model', "Toyota")
setattr(Car, 'color', "Pink")
setattr(Car, 'number', "P111UU77")

print(Car.color)




#4. Declare a class named Notes and define the following attributes within it:
#
# uid: 1005435
# title: "Joke"
# author: "J.S. Bach"
# pages: 2
#
# Then, using the getattr() function, read and display the value of the author attribute.

class Notes:
    uid = 1005435
    title = "Joke"
    author = "J.S. Bach"
    pages = 2

aut = getattr(Notes, "author")
print(aut)




#5. Declare a class named Dictionary and define the following attributes within it:
#
# rus: "Питон" (Python in Russian)
# eng: "Python"
#
# Then, using the getattr() function, read and display the value of the rus_word attribute. If such an attribute
# does not exist in the class, the getattr() function should return a boolean value of False.

class Dictionary:
    rus = "Питон"
    eng = "Python"
word_rus = getattr(Dictionary, "rus-word", False)
print(word_rus)

#not to have False:
word_rus = getattr(Dictionary, "rus", False)
print(word_rus)
