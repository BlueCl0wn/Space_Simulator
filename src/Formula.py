# libraries
import math

G = 6.67259e-11

def F(m_1, m_2, r) -> float:
    """
    Calculates the Force between two massive objects.
    """
    temp =G * m_1 * m_2
    return temp/r**2

# def split_F_components(F, angle) -> tuple:
#     """
#     Returns a tuple of the x and y component of a vector when vector and angle are given.
#     """
#     f_x = math.cos(angle) * F

def angle_of_vectors(x, y) -> float:
    """
    Calculates angle between two component_forces.
    Returns float 'angle'.
    Angles are now completely distinguishable from each other. Resulting angels can range from 0 to 360 degrees.
    """
    print(x)
    print(y)
    if y < 0 and x > 0: # Q2 (+x|-y)
        return 2 + math.pi + math.atan(y/x)
    elif x < 0: # Q3 & Q4 (-x|-+y)
        return math.pi + math.atan(y/x)
    #elif x == 0:
    #    print("x == 0")
    else: # Q1 (+x|+y)
        return math.atan(y/x)

def pythagoras(*args) -> float:
    temp = 0
    for i in args:
        temp += i**2
    # temp += i for i in self.forces
    return math.sqrt(temp)

def a(F, m) -> float:
    return F / m

def v(a, t, v_0=0) -> float:
    return a * t + v_0

def d(t, a=0, v_0=0, x_0=0) -> float:
    return x_0 + v_0*t + 0.5*a*t**2

def get_distance(object1, object2) -> float:
    x = object2.x - object1.x
    y = object2.y - object1.y
    pythagoras(x, y)

def check_for_collision(object1, object2) -> bool:
    return True if (object1.r + object2.r) >= get_distance(object1, object2) else False
