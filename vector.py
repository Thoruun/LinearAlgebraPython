from operator import add
from operator import sub
from numbers import Number

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

    def __iter__(self):
        return iter(self.coordinates)

    # def __next__(self):
    #
    #     if self.count == self.coordinates.count:
    #         raise StopIteration
    #
    #     self.count += 1
        # return self.coordinates[self.count - 1]

def add(vc1, vc2):
    print ("ADD VC1 = {}, VC2 = {}".format(vc1, vc2))

    if isinstance(vc1, (int, float)) and isinstance(vc2, (int, float)):
        sumOfNumbers = round(vc1 + vc2, 4)
        print("Returning number {}".format(sumOfNumbers))
        return sumOfNumbers
    else:
        if vc1.dimension != vc2.dimension:
            return 0

    # print (list(map(add, vc1, vc2)))
    return Vector(list(map(add, vc1, vc2)))
    # return [x + y for x, y in zip(vc1, vc2)]

def sub(vc1, vc2):
    print ("SUB VC1 = {}, VC2 = {}".format(vc1, vc2))

    if isinstance(vc1, (int, float)) and isinstance(vc2, (int, float)):
        sumOfNumbers = round(vc1 - vc2, 4)
        print("Returning number {}".format(sumOfNumbers))
        return sumOfNumbers
    else:
        if vc1.dimension != vc2.dimension:
            return 0

    # print (list(map(add, vc1, vc2)))
    return Vector(list(map(sub, vc1, vc2)))

def sclrMult(vc1, scalar):
        print ("SCLR_MULT VC1 = {}, scalar = {}".format(vc1, scalar))

        if isinstance(vc1, (int, float)) and isinstance(scalar, (int, float)):
            sumOfNumbers = round(vc1 * scalar, 4)
            print("Returning number {}".format(sumOfNumbers))
            return sumOfNumbers
        # else:
        #     return 0

        # print (list(map(add, vc1, vc2)))
        return Vector(list(map(sclrMult, vc1, scalar)))
