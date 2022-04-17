"""
ABC is a right triangle, 90 at B. Therefore, <ABC=90.
Point M is the midpoint of hypotenuse AC. You are given the lengths AB and BC.
Your task is to find (angle , as shown in the figure) in degrees.
"""
import math

AB = int(input())
BC = int(input())

# find the sides of the triangle using trigonometry
AC = math.sqrt(AB ** 2 + BC ** 2)
M = AC / 2
BC = BC / 2

# calculate the angle using SOHCAHTOA
angle = round(math.degrees(math.acos(BC / M)))
print(f"{angle}\N{DEGREE SIGN}")
