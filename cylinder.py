#volume of a cylinder
import math
radius=float (input("enter the radius of the cylinder"))
height= float(input("enter the height of the cylinder"))
volume=math.pi*radius**2*height
surface_area=2*math.pi*radius*(radius + height)
print("the volume of the cylinder is:",volume)
print("the surface_area of the cylinder is:",surface_area)
