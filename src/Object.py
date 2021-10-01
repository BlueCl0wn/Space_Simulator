# libraries
import math

# methods
import Formula

class Object:
    def __init__(self, id,  mass, position) -> None:
        self.id = id

        self.forces = []
        self.force = None
        self.total_force = None
        self.a = None
        self.v = None

        self.mass = mass

        # self.position = position
        self.x = position[0]
        self.y = position[1]

    def get_relation(self, object) -> tuple:
        """
        Calculates distance and angle of self and given object.
        Returns tuple ('distance', 'angle').
        """
        x = object.x - self.x
        y = object.y - self.y

        a = math.atan(y/x)

        return (Formula.pythagoras(x, y), a)

    def get_force(self, object) -> None:
        """
        Calculates Force and splits it up in its x and y components.
        Returns tuple ('dis_x', 'dis_y').
        """
        relation = self.get_relation(object)

        F = Formula.F(self.mass, object.mass, relation[0])
        a = relation[1]

        F_x = math.cos(a) * F
        F_y = math.sin(a) * F

        self.forces.append((F_x, F_y))

    def calc_force(self) -> None:
        temp_x = 0
        temp_y = 0
        for i in self.forces:
            temp_x += i[0]
            temp_y += i[1]
        self.force = (temp_x, temp_y)
        self.calc_total_force()


    def calc_total_force(self) -> None:
        self.total_force = Formula.pythagoras(self.force[0], self.force[1])

    def new_pos(self, t) -> None:
        self.a = Formula.a(self.total_force, self.mass)
        self.v = Formula.v(self.a, t)

        self.a_x = Formula.a(self.force[0], self.mass)
        self.a_y = Formula.a(self.force[1], self.mass)
        self.v_x = Formula.v(self.a_x, t)
        self.v_y = Formula.v(self.a_y , t)

        self.x = Formula.d(t, self.a_x, self.v_x, self.x)
        self.y = Formula.d(t, self.a_y, self.v_y, self.x)
