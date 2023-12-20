#1
#Declare a class named AbstractClass such that objects of this class cannot be created.
# When the command:

#obj = AbstractClass()
#is executed, the variable obj should refer to a string with the content:
#"Error: cannot create objects of an abstract class"

class AbstractClass:
    def __init__(self):
        raise TypeError("Error: cannot create objects of an abstract class")
obj = AbstractClass()




#2
# In the program, a variable TYPE_OS is declared, and two classes are defined as follows:
# TYPE_OS = 1  # 1 - Windows; 2 - Linux
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
# class DialogLinux:
#     name_class = "DialogLinux"
# It is necessary to declare a third class named Dialog, which would create objects with the command:
#
# dlg = Dialog(<name>)
# Here, <name> is a string that is stored in the local property name of the dlg object.
#
# The Dialog class should create objects of the DialogWindows class if the variable TYPE_OS is equal to 1,
# and objects of the DialogLinux class if the variable TYPE_OS is not equal to 1. Keep in mind that the
# variable TYPE_OS can change in subsequent lines of the program. Consider this when declaring the Dialog class.
TYPE_OS = input("Input 1 or 2 for TYPE_OS: ")
class DialogWindows:
    name_class = "DialogWindows"

class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    def __init__(self, name):
        self.name = name


    def create_objects(self):
        if TYPE_OS == 1:
            return DialogWindows.name_class
        else:
            return DialogLinux.name_class

dlg = Dialog("Hi")

print(dlg.name)
print(dlg.create_objects())


