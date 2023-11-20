#1. There is the following class for reading information from the input stream:
#
# import sys
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # reading a list of strings from the input stream
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
# Which can then be used as follows:
#
# sr = StreamReader()
# data, result = sr.readlines()
# Before the StreamReader class, it is necessary to declare another class StreamData with a method:
#
# class StreamData:
#     def create(self, fields, lst_values): ...
# This method, when given a tuple FIELDS of local attribute names (passed to the fields attribute) and a list of
# strings lst_in (passed to the lst_values attribute), should form local properties in the StreamData class with names
# of fields from fields and corresponding values from lst_values.
#
# If the creation of local properties is successful, the create() method returns True; otherwise, it returns False. If
# the number of fields and the number of strings do not match, the create() method returns False, and local attributes
# do not need to be created.
#
# P.S. In the program, it is necessary to additionally declare only the StreamData class. Nothing else needs to be done.
#
# Example input information (Sample Input):
#
# 10
# Python - Mastering Basics
# 512

import sys

class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        else:
            for pair in zip(fields, lst_values):
                setattr(self, pair[0], pair[1])
            return True

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # reading a list of strings from the input stream
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

sr = StreamReader()
data, result = sr.readlines()
print(data.__dict__, result)

#to execute: type run, 1+enter, Python+enter, 30+enter, ctrl+D




#2. Declare a class named MediaPlayer with two methods:
#
# open(file) - to open a media file with the name file (creates a local property filename with the value of the file
# argument in the MediaPlayer class object).
# play() - to play the media file (prints the string "Playback <media file name>" to the screen).
#
# Create two instances of this class with the names: media1 and media2. Call the open() method with the argument
# "filemedia1" for the media1 object and "filemedia2" for the media2 object. After that, call the play() method through
# the objects. In this case, two strings should be displayed on the screen (without quotes):
#
# "Playback filemedia1"
# "Playback filemedia2"

class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Playback {self.filename}")

media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open("filemedia1")
media2.open("filemedia2")
media1.play()
media2.play()




#3. Declare a class named Graph with the following methods:

# set_data(data) - passing a dataset data for subsequent display (data is a list of numerical data);
# draw() - displaying the data (in the same order as in the data list)
#
# and an attribute:
#
# LIMIT_Y = [0, 10]
#
# The set_data() method should create a local property data of the Graph class object. The data attribute should
# reference the list passed to the method. The draw() method should print to the screen a string of numbers separated
# by spaces and belonging to the specified range of the LIMIT_Y attribute (inclusive).
#
# Create an object graph_1 of the Graph class, call its set_data() method, and pass the list:
#
# [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
#
# Then, call the draw() method through the graph_1 object. A string with the corresponding set of numbers, separated by
# spaces, should appear on the screen. For example (output without quotes):
#
# "10 0 2 5 7"

class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        filtered = filter(lambda x: self.LIMIT_Y[0]<= x <= self.LIMIT_Y[1], self.data)
        print(" ".join(map(str, filtered)))

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()




#4.  Declare a class Point so that objects of this class can be created with the commands:
#
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')
# Here, the first two values are the coordinates of the point on the plane (local properties x, y), and the third
# optional argument is the color of the point (local property color). If the color is not specified, it
# defaults to black.
#
# Create a thousand such objects with coordinates (1, 1), (3, 3), (5, 5), ... that is, with an increase of two for
# each new point. Place each object in the points list (in order). Specify the color 'yellow' for the second object in
# the points list.

class Point:
    def __init__(self, x, y, color = 'black'):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"X:{self.x} Y: {self.y} Color: {self.color}\n"

points = [Point(i, i, "yellow") if i==3 else Point(i, i) for i in range(1, 2000, 2)]
print(*points)




#5. Declare a class Money so that objects of this class can be created as follows:
#
# my_money = Money(100)
# your_money = Money(1000)
# Here, when creating objects, the amount of money to be stored in the local property (attribute) money of each
# instance of the Money class is specified.

class Money:
    def __init__(self, money):
        self.money = money

    def __str__(self):
        return f"Amount: {self.money}"


my_money = Money(100)
print(my_money.__dict__) # without __str__
print(my_money)
your_money = Money(1000)
print(your_money)

