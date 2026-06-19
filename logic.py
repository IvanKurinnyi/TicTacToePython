import random, turtle
import playfield

cell_list = [
    0,0,0,
    0,0,0,
    0,0,0
]
turn = [0]
turn[0] = random.choice(["cross","zero"])

index_cell = [0]
x_save = [-150]
y_save = [150]

#
#
#

def check_click(x,y):
    if -150 < x < -50:
        index_cell[0] = 0
        x_save[0] = -150
    elif -50 < x < 50:
        index_cell[0] = 1
        x_save[0] = -50
    elif 50 < x < 150:
        index_cell[0] = 2
        x_save[0] = 50  
    
    if 50 < y < 150:
        index_cell[0] += 0
        y_save[0] = 150  
    elif -50 < y < 50:
        index_cell[0] += 3
        y_save[0] = 50  
    elif -150 < y < -50:
        index_cell[0] += 6
        y_save[0] = -50
    print(index_cell)
     
#
#
#

def cross(t,x,y):
    t.goto(x,y)
    t.pendown()
    t.goto(x + 100,y - 100)
    t.goto(x + 100,y)
    t.goto(x,y - 100)
    t.penup()
    turn[0] = "zero"

def zero(t,x,y):
    t.goto(x + 50, y - 100)
    t.setheading(0)
    t.pendown()
    t.circle(50)
    t.penup()
    turn[0] = "cross"

#
#
#

win_combo = [
    (0, 1, 2),  # верхняя строка
    (3, 4, 5),  # середина
    (6, 7, 8),  # низ
    (0, 3, 6),  # левый столбец
    (1, 4, 7),  # центр
    (2, 5, 8),  # правый столбец
    (0, 4, 8),  # диагональ \
    (2, 4, 6),  # диагональ /
]

player = [0]

def check_victory(cell_list, last_move_index):
    player[0] = cell_list[last_move_index]
    for combo in win_combo:
        if last_move_index in combo:
            if all(cell_list[i] == player[0] for i in combo):
                return combo
    return False

#
#
#

finish = [False]

def on_click(x, y):
    if not finish[0]:
        check_click(x, y)
        if cell_list[index_cell[0]] == 0: 
            cell_list[index_cell[0]] = turn[0]
            if turn[0] == "cross":
                cross(playfield.t,x_save[0],y_save[0])

            elif turn[0] == "zero":
                zero(playfield.t,x_save[0],y_save[0])   
        check_victory(cell_list, index_cell[0])
        if check_victory(cell_list, index_cell[0]):
            finish[0] = True
            playfield.draw_win_line(check_victory(cell_list, index_cell[0]))
            playfield.show_winner(player[0])
        elif all(cell != 0 for cell in cell_list):
            finish[0] = True
            playfield.show_draw()
            

def restart():
    if not finish[0]:
        return 
    

    
    for i in range(9):
        cell_list[i] = 0
    finish[0] = False
    turn[0] = random.choice(["cross", "zero"])

    playfield.screen.clear()
    playfield.screen.onclick(on_click)
    playfield.screen.onkey(restart, "space")
    playfield.screen.listen()
    playfield.t = turtle.Turtle()  
    playfield.t.speed(0)
    playfield.t.hideturtle()
    playfield.t.color("black")
    playfield.draw_playfield()
    playfield.screen.onclick(on_click)
