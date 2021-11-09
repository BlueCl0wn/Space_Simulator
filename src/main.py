# libraries
from Object import Object
import math
#import matplotlib.pyplot as plt



# t in s per iteration
t = 1
objects = []
objects.append(Object(1, "Mars", 100000000, (1, 0), 5, v=(0,100)))
objects.append(Object(2, "Sonne", 100000000, (0, 0), 5, v=(0,-100)))
# objects.append(Object(3, 300000, (2, 4)))
# objects.append(Object(4, 4000000, (3, 2)))
# objects.append(Object(5, 5000000, (4, 5)))


def calc_various_forces(objects) -> None:
    """
    Calculates the forces between all Objects in list 'objects'.
    """
    for i in range(len(objects)-1):
        for j in range(i+1, len(objects)):
            objects[i].calc_force(objects[j])
            objects[j].calc_force(objects[i])

def do_movements(objects) -> None:
    for i in objects:
        i.calc_sum_force()
        # i.calc_total_force()
        i.do_movement(t)



def calc_all_forces(objects, t) -> None:
    calc_various_forces(objects)
    for i in objects:
        i.calc_sum_force()
        # i.calc_total_force()
        i.do_movement(t)

r = 100

for i in range(r):
    # print("x[0] = {0} m".format(objects[0].x))
    # print("x[1] = {0} m".format(objects[1].x))


    objects[0].calc_force(objects[1])
    objects[0].calc_sum_force()
    objects[0].do_movement(t)



    # calc_all_forces(objects, t)

    # print("F[0] = {0} N".format(objects[0].force))
    # print("F[1] = {0} N".format(objects[1].force))

    # print("x[0] = {0} m".format(objects[0].x))
    # print("x[1] = {0} m".format(objects[1].x))

    # print("y[0] = {0} m".format(objects[0].y))
    # print("y[1] = {0} m".format(objects[1].y))

    # print("a = {0} m/s^2".format(objects[0].a))
    # print("v = {0} m/s".format(objects[0].v))
    # print("----------------")

# print(objects[0].stats[0])
# print(objects[0].stats[0][0])
# print(objects[0].stats[0][0][0])
# print(objects[0].stats[0][0][0][0])

position = [pos[3][0] for pos in objects[0].stats]
# position2 = [pos[3][0] for pos in objects[1].stats]
print("pos: {}".format(position))
# velocity = [pos[2][0] for pos in objects[0].stats]
# acceleration = [pos[1][0] for pos in objects[0].stats]
force = [pos[0][0][0] for pos in objects[0].stats]
print("force: {}".format(force))
time = [i for i in range(r)]

for i in range(r):
    print("i: {}        force: {}        pos: {}".format(i, force[i], position[i]))
"""
fig, ax = plt.subplots()
ax.plot(time, position, color='blue') # position
ax.plot(time, position2, color='magenta') # position
ax.plot(time, velocity, color='red') # velocity
ax.plot(time, acceleration, color='black') # acceleration
# ax.plot(time, force, color='orange') # force
ax.set_xlim(30, 70)
ax.grid()
plt.show()
"""
# for i in objects[0].stats:
#     print(i[2][0])
#     print(i[2][1][0])
#     # print("i: {}".format(i))
#     print("-----------")

#
# for i in objects:
#     print("id = %s" % i.id)
#     print(i.force)
#     print("\tF = {0} N".format(i.force))   #  N, {1} rad, ({2} x, {3} y))".format(i.force[0], i.force[1], i.force[2][0], i.force[2][1]))
#     print("\ta = {0} m/s^2)".format(i.a))
#     print("\tv = {0} m/s)".format(i.v))
