"""For this challenge, you are given two complex numbers, and you have to print the result of their addition,
subtraction, multiplication, division and modulus operations. The real and imaginary precision part should be correct
up to two decimal places. """

import math


class Complex(object):
    def __init__(self, re, im):
        self.im = im
        self.re = re

    def __add__(self, no):
        return Complex(self.re + no.re, self.im + no.im)

    def __sub__(self, no):
        return Complex(self.re - no.re, self.im - no.im)

    def __mul__(self, no):
        return Complex(self.re * no.re - self.im * no.im, self.im * no.re + self.re * no.im)

    def __truediv__(self, no):
        c2_mod2 = float(no.re * no.re + no.im * no.im)
        return Complex((self.re * no.re + self.im * no.im) / c2_mod2,
                       (self.im * no.re - self.re * no.im) / c2_mod2)

    def mod(self):
        return math.sqrt(self.re * self.re + self.im * self.im)

    def __str__(self):
        if self.im == 0:
            result = "%.2f+0.00i" % self.re
        elif self.re == 0:
            if self.im >= 0:
                result = "0.00+%.2fi" % self.im
            else:
                result = "0.00-%.2fi" % (abs(self.im))
        elif self.im > 0:
            result = "%.2f+%.2fi" % (self.re, self.im)
        else:
            result = "%.2f-%.2fi" % (self.re, abs(self.im))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, '%.2f+0.00i' % x.mod(), '%.2f+0.00i' % y.mod()]), sep='\n')
