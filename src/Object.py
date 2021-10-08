# libraries
import math
import numpy as np

# methods
import Formula

class Object:
    def __init__(self, id,  mass, position) -> None:
        self.id = id

        self.stats = []

        self.forces = []
        self.force = None # (F, a, (F_x, F_y))
        self.a = None
        self.v = None

        self.mass = mass

        # self.position = position
        self.x = position[0]
        self.y = position[1]



    def save_stats(self) -> None:
        """
        Saves all important informations in the list 'self.stats' for later usage.
        """
        forces = np.array(self.forces, dtype=object)
        acceleration = self.a
        speed = self.v
        pos = (self.x, self.y)

        # print("\tforces = %s")
        # print(forces)
        # print("\tacceleration = ")
        # print(acceleration)
        # print("\tspeed = ")
        # print(speed)
        # print("\tpos = ")
        # print(pos)

        # arr = np.array([forces, acceleration, speed, pos],dtype=object)
        arr = [forces, acceleration, speed, pos]
        self.stats.append(arr)

    def get_relation(self, object) -> tuple:
        """
        Calculates distance and angle of self and given object.
        Returns tuple ('distance', 'angle').
        """
        x = object.x - self.x
        y = object.y - self.y

        if x == 0:
            return (Formula.pythagoras(x, y), math.pi/2)
        else:
            a = math.atan(y/x)

        return (Formula.pythagoras(x, y), a)

    def calc_force(self, object) -> None:
        """
        Calculates Force and splits it up in its x and y components.
        Returns tuple ('dis_x', 'dis_y').
        """
        relation = self.get_relation(object)
        # print(relation)

        print("distance: ")
        print(relation[0])
        F = Formula.F(self.mass, object.mass, relation[0])
        a = relation[1]

        F_x = math.cos(a) * F
        F_y = math.sin(a) * F

        self.forces.append((F, a, (F_x, F_y)))

    def calc_sum_force(self) -> None:
        """
        Creates a tuple with all current information about self.
        Returns '(magnitude, angle, (F_x, F_y))'.
        """
        temp_x = 0
        temp_y = 0
        for i in self.forces:
            temp_x += i[0]
            temp_y += i[1]
        self.force = (temp_x, temp_y)
        force_components = (temp_x, temp_y)
        sum_force = Formula.pythagoras(self.force[0], self.force[1])
        angle = Formula.angle_of_vectors(force_components)
        self.force = (sum_force, angle, force_components)

    def calc_acceleration(self) -> None:
        """
        Calculates the acceleration on self.
        """
        a = Formula.a(self.force[0], self.mass)
        a_x = Formula.a(self.force[2][0], self.mass)
        a_y = Formula.a(self.force[2][1], self.mass)
        self.a = (a, (a_x, a_y))

    def calc_velocity(self, t) -> None:
        v = Formula.v(self.a[0], t)
        v_x = Formula.v(self.a[1][0], t)
        v_y = Formula.v(self.a[1][1] , t)
        self.v = (v, (v_x, v_y))

    # def calc_total_force(self) -> None:
    #     self.total_force = Formula.pythagoras(self.force[0], self.force[1])

    def calc_new_pos(self, t) -> None:
        self.x = Formula.d(t, self.a[1][0], self.v[1][0], self.x)
        self.y = Formula.d(t, self.a[1][1], self.v[1][1], self.x)

    def all_calcs(self, t) -> None:
        self.calc_sum_force()
        self.calc_acceleration()
        self.calc_velocity(t)
        self.calc_new_pos(t)
        self.save_stats()
