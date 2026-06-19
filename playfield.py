import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()

def draw_playfield():
    y = 250
    for i in range(3):
        x = -150
        y -= 100
        for i in range(3):
            t.penup()
            t.goto(x,y)
            t.pendown()
            x += 100
            t.setheading(270)
            for i in range(4):
                t.forward(100)
                t.left(90)

    t.penup()


def show_restart():
    t.penup()
    t.goto(0, -200)
    t.color("black")
    t.pendown()
    t.write("Натиснить SPACE щоб грати знову", align="center", font=("Arial", 24, "bold"))

def show_winner(player):
    t.penup()
    t.goto(0, 200)
    t.color("red")
    t.pendown()
    t.write(
        f"Переміг {('хрестик' if player == 'cross' else 'нолик')}",
        align="center",
        font=("Arial", 24, "bold")
    )
    show_restart()

def show_draw():
    t.penup()
    t.goto(0, 200)
    t.color("blue")
    t.pendown()
    t.write("Нічия", align="center", font=("Arial", 24, "bold"))
    show_restart()

def draw_win_line(combo):
    t.color("red")
    t.width(5)
    t.penup()

    if combo == (0, 1, 2):  # верхняя горизонталь
        t.goto(150, 100)
        t.pendown()
        t.goto(-150, 100)

    elif combo == (3, 4, 5):  # средняя горизонталь
        t.goto(150, 0)
        t.pendown()
        t.goto(-150, 0)

    elif combo == (6, 7, 8):  # нижняя горизонталь
        t.goto(150, -100)
        t.pendown()
        t.goto(-150, -100)

    elif combo == (0, 3, 6):  # правый вертикаль
        t.goto(-100, 150)
        t.pendown()
        t.goto(-100, -150)

    elif combo == (1, 4, 7):  # центральный вертикаль
        t.goto(0, 150)
        t.pendown()
        t.goto(0, -150)

    elif combo == (2, 5, 8):  # левый вертикаль
        t.goto(100, 150)
        t.pendown()
        t.goto(100, -150)

    elif combo == (0, 4, 8):  # диагональ \
        t.goto(-150, 150)
        t.pendown()
        t.goto(150, -150)

    elif combo == (2, 4, 6):  # диагональ /
        t.goto(150, 150)
        t.pendown()
        t.goto(-150, -150)

    t.penup()
    t.width(1)
    t.color("black")