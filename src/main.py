# libraries
from Object import Object
import math



"""

!!! Fehler !!!:
Bei Berechnung der Kraft. Die Richtung der Kraft auf zwei Körper ist die gleiche. Müsste aber aufeinander zeigen (+ und -).
Kraftkomponente in y-Richtung, obwohl nur versetzt in x-Ebene



"""



# t in s per iteration
t = 100
objects = []
objects.append(Object(1, 100000, (-1, 0)))
objects.append(Object(2, 100000, (1, 0)))
# objects.append(Object(3, 300000, (2, 4)))
# objects.append(Object(4, 4000000, (3, 2)))
# objects.append(Object(5, 5000000, (4, 5)))


def calc_all_forces(objects, t) -> None:
    for i in range(len(objects)-1):
        for j in range(i+1, len(objects)):
            objects[i].calc_force(objects[j])
            objects[j].calc_force(objects[i])
    for i in objects:
        i.calc_sum_force()
        # i.calc_total_force()
        i.all_calcs(t)




for i in range(100):
    calc_all_forces(objects, t)
    print("F[0] = {0} N".format(objects[0].force))
    print("F[1] = {0} N".format(objects[1].force))

    print("x[0] = {0} m".format(objects[0].x))
    print("x[1] = {0} m".format(objects[1].x))

    print("y[0] = {0} m".format(objects[0].y))
    print("y[1] = {0} m".format(objects[1].y))

    print("a = {0} m/s^2".format(objects[0].a))
    print("v = {0} m/s".format(objects[0].v))
    print("----------------")


#
# for i in objects:
#     print("id = %s" % i.id)
#     print(i.force)
#     print("\tF = {0} N".format(i.force))   #  N, {1} rad, ({2} x, {3} y))".format(i.force[0], i.force[1], i.force[2][0], i.force[2][1]))
#     print("\ta = {0} m/s^2)".format(i.a))
#     print("\tv = {0} m/s)".format(i.v))
