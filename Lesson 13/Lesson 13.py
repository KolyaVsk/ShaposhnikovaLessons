def rectangle():
    a  = float(input("Ширина: "))
    b = float(input("Высота: "))
    return a * b

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    return 0.5 * a * h




result = 0.0
figure = input("Введите цифру в соотвесвтии с фиугрой (1- прямоугольник, 2 - треугольник): ")

if figure == '1':
    result = rectangle()
    print("Площадь: %2f" % result)
elif figure == '2':
    result = triangle()
    print("Площадь: $2f" % result)
else:
    print("Hет такой фигуры")11