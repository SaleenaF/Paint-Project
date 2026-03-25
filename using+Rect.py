from pygame import *
from random import *
from math import *
import py_compile 

py_compile.compile("undoRedo.pyc")

screen = display.set_mode((1250,900))
pencilRect = Rect(20,80,40,40)
eraserRect = Rect(65,80,40,40)
canvasRect = Rect(125,80,850,630)
lineRect = Rect(20,125,40,40)
alphaRect = Rect(65,125,40,40)
undoRect = Rect(20,170,40,40)
pickRect = Rect(65,170,40,40)
sprayRect = Rect(20,215,40,40)
rgbRect = Rect(20,300,84,199)

start = 0,0
sizeLine = sizeAlpha = sizeSpray = 10
sizePen = 1

rgb = image.load('RGB Colour.png')
RGB = transform.scale(rgb,(85,200))

undos = []

draw.rect(screen, (255,255,255), canvasRect)

tool = ""
undo = -1

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN: #from Loop2
           if e.button == 1:
               start = e.pos
           if e.button == 4:
               if tool == "Line":
                   sizeLine += 1
               if tool == "Brush":
                   sizeAlpha += 1
               if tool == "Pencil":
                  sizePen += 1
               if tool == "Spray":
                  sizeSpray += 1
                  
           if e.button == 5:
               if tool == "Line":
                   sizeLine -= 1
               if tool == "Brush":
                   sizeAlpha -= 1
               if tool == "Pencil":
                   sizePen -= 1
               if tool == "Spray":
                   sizeSpray -= 1
           bg = screen.copy()

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    cover = Surface((50,50)).convert()                  # make blank Surface
    cover.set_alpha(5)
    cover.fill((255,0,255))
    cover.set_colorkey((255,0,255))
    draw.circle(cover,(255,0,0),(25,25),sizeAlpha)

    draw.rect(screen,(0,255,0),pencilRect,2)
    draw.rect(screen,(0,255,0),eraserRect,2)
    draw.rect(screen,(0,255,0),lineRect,2)
    draw.rect(screen, (0,255,0),undoRect,2)
    draw.rect(screen, (0,255,0),alphaRect,2)
    draw.rect(screen, (0,255,0),pickRect,2)
    draw.rect(screen, (0,255,0),sprayRect,2)

    screen.blit(RGB, (20,300))

    if mb[0] == 1 and pencilRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),pencilRect,2)
        tool = "Pencil"
        
    if mb[0] == 1 and eraserRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),eraserRect,2)
        tool = "Eraser"

    if mb[0] == 1 and lineRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),lineRect,2)
        tool = "Line"

    if mb[0] == 1 and undoRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),undoRect,2)
        tool = "Undo"

    if mb[0] == 1 and alphaRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),alphaRect,2)
        tool = "Brush"

    if mb[0] == 1 and pickRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),pickRect,2)
        tool = "Picker"

    if mb[0] == 1 and sprayRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),sprayRect,2)
        tool = "Spray"

    if mb[0] == 1 and rgbRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),rgbRect,2)
        tool = "RGB"

    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        
        if tool == "Pencil":
            draw.line(screen, 0, (omx,omy), (mx,my), sizePen)
            
        elif tool == "Eraser":
            draw.circle(screen, (255,255,255), (mx,my), 20)
            
        elif tool == "Line":
            screen.blit(bg,(0,0))
            draw.line(screen, (255,0,0), start,(mx,my), sizeLine)

        elif tool == "Spray":
            for i in range(5):
                x1 = randint(-sizeSpray,sizeSpray)
                y1 = randint(-sizeSpray,sizeSpray)
                draw.circle(screen, (255,0,0), (mx + x1,my + y1),1)

        if tool == "Undo":
            screen.blit(undos[undo],(0,0))
            undo -= 1
            ('''if undo < 0: #if undo button is clicked when canvas is blank
                undo = 0''')

        if tool == "Brush":
            screen.blit(cover,(mx-25,my-25))
            
        screen.set_clip(None)

        if tool == "Picker":
            c = screen.get_at((mx,my))
            draw.rect(screen,c,pickRect)
            draw.rect(screen,(255,0,0),pickRect,2) #boarder of picker
            
    omx,omy = mx,my        

    print(tool)
    display.flip()


quit()
