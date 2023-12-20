# The task is to create an object factory that allows the creation of objects from various classes (A, B, C)
# depending on the provided object_type argument, and then initialize these objects with specified argument values.
#
# Each of the classes A, B, C has its own constructors with a different number of arguments. The ObjectFactory
# accepts object_type and arguments to create the corresponding object.
#
# Example usage of the factory:
#
# Create an instance of the factory.
# Use the create_object method to create objects with different types (A, B, C) and pass the corresponding arguments.
# Then, access the properties of these objects and display their values on the screen.
# Each class (A, B, C) represents an object with different properties, and the ObjectFactory ensures the creation of
# these objects with various sets of arguments, making the code flexible for creating objects of different
# types with different characteristics.

class A:
    def __init__(self, attr1):
        self.attr1 = attr1


class B:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


class C:
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3


class Factory:
    @staticmethod
    def create_obj(link, *args):
        # if link.__name__ == 'A':
        #     return link(*args)
        # if link.__name__ == 'B':
        #     return B(*args)

        return link(*args)


obj_a = Factory.create_obj(A, "attr A")
obj_b = Factory.create_obj(B, "attr1 B", "attr2 B")
print(obj_a.attr1)
print(obj_b.attr1, obj_b.attr2)
