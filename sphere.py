# inspiration code for Python Unit Testing Project
import math

def surfaceArea(rad):
    area = 4 * math.pi * rad**2
    return area

def volume(rad):
    vol = (4/3) * math.pi * rad**3
    return vol

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    print("\nThe Volume of a Sphere = ", volume(radius))
    print("\nThe Surface Area of a Sphere = ", surfaceArea(radius))

if __name__ == '__main__':
    prompt()
