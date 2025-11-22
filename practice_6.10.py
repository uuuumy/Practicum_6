from turtle import *
xl1,yl1 = map(int, input('Введите верхнюю левую вершину 1 прямоугольника: (x,y) ').split(","))
xr1,yr1 = map(int, input('Введите правую нижнюю вершину 1 прямоугольника: (x,y) ').split(","))
xl2,yl2 = map(int, input('Введите верхнюю левую вершину 2 прямоугольника: (x,y) ').split(","))
xr2,yr2 = map(int, input('Введите правую нижнюю вершину 2 прямоугольника: (x,y) ').split(","))

def f(xl,yl,xr,yr):
    x_min = min(xl, xr)
    x_max = max(xl, xr)
    y_min = min(yr, yl)
    y_max = max(yr, yl)
    return x_min, y_min, x_max, y_max

x1_min, y1_min, x1_max, y1_max = f(xl1, yl1, xr1, yr1)
x2_min, y2_min, x2_max, y2_max = f(xl2, yl2, xr2, yr2)

# Проверка взаимного расположения прямоугольников
if (x1_max < x2_min or x1_min > x2_max or y1_max < y2_min or y1_min > y2_max):
    print( "Прямоугольники лежат вне друг друга, не касаясь")
elif (x1_min < x2_max and x1_max > x2_min and y1_min < y2_max and y1_max > y2_min):
    # Проверяем, является ли один прямоугольник полностью внутри другого без касания
    if (x1_min > x2_min and x1_max < x2_max and y1_min > y2_min and y1_max < y2_max) or \
       (x2_min > x1_min and x2_max < x1_max and y2_min > y1_min and y2_max < y1_max):
        print("Один прямоугольник лежит внутри другого, не касаясь")
    else:
        print( "Прямоугольники пересекаются")
else:
    print( "Прямоугольники имеют касание")

speed(5)
def tr(x_min, y_min, x_max, y_max):
    penup()
    goto(x_min, y_min)
    pendown()
    for i in range(2):
        forward(x_max - x_min)
        left(90)
        forward(y_max - y_min)
        left(90)

tr(x1_min, y1_min, x1_max, y1_max)
tr(x2_min, y2_min, x2_max, y2_max)

penup()
hideturtle()
done()