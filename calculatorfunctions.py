import math




class functions:
    def add(a, b):
        return print(f"The sum of {a} and {b} is {a + b}")
    def subtract(a, b):
        return print(f"The difference of {a} and {b} is {a - b}")
    def multiply(a, b):
        return print(f"The product of {a} and {b} is {a * b}")
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return print(f"The quotient of {a} and {b} is {a / b}")
    def power(a):
        return print(f"The square of {a} is {math.pow(a, 2)}")
    def power_add(a, b):
        return print(f"The sum of squares of {a} and {b} is {math.pow(a, 2) + math.pow(b, 2)}")
    def power_subtract(a, b):
        return print(f"The difference of squares of {a} and {b} is {math.pow(a, 2) - math.pow(b, 2)}")
    def power_multiply(a, b):
        return print(f"The product of squares of {a} and {b} is {math.pow(a, 2) * math.pow(b, 2)}")
    def power_divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return print(f"The quotient of squares of {a} and {b} is {math.pow(a, 2) / math.pow(b, 2)}")
    def square_root(c):
        return print(f"The square root of {c} is {math.sqrt(c)}")
    def circle_area(r):
        return print(f"The area of a circle with radius {r} is {3.14 * math.pow(r, 2)}")
    def circle_circumference(r):
        return print(f"The circumference of a circle with radius {r} is {2 * 3.14 * r}")
    def sphere_volume(r):
        return print(f"The volume of a sphere with radius {r} is {4/3 * 3.14 * math.pow(r, 3)}")
    def pytriple_prove(a, b, c):
        if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
            return "The given sides form a Pythagorean triple."