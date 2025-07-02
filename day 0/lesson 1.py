from turtle import *
# square start
width(3)
color("blue")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()
#end of square


color("blue")
left(90)
forward(40)
left(90)

#door start
color("yellow")
begin_fill()
forward(35)
right(90)
forward(20)
right(90)
forward(35)
end_fill()
#door end
penup()

goto(100, 100)

 #roof start
pendown()
color("red")
begin_fill()
left(180)
left(31)
forward(95)
left(117)
forward(96)
end_fill()

#roof end
exitonclick()