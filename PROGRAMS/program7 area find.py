'''
Write a menu-driven program, using user-defined functions to find the area of rectangle, square, circle and triangle by accepting suitable input parameters from user
'''

def area_rectangle(length, width):
    return length * width

def area_square(side):
    return side ** 2

def area_circle(radius):
    return 3.14 * radius ** 2

def area_triangle(base, height):
    return 0.5 * base * height

# Menu function
def main_menu():
    print("\n*** Area Calculation Menu ***\n")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")

# Main program
while True:
    main_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"Area of the rectangle: {area_rectangle(length, width)}")
    elif choice == '2':
        side = float(input("Enter the side length of the square: "))
        print(f"Area of the square: {area_square(side)}")
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        print(f"Area of the circle: {area_circle(radius)}")
    elif choice == '4':
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"Area of the triangle: {area_triangle(base, height)}")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
