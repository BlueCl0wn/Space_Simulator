# libraries
import math
import numpy as np

# methods
import Formula

class Object:
    def __init__(self, id, name, mass, position, radius, v) -> None:
        self.id = id
        self.name = name

        self.stats = []

        self.current_forces = []
        self.force = None # (F, alpha, (F_x, F_y))
        self.a = None
        self.v = None

        self.mass = mass
        self.r = radius

        # self.position = position
        self.x = position[0]
        self.y = position[1]


    def save_stats(self) -> None:
        """
        Saves all important informations in the list 'self.stats' for later usage.
        """
        # forces = np.array(self.forces, dtype=object)
        F = (self.force, self.current_forces)
        acceleration = self.a
        speed = self.v
        pos = (self.x, self.y)

        # arr = np.array([forces, acceleration, speed, pos],dtype=object)
        arr = [F, acceleration, speed, pos]
        self.stats.append(arr)

#    def get_distance(self, object) -> float:
#        return Formula.pythagoras(object.x - self.x, object.y - self.y)


    def get_relation(self, object) -> tuple:
        """
        Calculates distance and angle of self and given object.
        Returns tuple ('distance', 'angle').
        """
        x = object.x - self.x
        y = object.y - self.y

        angle = Formula.angle_of_vectors(x, y)
        distance = Formula.pythagoras(x, y)

        return (distance, angle)


    def calc_force(self, object) -> None:
        """
        Calculates Force and splits it up in its x and y components.
        Returns tuple ('dis_x', 'dis_y').
        """
        relation = self.get_relation(object)
        angle = Formula.angle_of_vectors(object.x - self.x, object.y - self.y)

        F = Formula.F(self.mass, object.mass, relation[0])

        F_x = round(math.cos(angle) * F, 9)
        F_y = round(math.sin(angle) * F, 9)

        self.current_forces.append((F, angle, (F_x, F_y)))


    def calc_sum_force(self) -> None:
        """
        Creates a tuple with all current information about self.
        Returns '(magnitude, angle, (F_x, F_y))'.
        """
        temp_x = 0
        temp_y = 0
        print()
        print(self.current_forces)
        for i in self.current_forces:
            temp_x += i[2][0]
            temp_y += i[2][1]

        temp_force = (temp_x, temp_y)

        self.current_forces = []

        sum_force = Formula.pythagoras(temp_force[0], temp_force[1])
        angle = Formula.angle_of_vectors(temp_force[0], temp_force[1])
        self.force = (sum_force, angle, temp_force)


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


    def calc_new_pos(self, t) -> None:
        self.x = Formula.d(t, self.a[1][0], self.v[1][0], self.x)
        self.y = Formula.d(t, self.a[1][1], self.v[1][1], self.y)


    def do_calculations(self, t) -> None:
        self.calc_sum_force()


    def do_movement(self, t) -> None:
        # self.calc_sum_force()

        self.calc_acceleration()
        self.calc_velocity(t)
        self.calc_new_pos(t)

        self.save_stats()

    def did_collide(self, object) -> None:
        print("I ({}) collided with {}".format(self.name, object.name))
