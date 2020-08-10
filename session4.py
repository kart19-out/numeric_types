import random
import decimal
import math
from decimal import Decimal
class Qualean():

    def __init__(self, number):
        '''Constructor function to build the Qualean object'''
        self.number = number

        if not number in [-1, 0, 1]:
            raise ValueError("You can provide only from these options [-1,0,1]")

        decimal.getcontext().prec = 10
        self.number = Decimal(number) * (Decimal(random.uniform(-1, 1)))

    def __str__(self):
        return 'Qualean Number: {0}'.format(self.number)

    def __repr__(self):
        return 'Qualean Number({0})'.format(self.number)

    def __lt__(self, other):
        if isinstance(other, Qualean):
            return (self.number < other.number)
        else:
            raise NotImplementedError

    def __gt__(self, other):
        if isinstance(other, Qualean):
            return (self.number > other.number)
        else:
            raise NotImplementedError

    def __eq__(self, other):
        if isinstance(other, Qualean):
            return (self.number == other.number)
        else:
            raise NotImplementedError

    def __le__(self, other):
        if isinstance(other, Qualean):
            return (self.number <= other.number)
        else:
            raise NotImplementedError

    def __ge__(self, other):
        if isinstance(other, Qualean):
            return (self.number >= other.number)
        else:
            raise NotImplementedError

    def __float__(self):
        return float(self.number)

    def __invertsign__(self):
        if self.number != 0:
            return (-1) * (self.number)
        else:
            return (self.number)

    def __add__(self, other):
        decimal.getcontext().prec = 10
        if isinstance(other, Qualean):
            return (self.number + other.number)
        else:
            raise NotImplementedError

    def __mul__(self, other):
        decimal.getcontext().prec = 10
        if isinstance(other, Qualean):
            return (self.number * other.number)
        else:
            raise NotImplementedError

    def __bool__(self):
        if self.number:
            return True
        else:
            return False

    def __and__(self, other):
        if isinstance(other, Qualean):
            if self.number:
                return other.__bool__()
            else:
                return False
        else:
            raise NotImplementedError

    def __or__(self, other):
        if isinstance(other, Qualean):
            if self.number:
                return True
            else:
                return other.__bool__()
        else:
            raise NotImplementedError

    def __sqrt__(self):
        if self.number >= 0:
            return (self.number).sqrt()
        else:
            return complex(0, (abs(self.number)).sqrt())