from pygame import *

screen = display.set_mode((800,600))
forestPic = image.load("images/forest.jpg")
fp2 = transform.scale(forestPic,(400,300))
for x in [0,400]:
    for y in [0,300]:
        screen.blit(fp2,(x,y))
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False    
   
    display.flip()

quit()
