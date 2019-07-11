'''The feature in Python, that allows same operator to have 
   different meaning according to the context is called operator overloading.
   For example, the + operator will, perform arithmetic addition on two numbers, 
   merge two lists and concatenate two strings.
'''

class Point:

    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

p1=Point(2,3)
p2=Point(-1,2)
p1+p2           # TypeError was raised since python didn't know how to add Point objects together
