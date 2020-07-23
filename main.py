import turtle
bob3 = turtle.Turtle()
bob3.shape("turtle")

bob3.speed(0)
bob3.pensize(3)

def sphere(size):
   shade = 75.0
   bob3.color(0,shade,0)
   while size > 0:
     bob3.begin_fill
     bob3.circle(size)
     bob3.end_fill()
     size -= .5
     shade += 1
     bob3.color(0,0,shade)

sphere(100)