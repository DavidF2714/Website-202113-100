"""Pacman, classic arcade game.

Exercises

1. Change the board. [DONE]
2. Change the number of ghosts. [DONE]
3. Change where pacman starts. [DONE]
4. Make the ghosts faster/slower. [DONE]
5. Make the ghosts smarter.

"""

from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, 0)
#Initial pos [from origin at 190 (0,0)] (point), and direction (course); in pixels."
ghosts = [
    # Position: 21        Direction:   Color:
    [vector(-180,  160), vector(0, 0),'red'      , 0],

    # 25
    [vector(-100,  160), vector(0, 0),'pink'     , 0],

    # 35
    [vector( 100,  160), vector(0, 0),'green'    , 0],

    # 341
    [vector(-180, -160), vector(0, 0),'orange'   , 0],

    # 342
    [vector(-160, -160), vector(0, 0),'purple'   , 0],

    # 355
    [vector( 100, -160), vector(0, 0),'lightblue', 0],
    
]
    
#Empty tile => 0; and tile with pellet => 1"
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Translate position in screen from pacman's origin position"
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    "Return True if point is valid in tiles.(aka blue tile)"
    
    # Translate coords into position on grid, check for black or blue tile.
    index = offset(point)
    #print(f"Trying on: {point}")
    #print(f"Index:{index}")
    #print(f"Tile: {tiles[index]}")
    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0
    
def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def check_routes(ghost):
    "Check whether a ghost can go on a certain direction"
    print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
    print(f"{ghost[2]} ghost:")
    routes = [
        False,
        False,
        False,
        False,
    ]
    # NORTH
    if valid(ghost[0]+vector(0,20)):
        routes[0] = True
        print(f"* Path at N...")
    else:
        print(f"* Wall at N!")

    # WESTS
    if valid(ghost[0]+vector(-20,0)):
        routes[1] = True
        print(f"* Path at W...")
    else:
        print(f"* Wall at W!")
    
    # SOUTH
    if valid(ghost[0]+vector(0,-20)):
        routes[2] = True
        print(f"* Path at S...")
    else:
        print(f"* Wall at S!")
    
    # EAST
    if valid(ghost[0]+vector(20,0)):
        routes[3] = True
        print(f"* Path at E...")
    else:
        print(f"* Wall at E!")

    return routes[0],routes[1],routes[2],routes[3]

def pacman_dir(ghost):
    "Choose vertical or horizontal path towards pacman"
    available_routes = check_routes(ghost)
    pacman_routes = [vector(0,0),vector(0,0),]
    # Pacman north, and can go north
    if (ghost[0].y < pacman.y) and available_routes[0]:
        pacman_routes[0] = vector(0,1)
    # Pacman south, and can go south
    elif (ghost[0].y > pacman.y) and available_routes[2]:
        pacman_routes[0] = vector(0,-1)
    else:
        print("^ No vertical!")

    # Pacman east, and can go east
    if (ghost[0].x < pacman.x) and available_routes[3]:
        pacman_routes[1] = vector(1,0)
    # Pacman west, and can go west
    elif (ghost[0].x > pacman.x) and available_routes[1]:
        pacman_routes[1] = vector(-1,0)
    else:
        print("^ No horizontal!")

    tactic = choice(pacman_routes)
    print(f"->PACMAN APROACH: {tactic}")
    return tactic

def random_dir(ghost):
    "Choose random new direction"
    routes = check_routes(ghost)
    strat = False
    while not strat:
        suits = [0,1,2,3]
        paths = [
            vector(0,1),
            vector(-1,0),
            vector(0,-1),
            vector(1,0),
        ]
        suit = choice(suits)
        if routes[suit] == True:
            tactic = paths[suit]
            strat = True
    
    print(f"->RANDOM MOVE: {tactic}")
    return tactic

def idle(ghost):
    "No move for ghost"
    print(f"->IDLE")
    return vector(0,0)

def strategy(ghost):
    ghost[3] = 0
    tactics = [
        pacman_dir(ghost),
        pacman_dir(ghost),
        pacman_dir(ghost),
        random_dir(ghost),
        idle(ghost),
        random_dir(ghost),
        pacman_dir(ghost),
        pacman_dir(ghost),
        pacman_dir(ghost),
    ]
    speeds = [
        5,
        10,
        #20,# EXPERIENCE DEMONIC HORSE GHOSTS (experimental)
    ]
    tactic = choice(tactics)
    x = choice(speeds)
    ghost[1]=tactic*x

def move():
    #Move pacman and all ghosts.
    writer.undo()
    writer.write(state['score'])

    clear()
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)
    
    #{ On get pellet -> update score, draw square over. }"
    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    #draw pacman in the center of central pos (190)
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for ghost in ghosts:
        "Move in any of 4 dir's, 'n' ammount of pixels (greater n -> more distance per 'tick'; therefore, higher speed)" 
        if((ghost[3])<20)and((abs(ghost[1].x) != 0)or(abs(ghost[1].y)!= 0)):
            ghost[0].move(ghost[1])
            if(abs(ghost[1].x) == 5)or(abs(ghost[1].y)== 5):
                ghost[3]+=5
            else:
                ghost[3]+=10
        else:
            strategy(ghost)

        up()
        # draw ghost on center of its given pos.
        goto(ghost[0].x + 10, ghost[0].y + 10)
        dot(20, ghost[2])

    update()

    for ghost in ghosts:
        # If collision between pacman and ghost
        if abs(pacman - ghost[0]) < 20:
            return

    ontimer(move, 100)

def change(actor, x, y):
    "Change actor's aim if valid."
    if valid(actor + vector(x, y)):
        aim.x = x
        aim.y = y

# (in pixels)
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
# Fourths of square
onkey(lambda: change(pacman,  5, 0), 'Right')
onkey(lambda: change(pacman, -5, 0), 'Left')
onkey(lambda: change(pacman,  0, 5), 'Up')
onkey(lambda: change(pacman,  0, -5), 'Down')
onkey(lambda: change(pacman,  5, 0), 'd')
onkey(lambda: change(pacman, -5, 0), 'a')
onkey(lambda: change(pacman,  0, 5), 'w')
onkey(lambda: change(pacman,  0, -5), 's')
world()
move()
done()