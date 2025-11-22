from turtle import *


import math

w = Screen()

x_1 = float(input('координат x первой окружности: '))
y_1 = float(input('координаты y первой окружности: '))
r_1 = float(input('радиус первой окружности: '))
x_2 = float(input('координата x второй окружности: '))
y_2 = float(input('координата y второй окружности: '))
r_2 = float(input('радиус второй окружности: '))

penup()
goto(x_1, y_1)
pendown()
circle(r_1)

penup()
goto(x_2, y_2)
pendown()
circle(r_2)

def distance_between_centers(x_1, y_1, x_2, y_2): # расстояние между центрами
    return math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

def circle_relation(x_1, y_1, r_1, x_2, y_2, r_2): # отношение окружностей
    distance = distance_between_centers(x_1, y_1, x_2, y_2)

    if distance > r_1 + r_2:
        return "Окружности лежат одна вне другой, не касаясь"
    elif distance == r_1 + r_2:
        return "Окружности имеют общее касание"
    elif distance < abs(r_1 - r_2):
        return "Одна окружность лежит внутри другой, не касаясь"
    elif distance == abs(r_1 - r_2):
        return "Окружности имеют внутреннее касание"
    else:
        return "Окружности пересекаются"


relation = circle_relation(x_1, y_1, r_1, x_2, y_2, r_2)
print(relation)

w.mainloop()