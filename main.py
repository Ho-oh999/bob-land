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

bob4 = turtle.Turtle()
bob4.shape("turtle")

bob4.speed(0)
bob4.pensize(3)

def sphere(size):
   shade = 75.0
   bob4.color(0,shade,0)
   while size > 0:
     bob4.begin_fill
     bob4.circle(size)
     bob4.end_fill()
     size -= .5
     shade += 1
     bob4.color(0,shade,0)

sphere(100)

bob5 = turtle.Turtle()
bob5.shape("turtle")

bob5.speed(0)
bob5.pensize(3)

def sphere(size):
   shade = 75.0
   bob5.color(0,shade,0)
   while size > 0:
     bob5.begin_fill
     bob5.circle(size)
     bob5.end_fill()
     size -= .5
     shade += 1
     bob5.color(shade,0,0)

sphere(100)