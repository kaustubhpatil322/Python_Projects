
# import turtle
#
# tim = turtle.Turtle()


# from turtle import Turtle , Screen
#
# tim  =  Turtle()
# print(tim)
# tim.shape("turtle")
# tim.color("turquoise")
# my_screen = Screen()
# print(my_screen.canvheight)
#
# tim.forward(100)
#
# my_screen.exitonclick()

from prettytable import PrettyTable , TableStyle
table = PrettyTable()
#table - object

table.field_names = ["PokemonNames" , "Type"]
table.add_row(["Pikachu" , "Thunder"])
table.add_row(["Charizard" , "Fire"])
table.add_row(["Squartle" , "Water"])

table.set_style(TableStyle.DOUBLE_BORDER)

table.align = "l"
table.add_column("Stage" , [2 , 3 , 1])
print(table)
