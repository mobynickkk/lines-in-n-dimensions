from lib import *


def is_on_one_side(a, c, d, other_side=False):
    """ Рассчитать то, что точка находится по одну сторону от отрезка """
    return any(map(lambda i: (other_side and a[i] >= c[i] and a[i] >= d[i]) or (a[i] <= c[i] and a[i] <= d[i]),
                   range(len(a))))


def calc_inf_overlap(a: Vector, b: Vector, c: Vector, d: Vector):
    v1, v2 = get_codirectional(Vector.get_vector(a, b), Vector.get_vector(c, d))
    if Vector.are_collinear(v1, v2) and v1.is_way_between(a, c):
        linear_reducer = Vector.get_linear_reducer(v1)
        _a, _b, _c, _d = linear_reducer(a, b, c, d)
        return Answer(max(_a, _b) >= min(_c, _d) and max(_c, _d) >= min(_a, _b),
                      (v1 * max(_a, _b), v1 * min(_c, _d))
                      if abs(max(_a, _b) - min(_c, _d)) < abs(max(_c, _d) - min(_a, _b))
                      else (v1 * max(_c, _d), v1 * min(_a, _b)))
    return Answer(False)


def main(a, b, c, d):
    inf_overlap = calc_inf_overlap(a, b, c, d)
    if inf_overlap.value:
        x, y = inf_overlap.coords
        print(f'Бесконечное количество точек в пересечении [{x}:{y}]')


if __name__ == "__main__":
    main(Vector(map(float, input().split())), Vector(map(float, input().split())),
         Vector(map(float, input().split())), Vector(map(float, input().split())))
