from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.colormode(255)

# Color list
color_list = [(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156),
              (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30),
              (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47),
              (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241),
              (5, 68, 42), (216, 90, 52), (173, 178, 231), (235, 170, 164), (8, 244, 224), (248, 9, 44), (10, 77, 114),
              (20, 53, 243)]

count_dots = 0
color_index = 0
tim.up()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
for _ in range(100):
    if color_index >= len(color_list):
        color_index = 0

    tim.dot(20, color_list[color_index])
    count_dots += 1
    color_index += 1

    if not count_dots % 10 == 0:
        tim.forward(50)
    elif (count_dots // 10) % 2 != 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
    else:
        tim.right(90)
        tim.forward(50)
        tim.right(90)

print(count_dots)
screen.exitonclick()
