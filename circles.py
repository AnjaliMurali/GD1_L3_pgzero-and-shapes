import pgzrun,random

WIDTH = 500
HEIGHT= 500

def draw():
    r1 = 250
    screen.fill("white")
    while(r1>50):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        screen.draw.filled_circle((WIDTH/2,HEIGHT/2),r1,(r,g,b))
        r1 -=10

pgzrun.go()