import sys 

print("Area calculator😒")

# Add the rest of the script content here
print("\n")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

print("\n")

shape = int(input("Which shape: "))

print("\n")

match shape:
    case 1:
        height = float(input("Enter height of triangle: "))
        base = float(input("Enter base of triangle: "))
        area = (height * base) / 2
        print(f"The area is {area}")
    
    case 2:
        length = float(input("Enter length of rectangle: "))
        breadth = float(input("Enter breadth of rectangle: "))
        area = length * breadth
        print(f"The area is {area}")
    
    case 3:
        side = float(input("Enter side of square: "))
        area = side * side
        print(f"The area is {area}")
    
    case 4:
        radius = float(input("Enter radius of circle: "))
        area = 3.14 * radius * radius
        print(f"The area is {area}")
            
    case 5:
        print("Quitting....")
        sys.exit()
        
    case _:
        print("Invalid input!")