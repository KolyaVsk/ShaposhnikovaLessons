def cylinder(r: float,h : float):

    side = 2 * 3.14 * r * h
    circle  = 3.14 * r ** 2
    full = side  + 2 * circle
    return full



c1 = cylinder(h = 4.5, r= 1.2)
print(c1)

c1 = cylinder (1.2,"gg")
print(c1)