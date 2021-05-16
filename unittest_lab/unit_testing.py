from math import pi

def areea_of_circle(r):
    if r < 0:
        raise ValueError("Negative radius value error") #Remove this line if want to see how test)unit_testing fails
    return pi*(r**2)


