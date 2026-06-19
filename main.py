import turtle, playfield, logic


#
#
#

playfield.draw_playfield()
playfield.screen.onclick(logic.on_click)
playfield.screen.onkey(logic.restart, "space")
playfield.screen.listen()




turtle.mainloop()