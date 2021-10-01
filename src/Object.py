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
        self.force = None
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
        forces = np.array(self.forces)
        acceleration = self.a
        speed = self.v
        pos = (self.x, self.y)

        arr = np.array([forces, acceleration, speed, pos])
        self.stats.append(arr)

    def get_relation(self, object) -> tuple:
        """
        Calculates distance and angle of self and given object.
        Returns tuple ('distance', 'angle').
        """
        x = object.x - self.x
        y = object.y - self.y

        a = math.atan(y/x)

        return (Formula.pythagoras(x, y), a)

    def calc_force(self, object) -> None:
        """
        Calculates Force and splits it up in its x and y components.
        Returns tuple ('dis_x', 'dis_y').
        """
        relation = self.get_relation(object)

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
        angle = F.angle_of_vectors(force_components)
        self.force = (sum_force, angle, force_components)

    def calc_acceleration(self) -> None:
        """
        Calculates the acceleration on self.
        """
        a = Formula.a(self.total_force, self.mass)
        a_x = Formula.a(self.force[0], self.mass)
        a_y = Formula.a(self.force[1], self.mass)
        self.a = (a, (a_x, a_y))

    def calc_velocity(self) -> None:
        v = Formula.v(self.a, t)
        v_x = Formula.v(self.a_x, t)
        v_y = Formula.v(self.a_y , t)
        self.v = (v, (v_x, v_y))

    # def calc_total_force(self) -> None:
    #     self.total_force = Formula.pythagoras(self.force[0], self.force[1])

    def calc_new_pos(self, t) -> None:
        self.x = Formula.d(t, self.a_x, self.v_x, self.x)
        self.y = Formula.d(t, self.a_y, self.v_y, self.x)

    def all_calcs(self, t) -> None:
        calc_sum_force()
        calc_acceleration()
        calc_velocity()
        calc_new_pos(t)
        save_stats()
