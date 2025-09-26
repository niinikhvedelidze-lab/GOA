#shevecade shemeqmna sxvadasxva namushevari igivine elementebis/funqciebis gamoyenebit


from turtle import *

speed(100)

width(30)
color("orange")
begin_fill()
forward(200)

left(120)

forward(200)

left(120)

forward(200)
end_fill()

penup()
goto(250, 0)
pendown()

# square
color("blue")
begin_fill()
setheading(0)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

penup()
right(207)
forward(400)
pendown()

begin_fill()
color("yellow")
circle(100)
end_fill()


width(3)
# Left eye
penup()
goto(-200, 120)
pendown()
color("black")
begin_fill()
circle(15)
end_fill()

# Right eye
penup()
goto(-100, 120)
pendown()
begin_fill()
circle(15)
end_fill()

# Smile
penup()
goto(-200, 55)

pendown()
setheading(-60)  
width(5)
circle(60, 120)  



exitonclick()