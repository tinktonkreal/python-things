from calculatorfunctions import functions

operation = int(input("Enter the operation you want to perform: "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number (for pythagorean triple, etc): "))
match operation:
    case 1:
        functions.add(num1,num2)
    case 2:
        functions.subtract(num1, num2)
    case 3:
        functions.multiply(num1, num2)
    case 4:
        functions.divide(num1, num2)
    case 5:
        functions.power(num1)
    case 6:
        functions.power_add(num1, num2)
    case 7:
        functions.power_subtract(num1, num2)
    case 8:
        functions.power_multiply(num1, num2)
    case 9:
        functions.power_divide(num1, num2)
    case 10:
        functions.square_root(num1)
    case 11:
        functions.circle_area(num1)
    case 12:
        functions.circle_circumference(num1)
    case 13:
        functions.sphere_volume(num1)
    case 14:
        functions.pytriple_prove(num1, num2, num3)
    case _:
        print("Invalid operation. Please choose a number between 1 and 14.")
        print('Functions: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Power, 6. Power Addition, 7. Power Subtraction , 8. Power Multiplication, 9. Power Division, 10. Square Root, 11. Circle Area, 12. Circle Circumference, 13. Sphere Volume, 14. Pythagorean Triple Prove')