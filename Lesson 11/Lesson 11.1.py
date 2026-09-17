def rectangle():
    a  = float(input("Ширина: "))
    b = float(input("Высота: "))
    print("Площадь: %2.f" % (a*b))

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print("Площадь: %2f" % (0.5 * a * h))

def circul():
    r = float(input("Радиус:"))
    print ("Площадь: %2.f" %(2 * 3.14159 * r))





figure = input("Введите цифру в соотвесвтии с фиугрой (1- прямоугольник, 2 - треугольник, 3 - кург): ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
elif figure == '3':
    circul()
else:
    print("Hет такой фигуры")