from lib import *


def are_in_one_plane(a: Tensor, b: Tensor, c: Tensor, d: Tensor):
    if len(a) <= 2:
        return True


def is_on_one_side(a, c, d, other_side=False):
    """ Рассчитать то, что точка находится по одну сторону от отрезка """
    return any(map(lambda i: (other_side and a[i] >= c[i] and a[i] >= d[i]) or (a[i] <= c[i] and a[i] <= d[i]),
                   range(len(a))))


def calc_inf_overlap(a: Tensor, b: Tensor, c: Tensor, d: Tensor):
    v1, v2 = get_codirectional(Tensor.get_vector(a, b), Tensor.get_vector(c, d))
    if Tensor.are_collinear(v1, v2) and v1.is_way_between(a, c):
        linear_reducer = Tensor.get_linear_reducer(v1)
        _a, _b, _c, _d = linear_reducer(a, b, c, d)
        return Answer(max(_a, _b) >= min(_c, _d) and max(_c, _d) >= min(_a, _b),
                      (v1 * max(_a, _b), v1 * min(_c, _d))
                      if abs(max(_a, _b) - min(_c, _d)) < abs(max(_c, _d) - min(_a, _b))
                      else (v1 * max(_c, _d), v1 * min(_a, _b)))
    return Answer(False)


def calc_one_point_intersection(a: Tensor, b: Tensor, c: Tensor, d: Tensor):
    v1, v2 = get_codirectional(Tensor.get_vector(a, b), Tensor.get_vector(c, d))
    if Tensor.are_collinear(v1, v2) and v1.is_way_between(a, c):
        linear_reducer = Tensor.get_linear_reducer(v1)
        _a, _b, _c, _d = linear_reducer(a, b, c, d)
        return Answer(max(_a, _b) == min(_c, _d) or max(_c, _d) == min(_a, _b),
                      max(_a, _b) if max(_a, _b) == min(_c, _d) else max(_c, _d))
    elif not Tensor.are_collinear(v1, v2):
        # TODO: добавить рекурсивный расчет (до трехмерной гиперплоскости) расположения точек в одной гиперплоскости
        #  для проверки их на возможность пересечения, а также проверку по теореме о концах отрезка
        return
    return Answer(False)


def main(a, b, c, d):
    inf_overlap = calc_inf_overlap(a, b, c, d)
    one_point_intersection = calc_one_point_intersection(a, b, c, d)
    if inf_overlap.value:
        x, y = inf_overlap.coords
        print(f'Бесконечное количество точек в пересечении [{x}:{y}]')
    elif one_point_intersection.value:
        print(f'Отрезки пересекаются в {one_point_intersection.coords}')
    print('Нет пересечений')


if __name__ == "__main__":
    main(Tensor(map(float, input().split())), Tensor(map(float, input().split())),
         Tensor(map(float, input().split())), Tensor(map(float, input().split())))
