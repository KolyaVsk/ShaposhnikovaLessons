def cylinder():
    try:
        r = float(input())
        h = float(input())
    except ValueError:
        return
    side = 2 * 3.14 * r * h
    circle = 3.14  * r ** 2
    full = side + 2 * circle
    return side, full1

sCyl, fCyl  = cylinder()
print('Площидь боковой поверхности %.2f' % sCyl)
print ('Площадь основания %.2f' % fCyl)

a = cylinder()
print(a)
print(type(a))1