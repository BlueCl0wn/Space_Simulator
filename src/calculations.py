def calc_various_forces(objects) -> None:
    """
    Calculates the forces between all Objects in list 'objects'.
    """
    for i in range(len(objects) - 1):
        for j in range(i + 1, len(objects)):
            objects[i].calc_force(objects[j])
            objects[j].calc_force(objects[i])


def do_movements(objects) -> None:
    for i in objects:
        # i.calc_sum_force()
        # i.calc_total_force()
        i.do_movement(t)


def calc_all_forces(objects, t) -> None:
    calc_various_forces(objects)
    for i in objects:
        i.calc_sum_force()
        # i.calc_total_force()
        i.do_movement(t)