def cylinder():
    r = float (input())
    h = float (input())
    # площадь боковой повехности цилиндра
    side  = 2 * 3.14 * r  * h
    # площадь одного основания цилиндра
    circle = 3.14 * r ** 2
    # полная площадь цилиндра
    full = side + 2 * circle
    return full
    # в основную ветку передается значение а не переменная


print(cylinder())

area = cylinder()
print(area)
print(type(area))11