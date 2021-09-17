"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity. [DONE]
3. Apply gravity to the targets.
4. Change the speed of the ball. [DONE]

"""

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
global score
score = 0
writer = Turtle(visible=False)

def value_color(y):
    color = 'black'
    if y <= -150:
        color = 'black'
    elif y < -100:
        color = 'blue'
    elif y < -50:
        color = 'green'
    elif y < 0:
        color = 'yellow'
    elif y < 50:
        color = 'orange'
    elif y < 100:
        color = 'red'
    elif y <= 150:
        color = 'purple'
    return color
        
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 400) / 25
        speed.y = (y + 400) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, value_color(target.y))

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    global score
    writer.undo()
    writer.write(score)
    # Generate a new target at random times
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move the existing targets
    for target in targets:
        target.x -= 0.5

    # Move the cannon shot
    if inside(ball):
        speed.y -= 0.50
        ball.move(speed)

    # Make a copy of the existing target list before redrawing
    dupe = targets.copy()
    targets.clear()

    # Detect if the bullet hits a target
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            value = round((target.y+160)/2)
            score += value
            print(f"Score: + {value}")
            print(f"Score:   {score}")
            
    draw()

    # Detect when a target reaches the left side
    for target in targets:
        if not inside(target):
           #targets.remove(target)
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
print("Your score")
print(f"Score:  {score}")
hideturtle()
up()
tracer(False)
writer.pencolor('white')
writer.goto(-200,190)
writer.color('black')
writer.write(score)
onscreenclick(tap)
move()
done()
