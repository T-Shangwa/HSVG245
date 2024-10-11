#program to either convert polar to join or vice versa
from math import sqrt, cos, sin, atan, degrees


def from_cart():
    x = float(input("enter x1 coordinate:"))  # get the value of x from user
    x1 = float(input("enter x2 coordinate:"))
    y = float(input("enter y1 coordinate:"))   #get the y coordinates from user
    y1 = float(input("enter y2 coordinate:"))
    dx = x1 - x                                 #calculate coordinate differences
    dy = y1 - y
    s = dx**2 + dy**2
    r = sqrt(s)  # calculate the square root of s
    a = y / x
    angle = degrees(atan(a))  # calculate the angle in degrees
    if 0< angle <90:          #opening for angle adjustments by quadrants, first quadrant
        angle
    elif 90<angle<180:        #second quadrant
        angle = 180 - angle
    elif -180< angle <-90:    #third quadrant
        angle = angle
    else:                      #fourth quadrant
        angle = 360 - angle
    print(f"{r}m, {angle}degrees")  # display the result



def from_pol():                       #defintion for polar to cartesian
    r = float(input("Enter the distance value:"))  #get values from user
    angle = float(input("Enter the angular value:"))
    x = r * cos(angle)  # calculate x and y coordinates
    y = r * sin(angle)
    print(f"coordinates = ({x}, {y})")  #display the result


def path():  #decision function
    dec = input("Enter type of calculation to peform, (polar or join):")
    if dec == "polar":  #conversion type decision
        from_pol()
    elif dec == "join":
        from_cart()


path()
