#Saleena Farrukh
#Paint V3 - A painting program
#This program allows the user to select from individual modes. Each mode has its own colour theme and
#character which explains which tool the user is currenting using and what that tool does
#Tools include: Pencil, Eraser, Line tool, Alpha/soft brush, Filled & Unfilled Rectangle, a Colour Picker (from canvas),
#Spray paint tool, Solid Brush, Filled & Unfilled Ellipse, and 6 individual stickers
#User can also choose the colour from the box on the right and other specific colours
#the colour in use is shown under the colour picker box
#The "Special" tool changes from mode to mode.
# > Normal mode makes multiple hearts in shades of red
# > Casual mode makes multiple stars in shades of purple
# > Ellite mode makes multiple hallow diamond shapes in shades of blue
#All tools and stcikers can change size using the scroll. They all have lower size limits, and only some have upper limits (alpha = 25 and special = 50)
#Other features this program has is the Undo/Redo function, Loading a png or jpg file from ANYWHERE, Saving progress
#to ANY folder the user chooses with name of user's choice
#The changing of modes also prompts the character to ask if the user is alright with losing progress w/ yes no buttons
#Coordinates of mouse on canvas are on the top right, and size of the tool in use are on the top left

from pygame import *
from random import *
from math import *
import random
from tkinter import *                
from tkinter import filedialog
import os

root = Tk()
root.withdraw()

#===============================FIX SCREEN POS==================================
#makes screen popup where is can easy be seen
init()
inf = display.Info()
w,h = inf.current_w,inf.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = '25,25'

screen = display.set_mode((w-50,h-50),NOFRAME)

for x in range(0,screen.get_width(),10):
    draw.line(screen, (0, 0, 255), (x,0), (x,screen.get_height()))
#===============================================================================

#FONTS
font.init()
comicFont = font.SysFont("Courier New", 20)
bigFont = font.SysFont("Courier New", 25)
smallFont = font.SysFont("Courier New", 14)

#LIST OF COMMENTS
#from characters in speech bubble
#0 = default, 1 = Pencil, 2 = Eraser, 3 = Line, 4 = Brush ect.

toolComment = ["", ".:PENCIL:.", ".:ERASER:.", ".:LINE:.", ".:SOFT BRUSH:.",
               ".:RECTANGLE:.", ".:COLOUR PICKER:.",".:SPRAY:.", ".:HARD BRUSH:.",
               ".:SPECIAL:.",".:ELLIPSE:.", ".:STICKERS:."]

commentSet_1 = ["Select your brush.", "Use this for","You made a mistake?",
                "Try underlining.","For gradation.","Size 0 = Filled In","It copies the colour",
                "Change size w/scroll.","For solid colouring.","This one is mine...",
                "Size 0 = Filled In","Rightclick + Scroll"]

commentSet_2 = ["pick a tool", "i prefer size 1 for","nice job...lol","it gets thicker",
                "25 is the max","it fills @ sZ 0","pick a colour on","it's like the",
                "paints slowly","GOOD CHOICE!","it fills @ Sz 0","the bears can get"]

commentSet_3 = ["Left side has tools.","Scroll to change","Do not fret over","Drag to draw."
                ,"Try shading.","The size equals the","Select a colour.","Click on your colour.",
                "Size has no limit.","The colour doesn't","Drag from top left to","I recommend not"]

screen = display.set_mode((1300,825)) #make screen

#RECTS FOR TOOLS
pencilRect = Rect(20,80,40,40)
eraserRect = Rect(65,80,40,40)
canvasRect = Rect(125,80,850,670)
lineRect = Rect(20,125,40,40)
alphaRect = Rect(65,125,40,40)
undoRect = Rect(20,305,40,40)
redoRect = Rect(65,305,40,40)
pickRect = Rect(65,170,40,40)
sprayRect = Rect(20,215,40,40)
solRect = Rect(65,215,40,40)
ellipseRect = Rect(65,260,40,40)
rectRect = Rect(20,170,40,40)
rgbRect = Rect(995,80,157,202) #two pixels bigger to cover the boarder
underRGBRect = Rect(995,300,155,20)
saveRect = Rect(20,350,40,40)
loadRect = Rect(65,350,40,40)
specialRect = Rect(20,260,40,40) #different brush for each character

yesRect = Rect(1080,406,50,25) #options when changing modes
noRect = Rect(1140,406,50,25)

redRect = Rect(1182,80,40,40) #colours: when picking from specific colour set
orgRect = Rect(1227,80,40,40)
yelRect = Rect(1182,125,40,40)
greRect = Rect(1227,125,40,40)
bluRect = Rect(1182,170,40,40)
purRect = Rect(1227,170,40,40)
blRect = Rect(1182,215,40,40)
whRect = Rect(1227,215,40,40)

#STICKER RECTS
bearRect1 = Rect(125,755,280,30)
bearRect2 = Rect(125,790,280,30)
bearRect3 = Rect(410,755,280,30)
bearRect4 = Rect(410,790,280,30)
bearRect5 = Rect(695,755,280,30)
bearRect6 = Rect(695,790,280,30)

#LOAD TOOL ICONS
pencil = transform.scale(image.load("images/Pencil.png"),(40,40))
eraser = transform.scale(image.load("images/Eraser.png"),(40,40))
brush = transform.scale(image.load("images/Brush.png"),(40,40))
spray = transform.scale(image.load("images/Spray.png"),(40,40))
picker = transform.scale(image.load("images/Picker.png"),(40,40))
line = transform.scale(image.load("images/Line.png"),(40,40))
brush2 = transform.scale(image.load("images/Brush3.png"),(40,40))
ellip = transform.scale(image.load("images/Circ.png"),(40,40))
back = transform.scale(image.load("images/Undo.png"),(40,40))
forward = transform.scale(image.load("images/Redo.png"),(40,40))
rct = transform.scale(image.load("images/Rect0.png"),(40,40))
flop = transform.scale(image.load("images/Save.png"),(30,30))
unflop = transform.scale(image.load("images/Load.png"),(30,30))
heart1 = transform.scale(image.load("images/RHeart.png"),(30,30))
heart2 = transform.scale(image.load("images/PHeart.png"),(30,30))
heart3 = transform.scale(image.load("images/BHeart.png"),(30,30))

speech = transform.scale(image.load("images/Speech.png"),(272,160))

#LOAD BACKGROUNDS
redBG = image.load('images/RedBG.png')
purBG = image.load('images/PurBG.png')
blueBG = image.load('images/BlueBG.png')

#LOAD CHAR BGS
#blits if character changes; to cover previously blit character
charBG1 = image.load("images/RedBG2.png")
charBG2 = image.load("images/PurBG2.png")
charBG3 = image.load("images/BlueBG2.png")

girlRect = Rect(20,465,85,85) #rects to click when changing modes
boyRect = Rect(20,565,85,85)
girl2Rect = Rect(20,665,85,85)

#LOAD STICKER SLITS
#there are a lot so the opacity decreasing effect can be creatd
bear1 = transform.scale(image.load("images/Monokuma Slit.png"),(150,30))
bear2 = transform.scale(image.load("images/Monotaro Slit.png"),(150,30))
bear3 = transform.scale(image.load("images/Monophanie Slit.png"),(150,30))
bear4 = transform.scale(image.load("images/Monokid Slit.png"),(150,30))
bear5 = transform.scale(image.load("images/Monosuke Slit.png"),(150,30))
bear6 = transform.scale(image.load("images/Monodam Slit.png"),(150,30))
#80% opacity
bear11 = transform.scale(image.load("images/Monokuma Slit2.png"),(150,30))
bear21 = transform.scale(image.load("images/Monotaro Slit2.png"),(150,30))
bear31 = transform.scale(image.load("images/Monophanie Slit2.png"),(150,30))
bear41 = transform.scale(image.load("images/Monokid Slit2.png"),(150,30))
bear51 = transform.scale(image.load("images/Monosuke Slit2.png"),(150,30))
bear61 = transform.scale(image.load("images/Monodam Slit2.png"),(150,30))
#60% opacity
bear12 = transform.scale(image.load("images/Monokuma Slit3.png"),(150,30))
bear22 = transform.scale(image.load("images/Monotaro Slit3.png"),(150,30))
bear32 = transform.scale(image.load("images/Monophanie Slit3.png"),(150,30))
bear42 = transform.scale(image.load("images/Monokid Slit3.png"),(150,30))
bear52 = transform.scale(image.load("images/Monosuke Slit3.png"),(150,30))
bear62 = transform.scale(image.load("images/Monodam Slit3.png"),(150,30))
#40% opacity
bear13 = transform.scale(image.load("images/Monokuma Slit4.png"),(150,30))
bear23 = transform.scale(image.load("images/Monotaro Slit4.png"),(150,30))
bear33 = transform.scale(image.load("images/Monophanie Slit4.png"),(150,30))
bear43 = transform.scale(image.load("images/Monokid Slit4.png"),(150,30))
bear53 = transform.scale(image.load("images/Monosuke Slit4.png"),(150,30))
bear63 = transform.scale(image.load("images/Monodam Slit4.png"),(150,30))
#20% opacity
bear14 = transform.scale(image.load("images/Monokuma Slit5.png"),(150,30))
bear24 = transform.scale(image.load("images/Monotaro Slit5.png"),(150,30))
bear34 = transform.scale(image.load("images/Monophanie Slit5.png"),(150,30))
bear44 = transform.scale(image.load("images/Monokid Slit5.png"),(150,30))
bear54 = transform.scale(image.load("images/Monosuke Slit5.png"),(150,30))
bear64 = transform.scale(image.load("images/Monodam Slit5.png"),(150,30))

#LOAD STICKERS
bearStick1 = image.load("images/Monokuma.png")
bearStick2 = image.load("images/Monotaro.png")
bearStick3 = image.load("images/Monophanie.png")
bearStick4 = image.load("images/Monokid.png")
bearStick5 = image.load("images/Monosuke.png")
bearStick6 = image.load("images/Monodam.png")

col = (255,0,0) #default RED boarders
c = (0,0,0) #default BLACK paint
WHITE = (255,255,255)

#DEFAULT CHARS
image1 = 'images/Maki (1).png'
image2 = 'images/Oma (1).png'
image3 = 'images/Kiru (1).png'

char1 = True #first character for normal mode
char2 = False
char3 = False

#DEFAULT BG
screen.blit(image.load('images/RedBG.png'), (0,0))

#DEFAULT COLOUR
draw.rect(screen,c,underRGBRect)

#TITLE
paint = transform.scale(image.load("images/Paint.png"),(350,70))
screen.blit(paint,(125,5))
V3 = transform.scale(image.load("images/V3.png"),(150,75))
screen.blit(V3,(360,5))
#mode text
mode = comicFont.render(("MODE"), True, (255,255,255))
#size text
sizeWord = comicFont.render(("SIZE"), True, (255,255,255))

#centering and mode words
screen.blit(mode,(60-mode.get_width()/2, 450-mode.get_height()/2))
screen.blit(sizeWord,(63-sizeWord.get_width()/2, 22-sizeWord.get_height()/2))
ver1 = comicFont.render(("- NORMAL MODE"), True, (255,255,255))
ver2 = comicFont.render(("- CASUAL MODE"), True, (255,255,255))
ver3 = comicFont.render(("- ELITE MODE"), True, (255,255,255))
screen.blit(ver1,(600-mode.get_width()/2, 40-mode.get_height()/2)) #default mode
changeMode = False
G1Clicked = False #these only become true if the mode changing buttons are clicked
B1Clicked = False
G2Clicked = False
yes = comicFont.render(("YES"), True, (0,0,0)) #for the changing modes options
no = comicFont.render(("NO"), True, (0,0,0))
warn = bigFont.render(("Warning"), True, (255,0,0))
info1 = smallFont.render(("You will lose your progress"), True, (0,0,0))
info2 = smallFont.render(("if you change modes."), True, (0,0,0))
info3 = smallFont.render(("Do you still want to continue?"), True, (0,0,0))

#WHITE CANVAS
canv = Surface((850,670)).convert()
canv.set_alpha(170)
canv.fill((255,255,255))
screen.blit(canv, (125,80))

#WHITE ICON BGS
icon = Surface((40,40)).convert()
icon.set_alpha(130)
icon.fill((255,255,255))

#SOLID COLOUR RECTS
draw.rect(screen, (255,0,0),redRect)
draw.rect(screen, (255,255,0),orgRect)
draw.rect(screen, (0,255,255),yelRect)
draw.rect(screen, (0,255,0),greRect)
draw.rect(screen, (0,0,255),bluRect)
draw.rect(screen, (255,0,255),purRect)
draw.rect(screen, (0,0,0),blRect)
draw.rect(screen, (255,255,255),whRect)

#ICON BGS
screen.blit(icon, pencilRect)
screen.blit(icon, eraserRect)
screen.blit(icon, solRect)
screen.blit(icon, sprayRect)
screen.blit(icon, pickRect)
screen.blit(icon, lineRect)
screen.blit(icon, alphaRect)
screen.blit(icon, undoRect)
screen.blit(icon, redoRect)
screen.blit(icon, saveRect)
screen.blit(icon, loadRect)
screen.blit(icon, rectRect)
screen.blit(icon, ellipseRect)
screen.blit(icon, specialRect)
   
#TOOL ICONS
screen.blit(pencil,pencilRect)
screen.blit(eraser,eraserRect)
screen.blit(brush,solRect)
screen.blit(spray,sprayRect)
screen.blit(picker,pickRect)
screen.blit(line,lineRect)
screen.blit(brush2,alphaRect)
screen.blit(ellip,ellipseRect)
screen.blit(back,undoRect)
screen.blit(forward,redoRect)
screen.blit(rct,rectRect)
screen.blit(flop,(25,355,40,40)) #saveRect
screen.blit(unflop,(70,355,40,40)) #loadRect
screen.blit(heart1,(25,265,30,30)) #default heart1Rect #specialRect

#STICKER ICONS
screen.blit(bear14,(225,755,280,30))
screen.blit(bear24,(225,790,280,30))
screen.blit(bear34,(510,755,280,30))
screen.blit(bear44,(510,790,280,30))
screen.blit(bear54,(795,755,280,30))
screen.blit(bear64,(795,790,280,30))
       
screen.blit(bear13,(200,755,280,30))
screen.blit(bear23,(200,790,280,30))
screen.blit(bear33,(485,755,280,30))
screen.blit(bear43,(485,790,280,30))
screen.blit(bear53,(770,755,280,30))
screen.blit(bear63,(770,790,280,30))
       
screen.blit(bear12,(175,755,280,30))
screen.blit(bear22,(175,790,280,30))
screen.blit(bear32,(460,755,280,30))
screen.blit(bear42,(460,790,280,30))
screen.blit(bear52,(745,755,280,30))
screen.blit(bear62,(745,790,280,30))
       
screen.blit(bear11,(150,755,280,30))
screen.blit(bear21,(150,790,280,30))
screen.blit(bear31,(435,755,280,30))
screen.blit(bear41,(435,790,280,30))
screen.blit(bear51,(720,755,280,30))
screen.blit(bear61,(720,790,280,30))
       
screen.blit(bear1,bearRect1)
screen.blit(bear2,bearRect2)
screen.blit(bear3,bearRect3)
screen.blit(bear4,bearRect4)
screen.blit(bear5,bearRect5)
screen.blit(bear6,bearRect6)

#BLACK COVER FOR STICKERS
over = Surface((280,30)).convert()
over.set_alpha(70)
over.fill((0,0,0))
screen.blit(over, bearRect1)
screen.blit(over, bearRect2)
screen.blit(over, bearRect3)
screen.blit(over, bearRect4)
screen.blit(over, bearRect5)
screen.blit(over, bearRect6)

#PIXEL CHARS
pix1 = transform.scale(image.load('images/Girl PA.png'),(85,85)) #pixel girl
screen.blit(pix1,(20,465))

pix2 = transform.scale(image.load('images/Oma PA.png'),(85,85)) #pixel boy
screen.blit(pix2,(20,565))

pix3 = transform.scale(image.load('images/Kiru PA.png'),(85,85)) #pixel female #2
screen.blit(pix3,(20,665))

#RBA PICKER IMAGE
rgb = image.load('images/RGB Colour.png')
RGB = transform.scale(rgb,(155,200))

start1 = 0 #For line and rect

#DEFAULT BRUSH SIZES
sizeLine = sizeAlpha = sizeSpray = sizeSol = 10
sizeErase= 20
sizeBear1 = sizeBear2 = sizeBear3 = sizeBear4 = sizeBear5 = sizeBear6 = 20
sizeRect = sizeEll = 2
sizeSpec = 20
sizePen = 1
size = "" #this changes for the blitting of the size number text

undos = [""] #index[0] is occupied (to not cause problems with undo redo)
redos = [""]

tool = "" #no tool has been selected
undo = 0
redo = 0
undoCopy = False #this becomes True when mb[0] == 0

running = True
while running:
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
           bg = screen.copy() #for dragging things
           Click1 = mx #initial click for x coordinate
           Click2 = my #initial click for y coordinate
           
           if e.button == 1:
               start1 = e.pos #for Line
               
               if canvasRect.collidepoint(mx,my): 
                   if len(redos) > 1:#if we are drawing after adding to redo list, previous redos are useless
                       redos = [""]
                       redo = 0
                   undobg = screen.subsurface(canvasRect).copy() #copies screen
                   undo += 1 #acts as i in list
                   undos.append(undobg) #adds to undo list

                   

               if undoRect.collidepoint(mx,my):
                      if undoCopy == True:
                           if undo != 0: #if undo button is clicked when canvas is blank, nothing happens
                               redos.append(undos[undo]) #takes from last undo
                               redo += 1
                               screen.blit(undos[undo],(125,80))
                               del undos[undo] #removes from undo list
                               undo -= 1
                               screen.blit(speech, (998,330)) #so previous text doesn't mesh with current text
                               undoCopy = False
                       

           elif e.button == 4:
               #all this is for when user scrolls to change size for individual tools/sticker
               #upper and lower limits are included for specific tools
               if tool == "Line":
                   sizeLine += 1
               elif tool == "Brush":
                   sizeAlpha += 1
                   if sizeAlpha > 25:
                       sizeAlpha = 25
               elif tool == "Pencil":
                  sizePen += 1
               elif tool == "Eraser":
                  sizeErase += 1
               elif tool == "Spray":
                  sizeSpray += 1
               elif tool == "Solid Brush":
                  sizeSol += 1
               elif tool == "Rect":
                  sizeRect += 1
                  screen.blit(bg, (0,0))#to be draggable
               elif tool == "Ellipse":
                  sizeEll += 1
                  screen.blit(bg, (0,0))
               elif tool == "Sticker1":
                  screen.blit(bg, (0,0))#to be draggable
                  sizeBear1 += 5
                  screen.blit(bg, (0,0))#to be draggable
               elif tool == "Sticker2":
                  screen.blit(bg, (0,0))
                  sizeBear2 += 1
               elif tool == "Sticker3":
                  screen.blit(bg, (0,0))
                  sizeBear3 += 5
               elif tool == "Sticker4":
                  screen.blit(bg, (0,0))
                  sizeBear4 += 5
               elif tool == "Sticker5":
                  screen.blit(bg, (0,0))
                  sizeBear5 += 5
               elif tool == "Sticker6":
                  screen.blit(bg, (0,0))
                  sizeBear6 += 5
               elif tool == "Special":
                  sizeSpec += 1
                  if sizeSpec > 50: #bigger heart starts showing flaws
                      sizeSpec = 50
           
           elif e.button == 5:
               #same thing but for scroll down
               if tool == "Line":
                   sizeLine -= 1
                   if sizeLine < 1:
                       sizeLine = 1
               elif tool == "Brush":
                   sizeAlpha -= 1
                   if sizeAlpha < 1:
                       sizeAlpha = 1
               elif tool == "Pencil":
                   sizePen -= 1
                   if sizePen < 1:
                       sizePen = 1
               elif tool == "Eraser":
                  sizeErase -= 1
                  if sizeErase < 1:
                      sizeErase = 1
               elif tool == "Spray":
                   sizeSpray -= 1
                   if sizeSpray < 1:
                       sizeSpray = 1
               elif tool == "Solid Brush":
                  sizeSol -= 1
                  if sizeSol < 1:
                       sizeSol = 1
               elif tool == "Rect":
                  sizeRect -= 1
                  if sizeRect < 0:
                       sizeRect = 0 #filled rect
                  screen.blit(bg, (0,0))
               elif tool == "Ellipse":
                  sizeEll -= 1
                  if sizeEll < 0:
                       sizeEll = 0 #filled ellipse
                  screen.blit(bg, (0,0))
               elif tool == "Sticker1":
                  screen.blit(bg, (0,0))
                  sizeBear1 -= 5
                  if sizeBear1 < 1:
                       sizeBear1 = 1
               elif tool == "Sticker2":
                  screen.blit(bg, (0,0))
                  sizeBear2 -= 5
                  if sizeBear2 < 1:
                       sizeBear2 = 1
               elif tool == "Sticker3":
                  screen.blit(bg, (0,0))
                  sizeBear3 -= 5
                  if sizeBear3 < 1:
                       sizeBear3 = 1
               elif tool == "Sticker4":
                  screen.blit(bg, (0,0))
                  sizeBear4 -= 5
                  if sizeBear4 < 1:
                       sizeBear4 = 1
               elif tool == "Sticker5":
                  screen.blit(bg, (0,0))
                  sizeBear5 -= 5
                  if sizeBear5 < 1:
                       sizeBear5 = 1
               elif tool == "Sticker6":
                  screen.blit(bg, (0,0))
                  sizeBear6 -= 5
                  if sizeBear6 < 1:
                       sizeBear6 = 1
               elif tool == "Special":
                   sizeSpec -= 1
                   if sizeSpec < 3:
                       sizeSpec = 3

        if e.type == MOUSEBUTTONUP:
            undoCopy = True #will only copy canvas if mouse button is unclicked
            if redoRect.collidepoint(mx,my):
                   if len(redos) - 1 < redo: #if redo is clicked for no reason
                       redo -= 1
                   elif str(redos[redo-1]) != "": #if we redo all the way until 1 pos before 0 in list
                       if len(redos) - 1 < redo:
                           redo -= 1
                       undos.append(redos[redo]) #takes from redo list
                       undo += 1
                       screen.blit(redos[redo-1],(125,80)) #-1 because it copied empty canvas
                       del redos[redo] #removes from redo list
                       redo -= 1
                       screen.blit(speech, (998,330)) #so previous text doesn't mesh with current text

            print("Undo:"+ str(undo))
            print("Redo:"+ str(redo))

    #==================================COMMENTS=================================
    if char1 == True:
        comment = commentSet_1 #first charcter uses first list of comments
    elif char2 == True:
        comment = commentSet_2 #second charcter uses second list of comments
    elif char3 == True:
        comment = commentSet_3 #third charcter uses third list of comments

    #===========================================================================
    #===============================DEFAULT CHAR================================
    #default character if "No Tool in Selection"
    if tool == "" and changeMode == False:
        if char1 == True:
            default = transform.scale(image.load(image1),(450,850))
            screen.blit(default,(895,460))
            #Blit speech bubble
            screen.blit(speech, (998,330))

            draw.rect(screen,c,underRGBRect) #if no colour has been picked yet

        elif char2 == True:
            default = transform.scale(image.load(image2),(300,780))
            screen.blit(default,(995,465))
            #Blit speech bubble
            screen.blit(speech, (998,330))

            draw.rect(screen,c,underRGBRect) #if no colour has been picked yet

        elif char3 == True:
            default = transform.scale(image.load(image3),(370,830))
            screen.blit(default,(950,467))
            #Blit speech bubble
            screen.blit(speech, (998,330))

            draw.rect(screen,c,underRGBRect) #if no colour has been picked yet

        #Blit default text
        text = comicFont.render((comment[0]), True, (0,0,0))
        screen.blit(text,(1144-len(comment[0])/2-text.get_width()/2, 390-text.get_height()/2))

    #===========================================================================
   
    #=================================BG EFFECTS================================
    #================================AND REDRAWING==============================

    #================================VERSION====================================
    #when changing modes
    if mb[0] == 1 and girlRect.collidepoint(mx,my): #if modes ever change
        G1Clicked = True
        changeMode = True
    elif mb[0] == 1 and boyRect.collidepoint(mx,my):
        B1Clicked = True
        changeMode = True

    elif mb[0] == 1 and girl2Rect.collidepoint(mx,my):
        G2Clicked = True
        changeMode = True
           
    if changeMode == True:
        #WARNING TEXT AND BUTTONS
        screen.blit(speech, (998,330))
        draw.rect(screen, (0,255,0), yesRect)
        draw.rect(screen, (255,255,255), yesRect, 2)
        draw.rect(screen, (255,0,0), noRect)
        draw.rect(screen, (255,255,255), noRect, 2)
        screen.blit(yes,(1106-yes.get_width()/2, 420-yes.get_height()/2))
        screen.blit(no,(1167-no.get_width()/2, 420-no.get_height()/2))
        screen.blit(warn,(1135-warn.get_width()/2, 358-warn.get_height()/2))
        screen.blit(warn,(1136-warn.get_width()/2, 358-warn.get_height()/2))
        screen.blit(info1,(1136-info1.get_width()/2, 375-info1.get_height()/2))
        screen.blit(info2,(1136-info2.get_width()/2, 387-info2.get_height()/2))
        screen.blit(info3,(1136-info3.get_width()/2, 399-info3.get_height()/2))

        if mb[0] == 1 and yesRect.collidepoint(mx,my):
            if G1Clicked == True: #if mode is changed to girl 1
                draw.rect(screen,WHITE,girlRect,2)
                char1 = True
                char2 = False
                char3 = False
               
                #default BG
                screen.blit(redBG, (0,0))
               
                #===============================RE BLIT=================================
                #TITLE
                screen.blit(paint,(125,5))
                screen.blit(V3,(360,5))
                #mode text
                screen.blit(mode,(60-mode.get_width()/2, 450-mode.get_height()/2))
                screen.blit(ver1,(600-mode.get_width()/2, 40-mode.get_height()/2))
                #size text
                screen.blit(sizeWord,(63-sizeWord.get_width()/2, 22-sizeWord.get_height()/2))
               
                #WHITE CANVAS
                screen.blit(canv, (125,80))

                #SOLID COLOUR RECTS
                draw.rect(screen, (255,0,0),redRect)
                draw.rect(screen, (255,255,0),orgRect)
                draw.rect(screen, (0,255,255),yelRect)
                draw.rect(screen, (0,255,0),greRect)
                draw.rect(screen, (0,0,255),bluRect)
                draw.rect(screen, (255,0,255),purRect)
                draw.rect(screen, (0,0,0),blRect)
                draw.rect(screen, (255,255,255),whRect)
                draw.rect(screen,c,underRGBRect)

                #ICON BGS
                screen.blit(icon, pencilRect)
                screen.blit(icon, eraserRect)
                screen.blit(icon, solRect)
                screen.blit(icon, sprayRect)
                screen.blit(icon, pickRect)
                screen.blit(icon, lineRect)
                screen.blit(icon, alphaRect)
                screen.blit(icon, undoRect)
                screen.blit(icon, redoRect)
                screen.blit(icon, saveRect)
                screen.blit(icon, loadRect)
                screen.blit(icon, rectRect)
                screen.blit(icon, ellipseRect)
                screen.blit(icon, specialRect)
                   
                #TOOL ICONS
                screen.blit(pencil,pencilRect)
                screen.blit(eraser,eraserRect)
                screen.blit(brush,solRect)
                screen.blit(spray,sprayRect)
                screen.blit(picker,pickRect)
                screen.blit(line,lineRect)
                screen.blit(brush2,alphaRect)
                screen.blit(ellip,ellipseRect)
                screen.blit(back,undoRect)
                screen.blit(forward,redoRect)
                screen.blit(rct,rectRect)
                screen.blit(flop,(25,355,40,40)) #saveRect
                screen.blit(unflop,(70,355,40,40)) #loadRect
                screen.blit(heart1,(25,265,30,30)) #default heart1Rect #specialRect

                #STICKER ICONS
                screen.blit(bear14,(225,755,280,30))
                screen.blit(bear24,(225,790,280,30))
                screen.blit(bear34,(510,755,280,30))
                screen.blit(bear44,(510,790,280,30))
                screen.blit(bear54,(795,755,280,30))
                screen.blit(bear64,(795,790,280,30))
                       
                screen.blit(bear13,(200,755,280,30))
                screen.blit(bear23,(200,790,280,30))
                screen.blit(bear33,(485,755,280,30))
                screen.blit(bear43,(485,790,280,30))
                screen.blit(bear53,(770,755,280,30))
                screen.blit(bear63,(770,790,280,30))
                       
                screen.blit(bear12,(175,755,280,30))
                screen.blit(bear22,(175,790,280,30))
                screen.blit(bear32,(460,755,280,30))
                screen.blit(bear42,(460,790,280,30))
                screen.blit(bear52,(745,755,280,30))
                screen.blit(bear62,(745,790,280,30))
                       
                screen.blit(bear11,(150,755,280,30))
                screen.blit(bear21,(150,790,280,30))
                screen.blit(bear31,(435,755,280,30))
                screen.blit(bear41,(435,790,280,30))
                screen.blit(bear51,(720,755,280,30))
                screen.blit(bear61,(720,790,280,30))
                       
                screen.blit(bear1,bearRect1)
                screen.blit(bear2,bearRect2)
                screen.blit(bear3,bearRect3)
                screen.blit(bear4,bearRect4)
                screen.blit(bear5,bearRect5)
                screen.blit(bear6,bearRect6)

                #BLACK COVER FOR STICKERS
                screen.blit(over, bearRect1)
                screen.blit(over, bearRect2)
                screen.blit(over, bearRect3)
                screen.blit(over, bearRect4)
                screen.blit(over, bearRect5)
                screen.blit(over, bearRect6)

                #PIXEL CHARS
                #pixel girl
                screen.blit(pix1,(20,465))

                #pixel boy
                screen.blit(pix2,(20,565))

                #pixel female #2
                screen.blit(pix3,(20,665))
                #=======================================================================
                undos = [""]
                redos = [""] #resets
                undo = 0
                redo = 0
                G1Clicked = changeMode = False #since mode has changed
               
            elif B1Clicked == True:      
                draw.rect(screen,WHITE,boyRect,2)
                char1 = False
                char2 = True
                char3 = False

                #default BG
                screen.blit(purBG, (0,0))
               
                #================================RE BLIT================================
                #TITLE
                screen.blit(paint,(125,5))
                screen.blit(V3,(360,5))
                #mode text
                screen.blit(mode,(60-mode.get_width()/2, 450-mode.get_height()/2))
                screen.blit(ver2,(600-mode.get_width()/2, 40-mode.get_height()/2))
                #size text
                screen.blit(sizeWord,(63-sizeWord.get_width()/2, 22-sizeWord.get_height()/2))
               
                #WHITE CANVAS
                screen.blit(canv, (125,80))

                #SOLID COLOUR RECTS
                draw.rect(screen, (255,0,0),redRect)
                draw.rect(screen, (255,255,0),orgRect)
                draw.rect(screen, (0,255,255),yelRect)
                draw.rect(screen, (0,255,0),greRect)
                draw.rect(screen, (0,0,255),bluRect)
                draw.rect(screen, (255,0,255),purRect)
                draw.rect(screen, (0,0,0),blRect)
                draw.rect(screen, (255,255,255),whRect)
                draw.rect(screen,c,underRGBRect)

                #ICON BGS
                screen.blit(icon, pencilRect)
                screen.blit(icon, eraserRect)
                screen.blit(icon, solRect)
                screen.blit(icon, sprayRect)
                screen.blit(icon, pickRect)
                screen.blit(icon, lineRect)
                screen.blit(icon, alphaRect)
                screen.blit(icon, undoRect)
                screen.blit(icon, redoRect)
                screen.blit(icon, saveRect)
                screen.blit(icon, loadRect)
                screen.blit(icon, rectRect)
                screen.blit(icon, ellipseRect)
                screen.blit(icon, specialRect)
                   
                #TOOL ICONS
                screen.blit(pencil,pencilRect)
                screen.blit(eraser,eraserRect)
                screen.blit(brush,solRect)
                screen.blit(spray,sprayRect)
                screen.blit(picker,pickRect)
                screen.blit(line,lineRect)
                screen.blit(brush2,alphaRect)
                screen.blit(ellip,ellipseRect)
                screen.blit(back,undoRect)
                screen.blit(forward,redoRect)
                screen.blit(rct,rectRect)
                screen.blit(flop,(25,355,40,40)) #saveRect
                screen.blit(unflop,(70,355,40,40)) #loadRect
                screen.blit(heart2,(25,265,30,30)) #starRect #specialRect

                #STICKER ICONS
                screen.blit(bear14,(225,755,280,30))
                screen.blit(bear24,(225,790,280,30))
                screen.blit(bear34,(510,755,280,30))
                screen.blit(bear44,(510,790,280,30))
                screen.blit(bear54,(795,755,280,30))
                screen.blit(bear64,(795,790,280,30))
                       
                screen.blit(bear13,(200,755,280,30))
                screen.blit(bear23,(200,790,280,30))
                screen.blit(bear33,(485,755,280,30))
                screen.blit(bear43,(485,790,280,30))
                screen.blit(bear53,(770,755,280,30))
                screen.blit(bear63,(770,790,280,30))
                       
                screen.blit(bear12,(175,755,280,30))
                screen.blit(bear22,(175,790,280,30))
                screen.blit(bear32,(460,755,280,30))
                screen.blit(bear42,(460,790,280,30))
                screen.blit(bear52,(745,755,280,30))
                screen.blit(bear62,(745,790,280,30))
                       
                screen.blit(bear11,(150,755,280,30))
                screen.blit(bear21,(150,790,280,30))
                screen.blit(bear31,(435,755,280,30))
                screen.blit(bear41,(435,790,280,30))
                screen.blit(bear51,(720,755,280,30))
                screen.blit(bear61,(720,790,280,30))
                       
                screen.blit(bear1,bearRect1)
                screen.blit(bear2,bearRect2)
                screen.blit(bear3,bearRect3)
                screen.blit(bear4,bearRect4)
                screen.blit(bear5,bearRect5)
                screen.blit(bear6,bearRect6)

                #BLACK COVER FOR STICKERS
                screen.blit(over, bearRect1)
                screen.blit(over, bearRect2)
                screen.blit(over, bearRect3)
                screen.blit(over, bearRect4)
                screen.blit(over, bearRect5)
                screen.blit(over, bearRect6)

                #PIXEL CHARS
                #pixel girl
                screen.blit(pix1,(20,465))

                #pixel boy
                screen.blit(pix2,(20,565))

                #pixel female #2
                screen.blit(pix3,(20,665))
                #=======================================================================
                undos = [""]
                redos = [""] #resets
                undo = 0
                redo = 0
                B1Clicked = changeMode = False #since mode has changed

            elif G2Clicked == True:        
                draw.rect(screen,WHITE,girl2Rect,2)
                char1 = False
                char2 = False
                char3 = True

                #default BG
                screen.blit(blueBG, (0,0))
               
                #===============================RE BLIT=================================
                #TITLE
                screen.blit(paint,(125,5))
                screen.blit(V3,(360,5))
                #mode text
                screen.blit(mode,(60-mode.get_width()/2, 450-mode.get_height()/2))
                screen.blit(ver3,(600-mode.get_width()/2, 40-mode.get_height()/2))
                #size text
                screen.blit(sizeWord,(63-sizeWord.get_width()/2, 22-sizeWord.get_height()/2))
               
                #WHITE CANVAS
                screen.blit(canv, (125,80))
               
                #SOLID COLOUR RECTS
                draw.rect(screen, (255,0,0),redRect)
                draw.rect(screen, (255,255,0),orgRect)
                draw.rect(screen, (0,255,255),yelRect)
                draw.rect(screen, (0,255,0),greRect)
                draw.rect(screen, (0,0,255),bluRect)
                draw.rect(screen, (255,0,255),purRect)
                draw.rect(screen, (0,0,0),blRect)
                draw.rect(screen, (255,255,255),whRect)
                draw.rect(screen,c,underRGBRect)

                #ICON BGS
                screen.blit(icon, pencilRect)
                screen.blit(icon, eraserRect)
                screen.blit(icon, solRect)
                screen.blit(icon, sprayRect)
                screen.blit(icon, pickRect)
                screen.blit(icon, lineRect)
                screen.blit(icon, alphaRect)
                screen.blit(icon, undoRect)
                screen.blit(icon, redoRect)
                screen.blit(icon, saveRect)
                screen.blit(icon, loadRect)
                screen.blit(icon, rectRect)
                screen.blit(icon, ellipseRect)
                screen.blit(icon, specialRect)
                   
                #TOOL ICONS
                screen.blit(pencil,pencilRect)
                screen.blit(eraser,eraserRect)
                screen.blit(brush,solRect)
                screen.blit(spray,sprayRect)
                screen.blit(picker,pickRect)
                screen.blit(line,lineRect)
                screen.blit(brush2,alphaRect)
                screen.blit(ellip,ellipseRect)
                screen.blit(back,undoRect)
                screen.blit(forward,redoRect)
                screen.blit(rct,rectRect)
                screen.blit(flop,(25,355,40,40)) #saveRect
                screen.blit(unflop,(70,355,40,40)) #loadRect
                screen.blit(heart3,(25,265,30,30)) #hollow diamondRect #specialRect

                #STICKER ICONS
                screen.blit(bear14,(225,755,280,30))
                screen.blit(bear24,(225,790,280,30))
                screen.blit(bear34,(510,755,280,30))
                screen.blit(bear44,(510,790,280,30))
                screen.blit(bear54,(795,755,280,30))
                screen.blit(bear64,(795,790,280,30))
                       
                screen.blit(bear13,(200,755,280,30))
                screen.blit(bear23,(200,790,280,30))
                screen.blit(bear33,(485,755,280,30))
                screen.blit(bear43,(485,790,280,30))
                screen.blit(bear53,(770,755,280,30))
                screen.blit(bear63,(770,790,280,30))
                       
                screen.blit(bear12,(175,755,280,30))
                screen.blit(bear22,(175,790,280,30))
                screen.blit(bear32,(460,755,280,30))
                screen.blit(bear42,(460,790,280,30))
                screen.blit(bear52,(745,755,280,30))
                screen.blit(bear62,(745,790,280,30))
                       
                screen.blit(bear11,(150,755,280,30))
                screen.blit(bear21,(150,790,280,30))
                screen.blit(bear31,(435,755,280,30))
                screen.blit(bear41,(435,790,280,30))
                screen.blit(bear51,(720,755,280,30))
                screen.blit(bear61,(720,790,280,30))
                       
                screen.blit(bear1,bearRect1)
                screen.blit(bear2,bearRect2)
                screen.blit(bear3,bearRect3)
                screen.blit(bear4,bearRect4)
                screen.blit(bear5,bearRect5)
                screen.blit(bear6,bearRect6)

                #BLACK COVER FOR STICKERS
                screen.blit(over, bearRect1)
                screen.blit(over, bearRect2)
                screen.blit(over, bearRect3)
                screen.blit(over, bearRect4)
                screen.blit(over, bearRect5)
                screen.blit(over, bearRect6)

                #PIXEL CHARS
                #pixel girl
                screen.blit(pix1,(20,465))

                #pixel boy
                screen.blit(pix2,(20,565))

                #pixel female #2
                screen.blit(pix3,(20,665))
                #=======================================================================
                undos = [""]
                redos = [""] #resets
                undo = 0
                redo = 0
                G2Clicked = changeMode = False #since mode has changed = False
               
        elif mb[0] == 1 and noRect.collidepoint(mx,my):
            changeMode = False
            G1Clicked = False
            B1Clicked = False
            G2Clicked = False

    #===========================================================================

    #=============================RECTS ON LEFT=================================
    draw.rect(screen, col,pencilRect,2)
    draw.rect(screen, col,eraserRect,2)
    draw.rect(screen, col,lineRect,2)
    draw.rect(screen, col,undoRect,2)
    draw.rect(screen, col,redoRect,2)
    draw.rect(screen, col,alphaRect,2)
    draw.rect(screen, col,pickRect,2)
    draw.rect(screen, col,sprayRect,2)
    draw.rect(screen, col,solRect,2)
    draw.rect(screen, col,rectRect,2)
    draw.rect(screen, col,ellipseRect,2)
    draw.rect(screen, col,specialRect,2)
    draw.rect(screen, col,saveRect,2)
    draw.rect(screen, col,loadRect,2)
    draw.rect(screen, col,canvasRect,2) #canvas boarder

    screen.blit(RGB, (995,80)) #RGB IMAGE (ON RIGHT)
   
    draw.rect(screen, (255,0,0),girlRect,2) #RED
    draw.rect(screen, (255,0,255),boyRect,2) #PURPLE
    draw.rect(screen, (0,0,255),girl2Rect,2) #BLUE
    #===============================RECTS ON BOTTOM=============================
    draw.rect(screen, col,bearRect1,2)
    draw.rect(screen, col,bearRect2,2)
    draw.rect(screen, col,bearRect3,2)
    draw.rect(screen, col,bearRect4,2)
    draw.rect(screen, col,bearRect5,2)
    draw.rect(screen, col,bearRect6,2)
    #================================RECTS ON RIGHT=============================
    draw.rect(screen,col,redRect,2)
    draw.rect(screen,col,orgRect,2)
    draw.rect(screen,col,yelRect,2)
    draw.rect(screen,col,greRect,2)
    draw.rect(screen,col,bluRect,2)
    draw.rect(screen,col,purRect,2)
    draw.rect(screen,col,blRect,2)
    draw.rect(screen,col,whRect,2)
    #===========================================================================

    #==============================SOLID COLOUR PICK============================
    if mb[0] == 1 and 2262 >= mx >= 1182 and 300 >= my >= 80: #and in the area of colours
        if redRect.collidepoint(mx,my):#RED
            draw.rect(screen,WHITE,redRect,2)
            c = (255,0,0)
            draw.rect(screen,c,underRGBRect)
           
        elif orgRect.collidepoint(mx,my): #YELLOW
            draw.rect(screen,WHITE,orgRect,2)
            c = (255,255,0)
            draw.rect(screen,c,underRGBRect)
           
        elif yelRect.collidepoint(mx,my):#LBLUE
            draw.rect(screen,WHITE,yelRect,2)
            c = (0,255,255)
            draw.rect(screen,c,underRGBRect)
           
        elif greRect.collidepoint(mx,my):#GREEN
            draw.rect(screen,WHITE,greRect,2)
            c = (0,255,0)
            draw.rect(screen,c,underRGBRect)
           
        elif bluRect.collidepoint(mx,my):#DBLUE
            draw.rect(screen,WHITE,bluRect,2)
            c = (0,0,255)
            draw.rect(screen,c,underRGBRect)
           
        elif purRect.collidepoint(mx,my):#PURPLE
            draw.rect(screen,WHITE,purRect,2)
            c = (255,0,255)
            draw.rect(screen,c,underRGBRect)

        elif blRect.collidepoint(mx,my):#BLACK
            draw.rect(screen,WHITE,blRect,2)
            c = (0,0,0)
            draw.rect(screen,c,underRGBRect)

        elif whRect.collidepoint(mx,my):#WHITE
            draw.rect(screen,WHITE,whRect,2)
            c = (255,255,255)
            draw.rect(screen,c,underRGBRect)
    #===========================================================================
    #==================================PICK CHAR================================
    #tools and character variables change according to which tool is selected
    if mb[0] == 1:
        if pencilRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,pencilRect,2) #indicates that box was clicked
            tool = "Pencil"

            image1 = 'images/Maki (2).png'
            image2 = 'images/Oma (11).png'
            image3 = 'images/Kiru (17).png'
       
        elif eraserRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,eraserRect,2)
            tool = "Eraser"

            image1 = 'images/Maki (25).png'
            image2 = 'images/Oma (2).png'
            image3 = 'images/Kiru (9).png'

        elif lineRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,lineRect,2)
            tool = "Line"

            image1 = 'images/Maki (4).png'
            image2 = 'images/Oma (3).png'
            image3 = 'images/Kiru (4).png'
           
        elif undoRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,undoRect,2)

        elif redoRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,redoRect,2)
           
        elif alphaRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,alphaRect,2)
            tool = "Brush"

            image1 = 'images/Maki (53).png'
            image2 = 'images/Oma (5).png'
            image3 = 'images/Kiru (14).png'

        elif pickRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,pickRect,2)
            tool = "Picker"

            image1 = 'images/Maki (11).png'
            image2 = 'images/Oma (9).png'
            image3 = 'images/Kiru (19).png'

        elif sprayRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,sprayRect,2)
            tool = "Spray"

            image1 = 'images/Maki (40).png'
            image2 = 'images/Oma (16).png'
            image3 = 'images/Kiru (20).png'

        elif solRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,solRect,2)
            tool = "Solid Brush"

            image1 = 'images/Maki (42).png'
            image2 = 'images/Oma (17).png'
            image3 = 'images/Kiru (31).png'

        elif rectRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,rectRect,2)
            tool = "Rect"

            image1 = 'images/Maki (9).png'
            image2 = 'images/Oma (4).png'
            image3 = 'images/Kiru (17).png'

        elif ellipseRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,ellipseRect,2)
            tool = "Ellipse"

            image1 = 'images/Maki (27).png'
            image2 = 'images/Oma (15).png'
            image3 = 'images/Kiru (15).png'
           
        elif specialRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,specialRect,2)
            tool = "Special"

            image1 = 'images/Maki (10).png'
            image2 = 'images/Oma (21).png'
            image3 = 'images/Kiru (5).png'
       
    #==================================CHARS====================================
    if mb[0] == 1 and mx < 125 or mb[0] == 1 and mx > 995 or mb[0] == 1 and my > 750: #needs specifics because it lags otherwise
        if char1 == True:
            col = (255,0,0) #RED
            screen.blit(charBG1, (976,412))
            draw.rect(screen, col,canvasRect,2) #canvas boarder

            if tool == "Special" or tool == "Pencil":
                girlBlitX = 960 # because this image is a big bigger
            else:
                girlBlitX = 895
            #default female character
            girl = transform.scale(image.load(image1),(450,850))
            screen.blit(girl,(girlBlitX,460))

            #Blit speech bubble
            screen.blit(speech, (998,330))

        elif char2 == True:
            col = (255,0,255) #PURPLE
            screen.blit(charBG2, (977,411))
            draw.rect(screen, col,canvasRect,2) #canvas boarder

            #default male character
            boy = transform.scale(image.load(image2),(300,780))
            screen.blit(boy,(995,465))

            #Blit speech bubble
            screen.blit(speech, (998,330))

        elif char3 == True:
            col = (0,0,255) #BLUE
            screen.blit(charBG3, (975,412))
            draw.rect(screen, col,canvasRect,2) #canvas boarder

            #default female character #2
            girl2 = transform.scale(image.load(image3),(370,830))
            screen.blit(girl2,(950,467))

            #Blit speech bubble
            screen.blit(speech, (998,330))

    #===========================================================================
    #==============================SAVE AND LOAD================================
    if mb[0] == 1:
        if loadRect.collidepoint(mx,my):
            root.update() #to stop window from opening if previously exited
            result = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")])
            root.update()

            if result:
                root.update()
                BG = image.load(str(result)) #takes the directory information
                BG = transform.scale(BG,(850,670))
                screen.blit(BG, (125,80))
                root.update()
               
        elif saveRect.collidepoint(mx,my):
            root.update()
            result = filedialog.asksaveasfilename() + ".png"#png because image isn't recognized as anything
            root.update()

            if result:
                root.update()
                sav = screen.subsurface(canvasRect)
                image.save(sav,result) #saves where user specified
                root.update()
           
    #===========================================================================
    #==============================SELECT STICKERS==============================
    if my > 750: #if in the sticker area
        if mb[0] == 1:
            if bearRect1.collidepoint(mx,my):
                tool = "Sticker1"
                draw.rect(screen,WHITE,bearRect1,2)
            elif bearRect2.collidepoint(mx,my):
                tool = "Sticker2"
                draw.rect(screen,WHITE,bearRect2,2)
            elif bearRect3.collidepoint(mx,my):
                tool = "Sticker3"
                draw.rect(screen,WHITE,bearRect3,2)
            elif bearRect4.collidepoint(mx,my):
                tool = "Sticker4"
                draw.rect(screen,WHITE,bearRect4,2)
            elif bearRect5.collidepoint(mx,my):
                tool = "Sticker5"
                draw.rect(screen,WHITE,bearRect5,2)
            elif bearRect6.collidepoint(mx,my):
                tool = "Sticker6"
                draw.rect(screen,WHITE,bearRect6,2)
       
    #===========================================================================
    if canvasRect.collidepoint(mx,my):
        #==============================COORDINATES==============================
        draw.rect(screen, col, (1117,20,150,40)) #blits box behind coordinates

        #blitting text for coordinates
        txtPic = comicFont.render((str(mx-125)), True, (255,255,255))
        screen.blit(txtPic,(1155-txtPic.get_width()/2, 40-txtPic.get_height()/2))
        txtPic2 = comicFont.render((str(my-80)), True, (255,255,255))
        screen.blit(txtPic,(1225-txtPic.get_width()/2, 40-txtPic.get_height()/2))
       
        #=======================================================================
        
    #===========================================================================
    #============================SIZES & BLITTING TEXT==========================
    #All this is the loading/blitting/sizing of comments each character says about the tools
    if changeMode == False:
        if tool == "Pencil":
            size = sizePen #needed when drawing the size of tool in use

            title = comicFont.render((toolComment[1]), True, (0,0,0))
            #135*2 = length of speech bubble #we need it to center title text
            screen.blit(title,(1137-len(toolComment[1])/2-title.get_width()/2, 360-title.get_height()/2))

            #Comment from char about tool
            text = comicFont.render((comment[1]), True, (0,0,0))
            screen.blit(text,(1144-len(comment[1])/2-text.get_width()/2, 385-text.get_height()/2))
            if char1 == True or char2 == True:
                text = comicFont.render(("smaller details."), True, (0,0,0)) #second line because text is too long
                screen.blit(text,(1144-len(comment[1])/2-text.get_width()/2, 405-text.get_height()/2))
            elif char3 == True:
                text = comicFont.render(("pencil size."), True, (0,0,0)) #second line because text is too long
                screen.blit(text,(1144-len(comment[1])/2-text.get_width()/2, 405-text.get_height()/2))

        elif tool == "Eraser":
            size = sizeErase

            title = comicFont.render((toolComment[2]), True, (0,0,0))
            screen.blit(title,(1137-len(toolComment[2])/2-title.get_width()/2, 360-title.get_height()/2))
            if char1 == True or char2 == True:
                text = comicFont.render((comment[2]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[2])/2-text.get_width()/2, 395-text.get_height()/2))
            elif char3 == True:
                text = comicFont.render((comment[2]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[2])/2-text.get_width()/2, 385-text.get_height()/2))
                text = comicFont.render(("a mistake."), True, (0,0,0))
                screen.blit(text,(1144-len(comment[2])/2-text.get_width()/2, 405-text.get_height()/2))
           
        elif tool == "Line":
            size = sizeLine

            title = comicFont.render((toolComment[3]), True, (0,0,0))
            screen.blit(title,(1137-len(toolComment[3])/2-title.get_width()/2, 360-title.get_height()/2))

            if char1 == True or char3 == True:
                text = comicFont.render((comment[3]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[3])/2-text.get_width()/2, 395-text.get_height()/2))

            if char2 == True:
                text = comicFont.render((comment[3]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[3])/2-text.get_width()/2, 390-text.get_height()/2))
                text = comicFont.render(("w/size"), True, (0,0,0))
                screen.blit(text,(1144-len("w/size")/2-text.get_width()/2, 410-text.get_height()/2))
           
        elif tool == "Brush":
            size = sizeAlpha

            title = comicFont.render((toolComment[4]), True, (0,0,0))
            screen.blit(title,(1137-len(toolComment[4])/2-title.get_width()/2, 360-title.get_height()/2))

            if char1 == True or char3 == True:
                text = comicFont.render((comment[4]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[4])/2-text.get_width()/2, 395-text.get_height()/2))
            elif char2 == True:
                text = comicFont.render((comment[4]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[4])/2-text.get_width()/2, 390-text.get_height()/2))
                text = comicFont.render(("it'll go"), True, (0,0,0))
                screen.blit(text,(1144-len("it'll go")/2-text.get_width()/2, 410-text.get_height()/2))

        elif tool == "Rect":
            size = sizeRect

            title = comicFont.render((toolComment[5]), True, (0,0,0))
            screen.blit(title,(1137-len(toolComment[5])/2-title.get_width()/2, 360-title.get_height()/2))

            if char1 == True or char2 == True:
                text = comicFont.render((comment[5]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[5])/2-text.get_width()/2, 395-text.get_height()/2))
            elif char3 == True:
                text = comicFont.render((comment[5]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[5])/2-text.get_width()/2, 385-text.get_height()/2))
                text = comicFont.render(("the thickness."), True, (0,0,0))
                screen.blit(text,(1144-len("the thickness.")/2-text.get_width()/2, 405-text.get_height()/2))
                text = comicFont.render(("0 = Filled"), True, (0,0,0))
                screen.blit(text,(1144-len("0 = Filled")/2-text.get_width()/2, 425-text.get_height()/2))

        elif tool == "Picker":
            title = comicFont.render((toolComment[6]), True, (0,0,0))
            screen.blit(title,(1144-len(toolComment[6])/2-title.get_width()/2, 365-title.get_height()/2))

            if char1 == True:
                text = comicFont.render((comment[6]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[6])/2-text.get_width()/2, 390-text.get_height()/2))
                text = comicFont.render(("on screen."), True, (0,0,0))
                screen.blit(text,(1144-len("on screen.")/2-text.get_width()/2, 410-text.get_height()/2))
            elif char2 == True:
                text = comicFont.render((comment[6]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[6])/2-text.get_width()/2, 390-text.get_height()/2))
                text = comicFont.render(("screen"), True, (0,0,0))
                screen.blit(text,(1144-len("screen")/2-text.get_width()/2, 410-text.get_height()/2))
            elif char3 == True:
                text = comicFont.render((comment[6]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[6])/2-text.get_width()/2, 395-text.get_height()/2))

        elif tool == "Spray":
            size = sizeSpray

            title = comicFont.render((toolComment[7]), True, (0,0,0))
            screen.blit(title,(1137-len(toolComment[7])/2-title.get_width()/2, 360-title.get_height()/2))

            if char1 == True or char3 == True:
                text = comicFont.render((comment[7]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[7])/2-text.get_width()/2, 395-text.get_height()/2))
            elif char2 == True:
                text = comicFont.render((comment[7]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[7])/2-text.get_width()/2, 390-text.get_height()/2))
                text = comicFont.render(("dissolve effect"), True, (0,0,0))
                screen.blit(text,(1144-len("dissolve effect")/2-text.get_width()/2, 410-text.get_height()/2))
           
        elif tool == "Solid Brush":
            size = sizeSol

            title = comicFont.render((toolComment[8]), True, (0,0,0))
            screen.blit(title,(1137-len(toolComment[8])/2-title.get_width()/2, 360-title.get_height()/2))

            text = comicFont.render((comment[8]), True, (0,0,0))
            screen.blit(text,(1144-len(comment[8])/2-text.get_width()/2, 395-text.get_height()/2))

        elif tool == "Special":
            size = sizeSpec
                   
            title = comicFont.render((toolComment[9]), True, (0,0,0))
            screen.blit(title,(1137-len(toolComment[9])/2-title.get_width()/2, 360-title.get_height()/2))

            if char1 == True or char2 == True:
                text = comicFont.render((comment[9]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[9])/2-text.get_width()/2, 395-text.get_height()/2))

            elif char3 == True:
                text = comicFont.render((comment[9]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[9])/2-text.get_width()/2, 390-text.get_height()/2))
                text = comicFont.render(("change."), True, (0,0,0))
                screen.blit(text,(1144-len("change.")/2-text.get_width()/2, 410-text.get_height()/2))
           
        elif tool == "Ellipse":
            size = sizeEll

            title = comicFont.render((toolComment[10]), True, (0,0,0))
            screen.blit(title,(1137-len(toolComment[10])/2-title.get_width()/2, 360-title.get_height()/2))

            if char1 == True or char2 == True:
                text = comicFont.render((comment[10]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[10])/2-text.get_width()/2, 395-text.get_height()/2))

            elif char3 == True:#extra text for char3
                text = comicFont.render((comment[10]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[10])/2-text.get_width()/2, 390-text.get_height()/2))
                text = comicFont.render(("bottom right."), True, (0,0,0))
                screen.blit(text,(1144-len("bottom right.")/2-text.get_width()/2, 410-text.get_height()/2))
            
        elif tool == "Sticker1" or tool == "Sticker2" or tool == "Sticker3" or tool == "Sticker4" or tool == "Sticker5" or tool == "Sticker6":
            title = comicFont.render((toolComment[11]), True, (0,0,0))
            screen.blit(title,(1137-len(toolComment[11])/2-title.get_width()/2, 360-title.get_height()/2))

            if char1 == True:
                text = comicFont.render((comment[11]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[11])/2-text.get_width()/2, 390-text.get_height()/2))
                text = comicFont.render(("to change size"), True, (0,0,0))
                screen.blit(text,(1144-len("to change size")/2-text.get_width()/2, 410-text.get_height()/2))
            elif char2 == True:
                text = comicFont.render((comment[11]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[11])/2-text.get_width()/2, 390-text.get_height()/2))
                text = comicFont.render(("REALLY big"), True, (0,0,0))
                screen.blit(text,(1144-len("REALLY big")/2-text.get_width()/2, 410-text.get_height()/2))
               
            elif char3 == True:
                text = comicFont.render((comment[11]), True, (0,0,0))
                screen.blit(text,(1144-len(comment[11])/2-text.get_width()/2, 390-text.get_height()/2))
                text = comicFont.render(("making them small."), True, (0,0,0))
                screen.blit(text,(1144-len("making them small.")/2-text.get_width()/2, 410-text.get_height()/2))
               
            if tool == "Sticker1":
                size = sizeBear1

            elif tool == "Sticker2":
                size = sizeBear2

            elif tool == "Sticker3":
                size = sizeBear3

            elif tool == "Sticker4":
                size = sizeBear4

            elif tool == "Sticker5":
                size = sizeBear5

            elif tool == "Sticker6":
                size = sizeBear6
           
        draw.rect(screen, col, (20,40,85,30)) #bg for size
           
        szPic = comicFont.render((str(size)), True, (255,255,255)) #size of brush in use
        screen.blit(szPic,(63-szPic.get_width()/2, 55-szPic.get_height()/2))

    #===========================================================================

    #================================DRAWING====================================
           
    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
           
        screen.set_clip(canvasRect)
       
        if tool == "Pencil":
            draw.line(screen, c, (omx,omy), (mx,my), sizePen)
   
        elif tool == "Eraser":
            if char1 == True:#which colour bg to blit
                #the area in which image is covered (to erase)
                rubRect = (mx-sizeErase/2,my-sizeErase/2,sizeErase,sizeErase)
                screen.blit(redBG,rubRect,(mx-sizeErase/2,my-sizeErase/2,sizeErase,sizeErase))
                screen.blit(canv, rubRect,(mx-sizeErase/2-125,my-sizeErase/2-80,sizeErase,sizeErase))
               
            elif char2 == True:
                rubRect = (mx-sizeErase/2,my-sizeErase/2,sizeErase,sizeErase)
                screen.blit(purBG,rubRect,(mx-sizeErase/2,my-sizeErase/2,sizeErase,sizeErase))
                screen.blit(canv, rubRect,(mx-sizeErase/2,my-sizeErase/2,sizeErase,sizeErase))
               
            elif char3 == True:
                rubRect = (mx-sizeErase/2,my-sizeErase/2,sizeErase,sizeErase)
                screen.blit(blueBG,rubRect,(mx-sizeErase/2,my-sizeErase/2,sizeErase,sizeErase))
                screen.blit(canv, rubRect,(mx-sizeErase/2,my-sizeErase/2,sizeErase,sizeErase))
               
           
        elif tool == "Line":
            screen.blit(bg,(0,0))
            draw.line(screen, c, start1,(mx,my), sizeLine)

        elif tool == "Spray":
            for i in range(sizeSpray):
                x1 = randint(-sizeSpray,sizeSpray)
                y1 = randint(-sizeSpray,sizeSpray)
                draw.line(screen, c, (mx + x1,my + y1), (mx + x1,my + y1),1)

        elif tool == "Brush":
            #==========================FOR ALPHA BRUSH==========================

            if sizeAlpha > 25: #don't want circle to become a square
                sizeAlpha = 25
           
            cover = Surface((50,50)).convert()  # make blank Surface
            cover.set_alpha(10)
            cover.fill((255,0,255))
            cover.set_colorkey((255,0,255))
            draw.circle(cover,c,(25,25),sizeAlpha)

            #===================================================================
            screen.blit(cover,(mx-25,my-25))

        elif tool == "Solid Brush":
            draw.circle(screen, c, (mx,my), sizeSol)

        elif tool == "Rect":
            screen.blit(bg,(0,0))
            draw.rect(screen,c,(Click1,Click2,mx-Click1,my-Click2),sizeRect)

        elif tool == "Ellipse":
            screen.blit(bg,(0,0)) #for dragging

            #distance between the initial point and current mouse position
            newX = mx-Click1 
            newY = my-Click2
            
            newEllRect = Rect(Click1,Click2,newX if newX > sizeEll*2 else sizeEll*2,newY if newY > sizeEll*2 else sizeEll*2) #area to be drawn in
            #can't be smaller than twice the width 
            newEllRect.normalize()
            draw.ellipse(screen,c, newEllRect,sizeEll if sizeEll < max(newX,newY) else 0) #so width isn't greater

        elif tool == "Special": 
            if char1 == True:#red
                col2 = (randint(0,255))
                col3 = 0
                col4 = 0

                #heart shaped polygon
                draw.circle(screen, (col2,col3,col4), (mx-sizeSpec,my-sizeSpec), sizeSpec)#right circle
                draw.circle(screen, (col2,col3,col4), (mx+sizeSpec+1,my-sizeSpec), sizeSpec)#left circle
                #math below makes triangle proportional and fit with the circles
                draw.polygon(screen, (col2,col3,col4), ((mx-round(sizeSpec*1.67),my-round(sizeSpec*0.3)),(mx+round(sizeSpec*1.67),my-round(sizeSpec*0.3)),(mx,my+round(sizeSpec*1.5))))#bottom triangle
                #covering hole in the middle w/Rect
                draw.rect(screen, (col2,col3,col4), (mx-round(sizeSpec/2),my-round(sizeSpec),round(sizeSpec),round(sizeSpec)))
                
            elif char2 == True:#purple
                col2 = randint(0,255)
                col3 = 0
                col4 = col2

                #1) needs be same size as heart #therefore similar numbers
                #2) triangle + inverted triiangle = star
                draw.polygon(screen, (col2,col3,col4), ((mx-round(sizeSpec*1.5),my-round(sizeSpec*0.3)),(mx+round(sizeSpec*1.5),my-round(sizeSpec*0.3)),(mx,my+round(sizeSpec*2))))
                draw.polygon(screen, (col2,col3,col4), ((mx-round(sizeSpec*1.5),my+round(sizeSpec*1.3)),(mx+round(sizeSpec*1.5),my+round(sizeSpec*1.3)),(mx,my-round(sizeSpec))))

            elif char3 == True:#blue
                col2 = 0
                col3 = 0
                col4 = randint(0,255)

                #fancy diamond shape
                draw.polygon(screen, (col2,col3,col4), ((mx-round(sizeSpec*0.8),my-round(sizeSpec*0.3)),(mx-round(sizeSpec*0.8),my+round(sizeSpec*0.3)),(mx,my-round(sizeSpec*2))))
                draw.polygon(screen, (col2,col3,col4), ((mx-round(sizeSpec*0.8),my-round(sizeSpec*0.3)),(mx-round(sizeSpec*0.8),my+round(sizeSpec*0.3)),(mx,my+round(sizeSpec*2))))
                draw.polygon(screen, (col2,col3,col4), ((mx+round(sizeSpec*0.8),my-round(sizeSpec*0.3)),(mx+round(sizeSpec*0.8),my+round(sizeSpec*0.3)),(mx,my-round(sizeSpec*2))))
                draw.polygon(screen, (col2,col3,col4), ((mx+round(sizeSpec*0.8),my-round(sizeSpec*0.3)),(mx+round(sizeSpec*0.8),my+round(sizeSpec*0.3)),(mx,my+round(sizeSpec*2))))
                
        elif tool == "Sticker1":
            bearImage1 = transform.scale(bearStick1,(80+sizeBear1,139+sizeBear1))
            screen.blit(bg,(0,0))# to be draggable
            screen.blit(bearImage1, (mx-bearImage1.get_width()/2, my-bearImage1.get_height()/2)) #so mouse stays centered
           
        elif tool == "Sticker2":
            bearImage2 = transform.scale(bearStick2,(80+sizeBear2,139+sizeBear2))
            screen.blit(bg,(0,0))
            screen.blit(bearImage2, (mx-bearImage2.get_width()/2, my-bearImage2.get_height()/2))
           
        elif tool == "Sticker3":
            bearImage3 = transform.scale(bearStick3,(53+sizeBear3,137+sizeBear3))
            screen.blit(bg,(0,0))
            screen.blit(bearImage3, (mx-bearImage3.get_width()/2, my-bearImage3.get_height()/2))
           
        elif tool == "Sticker4":
            bearImage4 = transform.scale(bearStick4,(65+sizeBear4,142+sizeBear4))
            screen.blit(bg,(0,0))
            screen.blit(bearImage4, (mx-bearImage4.get_width()/2, my-bearImage4.get_height()/2))
           
        elif tool == "Sticker5":
            bearImage5 = transform.scale(bearStick5,(60+sizeBear5,139+sizeBear5))
            screen.blit(bg,(0,0))
            screen.blit(bearImage5, (mx-bearImage5.get_width()/2, my-bearImage5.get_height()/2))
           
        elif tool == "Sticker6":
            bearImage6 = transform.scale(bearStick6,(90+sizeBear6,139+sizeBear6))
            screen.blit(bg,(0,0))
            screen.blit(bearImage6, (mx-bearImage6.get_width()/2, my-bearImage6.get_height()/2))
       
        screen.set_clip(None)

        if tool == "Picker":
            c = screen.get_at((mx,my))
            draw.rect(screen,c,underRGBRect) #blits outside canvas and needs to be outside screen.set_clip()

    if mb[0] == 1 and rgbRect.collidepoint(mx,my): #if in area of RGB
        c = screen.get_at((mx,my))
        draw.rect(screen,c,underRGBRect)

    omx,omy = mx,my #for pencil connection
    #print(tool)
    display.flip()


quit()
