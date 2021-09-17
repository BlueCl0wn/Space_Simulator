# libraries
from Object import Object
import math

# t in s per iteration
t = 1

objects = []
objects.append(Object(1, 1000000, (-2, 0)))
objects.append(Object(2, 2000000, (2, 0)))
# objects.append(Object(3, 3000000, (2, 4)))
# objects.append(Object(4, 4000000, (3, 2)))
# objects.append(Object(5, 5000000, (4, 5)))


def calc_all_forces(objects) -> None:
    for i in range(len(objects)-1):
        for j in range(i+1, len(objects)):
            objects[i].get_force(objects[j])
            objects[j].get_force(objects[i])
    for i in objects:
        i.calc_force()
        # i.calc_total_force()
        i.new_pos(t)




calc_all_forces(objects)

for i in objects:
    print("id = %s" % i.id)
    print("\tF = (%s N, %s N)" % i.force)
    print("\tF_total = %s N" % i.total_force)
    print("\ta =  %s m/s^2)" % i.a)
    print("\tv =  %s m/s)" % i.v)
