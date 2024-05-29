import pgzrun
import random

WIDTH=300
HEIGHT=300

def draw():
    #screen.fill((123,123,123))
    screen.fill("black")
    #r = Rect((0,0),(100,100))
    #r = Rect((WIDTH/2,HEIGHT/2),(100,100))
    w = WIDTH
    h = HEIGHT-200
    
    g = 50
    screen.draw.text("Hi", center=(WIDTH/2,HEIGHT/2), color="orange") 

    for i in range(20):
        r1 = Rect((0,0),(w,h))
        r = random.randint(0,255)
        b = random.randint(100,200)
        r1.center = WIDTH/2,HEIGHT/2
        #r.bottomright = WIDTH/2,HEIGHT/2
        screen.draw.rect(r1,(r,g,b)) 
        #screen.draw.filled_rect(r1,(r,g,b))   
        w -= 10
        h += 10
        g += 10

pgzrun.go()