# Problem: Create a function that returns both the area and circumference of a circle given its radius.

# The area and circumference of a circle based on radius (\(r\)) are calculated using the formulas
#  \(Area = \pi r^2\) and \(Circumference = 2\pi r\). Using \(\pi \approx 3.14159\), the area represents
#  the total space inside the circle, while the circumference is the distance around it
import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circleumference = 2 * math.pi * radius
    return area, circleumference


area, circumference = circle_stats(3)

print("Area: ", area,"Circumferance: " , circumference)
print("Area: ", round(area, 2),"Circumferance: " , round(circumference, 2))


