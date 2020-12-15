from math import *
import os
import sys
from itertools import combinations

class vector():
    def __init__(self, vector_list): # creating a new vector (initialization)
        self.coordinates  = vector_list

    def __str__(self): # format used to display the vector
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        return vector([a + b for a, b in zip(self.coordinates, v.coordinates)])

    def subtract(self, v):
        return vector([a - b for a, b  in zip(self.coordinates, v.coordinates)])

    def scalar_multiply(self, s):
        return vector([s * a for a in self.coordinates])

    def dot(self, v):
        return sum([a * b for a, b in zip(self.coordinates, v.coordinates)])

    def angle(self, v):
        try:
            return acos(self.dot(v) / (self.magnitude * v.magnitude))
        except ZeroDivisionError:
            raise("tried to divide by zero")

    def magnitude(self):
        return sqrt(sum([a**2 for a in self.coordinates]))

    def unit_vector(self):
        try:
            return vector([a / self.magnitude() for a in self.coordinates])
        except ZeroDivisionError:
            raise("tried to divide by zero")

    def cross(self, v):
        if is_zero(self) or is_zero(v):
            return 0

        if len(self.coordinates) < len(v.coordinates):
            holder1 = extending_vector(v, len(v.coordinates) - len(self.coordinates))
            holder2 = v.coordinates
        elif len(self.coordinates) > len(v.coordinates):
            holder1 = self.coordinates
            holder2 = extending_vector(self, len(self.coordinates) - len(v.coordinates))
        else:
            holder1, holder2 = self.coordinates, v.coordinates

        result = []
        for i in combinations(range(len(holder1))).reverse():
            a, b = i
            result.append((holder1[a] * holder1[b]) - (holder2[a] * holder2[b]))

        return result.reverse()

    def is_zero(self):
        return self.magnitude() == 0

    def extending_vector(v, length):
        return v + [0] * length
        
if __name__ == "__main__":
    """
    on run create a vector
    print out the vector name, if it is a zero vector and print out the unit vector
    """
    vector_list = input("enter the coordinate values for the vector accordingly seperated by a space").split(" ")
    vector_list = [float(i) for i in vector_list]
    u = vector(vector_list)
    print(vector(vector_list))
    print("is vector a zero vector ? " + str(u.is_zero()))
    print("the unit vector" + u.unit_vector())