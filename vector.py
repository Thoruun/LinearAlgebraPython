from operator import add
from operator import sub
from numbers import Number
import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.count = 0

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __getitem__(self,index):
        return self.coordinates[index]

    def __setitem__(self,index,value):
        self.coordinates[index] = value

    def __iter__(self):
        return iter(self.coordinates)

    # def __next__(self):
    #
    #     if self.count == self.coordinates.count:
    #         raise StopIteration
    #
    #     self.count += 1
        # return self.coordinates[self.count - 1]

    def magnitude(self):
        magnitude = 0
        if self.dimension == 0:
            return magnitude
        else:
            sum = 0
            for coord in self:
                sum = sum + pow(coord, 2)

            magnitude = math.sqrt(sum)
            magnitude = magnitude
            print ("MAGNITUDE OF {}, is {}".format(self, magnitude))
            return magnitude

    def direction(self):
        unitVector = []
        magnitude = self.magnitude()

        for i in range(self.dimension):
            unitVector.insert(i - 1, self[i - 1] / magnitude)

        return unitVector

def add(vc1, vc2):
    print ("ADD VC1 = {}, VC2 = {}".format(vc1, vc2))

    if isinstance(vc1, (int, float)) and isinstance(vc2, (int, float)):
        sumOfNumbers = vc1 + vc2
        print("Returning number {}".format(sumOfNumbers))
        return sumOfNumbers
    else:
        if vc1.dimension != vc2.dimension:
            return 0

    return Vector(list(map(add, vc1, vc2)))

def sub(vc1, vc2):
    print ("SUB VC1 = {}, VC2 = {}".format(vc1, vc2))

    if isinstance(vc1, (int, float)) and isinstance(vc2, (int, float)):
        sumOfNumbers = vc1 - vc2
        print("Returning number {}".format(sumOfNumbers))
        return sumOfNumbers
    else:
        if vc1.dimension != vc2.dimension:
            return 0

    return Vector(list(map(sub, vc1, vc2)))

def sclrMult(vc1, scalar):
    print ("SCLR_MULT VC1 = {}, scalar = {}".format(vc1, scalar))

    if isinstance(vc1, (int, float)) and isinstance(scalar, (int, float)):
        sumOfNumbers = vc1 * scalar
        print("Returning number {}".format(sumOfNumbers))
        return sumOfNumbers

    multVector = []
    for i in range(vc1.dimension):
        if scalar > 0:
            multVector.insert(i - 1, vc1[i - 1] * scalar)

    return multVector

def dotProduct(vc1, vc2):
    if vc1.dimension != vc2.dimension:
        return IndexError

    dotProduct = 0
    for i in range(vc1.dimension):
        dotProduct += vc1[i] * vc2[i]

    return dotProduct

def angleBetween(vc1, vc2, inRadians):
    if vc1.dimension != vc2.dimension:
        return IndexError

    angle = dotProduct(vc1, vc2) / (vc1.magnitude() * vc2.magnitude())
    print("cos (θ) = {}".format(angle))
    angle = math.acos(angle)
    if inRadians == False:
        angle = math.degrees(angle)

    return angle
