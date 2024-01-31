import turtle

#
# turtle.showturtle()
# turtle.forward(n)
# turtle.backward(n)

# при помощи команд turtle.right() и turtle.left() можно повернуть черепашку:
# команда turtle.right(angle) поворачивает черепашку вправо на angle градусов;
# команда turtle.left(angle) поворачивает черепашку влево на angle градусов.


# Команда turtle.setheading() применяется для установки углового направления черепашки с заданным углом. В качестве аргумента нужно указать желаемый угол.

# turtle.speed(1)
#
# turtle.forward(100)
# turtle.setheading(90)
#
# turtle.forward(100)
# turtle.setheading(180)
#
# turtle.forward(100)
# turtle.setheading(270)
#
# turtle.forward(100)
# turtle.done()
# чтобы получить текущее угловое направление черепашки используется команда turtle.heading()
# print(turtle.heading())
# turtle.setheading(180)
# print(turtle.heading())

# По умолчанию черепашка выглядит как стрелочка, но возможен и другой внешний вид. Для его изменения используют
# команду shape(). Команда принимает в качестве аргумента строковое название фигуры, определяющей форму черепашки.

# import turtle
# def rectangle(width, height):
#     turtle.forward(width)
#     turtle.left(90)
#
#     turtle.forward(height)
#     turtle.left(90)
#
#     turtle.forward(width)
#     turtle.left(90)
#
#     turtle.forward(height)
#     turtle.left(90)
#
# width_1 = int(input())
# height_1 = int(input())
# rectangle(width_1, height_1)


# import turtle
#
# def rectangle(width, height):
#   for _ in range(4):
#     turtle.forward(width)
#     turtle.left(90)
#     width, height = height, width
#
# width = int(input())
# height = int(input())
# rectangle(width, height)


