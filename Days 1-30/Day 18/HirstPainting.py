import random 
import turtle as t


t.up()
t.colormode(255)
def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    color = (r , g , b)
    return color

t.goto(-500 , -500)
for x in range(10):
    for x in range(10):
        t.color(random_color())
        t.dot(50)
        t.forward(100)
    t.back(1000)
    t.left(90)
    t.forward(100)
    t.right(90)


