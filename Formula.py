# libraries
import math

G = 6.67259e-11

def F(m_1, m_2, r) -> float:
    """
    Calculates the Force between two massive objects.
    """
    return G * ((m_1 * m_2)/r**2)

def pythagoras(*args) -> float:
    temp = 0
    for i in args:
        temp += i**2
    # temp += i for i in self.forces
    return math.sqrt(temp)

def a(F, m) -> float:
    return F / m

def v(a, t, v_0=0) -> float:
    return (a * t) + v_0

def d(t, a=0, v_0=0, x_0=0) -> float:
    return x_0 + v_0*t + 0.5*a*t**2
