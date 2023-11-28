#Declare the following classes in the program:
#
# CPU - a class for describing processors.
# Memory - a class for describing memory.
# MotherBoard - a class for describing motherboards.
#
# Provide the ability to create objects of each class with the following commands:
#
# cpu = CPU(name, clock_frequency)
# mem = Memory(name, size)
# mb = MotherBoard(name, cpu, memory1, memory2, ..., memoryN)
#
# Note that when creating an object of the MotherBoard class, you can pass multiple objects of the Memory class,
# up to a maximum of N, which is the number of memory slots on the motherboard (N = 4).
#
# The objects of the classes should have the following instance properties:
#
# For the CPU class: name - the name; fr - clock frequency.
# For the Memory class: name - the name; volume - memory size.
# For the MotherBoard class: name - the name; cpu - a reference to an object of the CPU class;
# total_mem_slots = 4 - the total number of memory slots (this attribute is initialized with this value and does
# not change); mem_slots - a list of objects of the Memory class (up to a maximum of total_mem_slots = 4 objects,
# corresponding to the maximum number of memory slots).
#
# The MotherBoard class should have a method get_config(self) to return the current configuration of components on
# the motherboard in the following format as a list of four strings:
#
# ['Motherboard: <name>',
# 'Central Processor: <name>, <clock speed>',
# 'Memory Slots: <total number of memory slots>',
# 'Memory: <name_1> - <size_1>; <name_2> - <size_2>; ...; <name_N> - <size_N>']
#
# Create an object mb of the MotherBoard class with one CPU (an object of the CPU class) and two memory slots (objects
# of the Memory class).

##1.
# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
# class MotherBoard:
#     def __init__(self, name, cpu:CPU, memory_slots:list[Memory], total_mem_slots=4):
#         self.name = name
#         self.cpu = cpu
#         self.memory_slots = memory_slots
#         self.total_mem_slots = total_mem_slots
#     def get_config(self):
#         return [
#             f"Motherboard: {self.name}",
#             f"Central Processor: {self.cpu.name}, {self.cpu.fr}",
#             f"Memory Slots: {self.total_mem_slots}",
#             f"Memory: {self.decompose_list()}"
#         ]
#
#     def decompose_list(self):
#         return [f" Name: {memory.name}, Volume: {memory.volume}"for memory in self.memory_slots]
#
# cpu = CPU('Intel 17', '2.4Hz')
# mem1 = Memory('Kingstone', '4Gb')
# mem2 = Memory('Kingstone', '6Gb')
# memories = [mem1, mem2]
# mb = MotherBoard('Asus', cpu, memories)
# print(*mb.get_config(), sep="\n")



##2.
class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr
class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
class MotherBoard:
    def __init__(self, name, cpu:CPU, memory_slots:list[Memory], total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.memory_slots = memory_slots
        self.total_mem_slots = total_mem_slots
    def get_config(self):
        return [
            f"Motherboard: {self.name}",
            f"Central Processor: {self.cpu.name}, {self.cpu.fr}",
            f"Memory Slots: {self.total_mem_slots}",
            f"Memory: {self.decompose_list()}"
        ]



    def decompose_list(self):
        return [f" Name: {memory.name}, Volume: {memory.volume}"for memory in self.memory_slots]

cpu = CPU('Intel 17', '2.4Hz')
mem1 = Memory('Kingstone', '4Gb')
mem2 = Memory('Kingstone', '6Gb')
memories = [mem1, mem2]
mb = MotherBoard('Asus', cpu, memories)
print(*mb.get_config(), sep="\n")

