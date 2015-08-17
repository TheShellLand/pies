def simple_areas(*args):

    if len(args) == 0:
        return 0

    # Circle
    if len(args) == 1:
        for unknown_args in args:
            diameter = round(unknown_args, 8)
        radius = round(diameter / 2, 8)
        pi = round(3.14159265, 8)
        area_circle = round((radius ** 2) * pi, 8)
        print('Args', len(args), ':', args, 'Area of circle:', round(area_circle, 2))
        return round(area_circle, 2)
    # END Circle


    # Rectangle
    if len(args) == 2:
        side = []
        for num in args:
            side.append(num)

        area_rectangle = side[0] * side[1]
        print('Args', len(args), ':', args, 'Area of rectangle:', round(area_rectangle, 2))
        return round(area_rectangle, 2)
    # END Rectangle


    # Triangle
    if len(args) == 3:
        side = []
        for num in args:
            side.append(num)

        a = side[0]
        b = side[1]
        c = side[2]
        s = (a + b + c) / 2
        area_triangle = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('Args', len(args), ':', args, 'Area of triangle:', round(area_triangle, 2))
        return round(area_triangle, 2)
    # END Triangle


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
    assert almost_equal(simple_areas(1000), 785398.16)
    assert almost_equal(simple_areas(3.14), 7.74)