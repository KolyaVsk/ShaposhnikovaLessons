def rectangle():
    a  = float(input("Ширина: "))
    b = float(input("Высота: "))
    print (print ("Площадь: %10.f" % (a*b)))



def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print("Площадь: %2f" % (0.5 * a * h))







figure = input("1- прямоугольник, 2 - треугольник, 3 - кург")

if figure == '1':
    rectangle()
if figure == '2':
    triangle()
