"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower? [DONE]
2. How can you make the snake go around the edges?
3. How would you move the food? [ALREADY SATISFIED]
4. Change the snake to respond to arrow keys. [ALREADY SATISFIED]
*5. Make snake and fruit be different colors for every new game. [DONE]
"""

from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def set_initial_colors():
    colorOptions = [
        'black',
        'green',
        'blue',
        'orange',
        'purple',
        'yellow',
        'pink',
    ]
    snakeColor = choice(colorOptions)
    fruitColor = choice(colorOptions)
    if fruitColor == snakeColor:
        while fruitColor == snakeColor:
            fruitColor = choice(colorOptions)
    return snakeColor,fruitColor

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    colors = clrs
    "Move snake forward one segment."
    head = snake[-1].copy()
    print("working")
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colors[0])

    square(food.x, food.y, 9, colors[1])
    update()
<<<<<<< HEAD
    
    #We chane the speed of the snake making this value higher
    #Higher value = Slower
    #Lower value = Faster 
    ontimer(move, 50) 
=======
    ontimer(move, 100)
>>>>>>> origin

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
global clrs
clrs = set_initial_colors()
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
onkey(lambda: change(10, 0), 'D')
onkey(lambda: change(-10, 0), 'A')
onkey(lambda: change(0, 10), 'W')
onkey(lambda: change(0, -10), 'S')
move()
done()
