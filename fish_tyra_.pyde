xSpeed=2
xCoordinate = random (50, 200)



def setup():
    size(400,400)
    background(0, 0, 255)
    fish(200,200,40,30)
    setColor("orange")
    tail(220,200,250,220,250,180)
     
    
 
       
def fish(xCoordinate, yCoordinate, fishwidth, fisheight):
    fill(255, 128, 0)
    ellipse(xCoordinate, yCoordinate, fishwidth, fisheight)
    
    
    
def tail(xCoordinate, yCoordinate, talex, taley, tale1, tale2):
    fill(255, 128, 0)
    triangle(xCoordinate, yCoordinate, talex, taley, tale1, tale2)
    
# def draw(): 
#     global xCoordinate, tail, xSpeed, fish
#        leftBoundary = fish/2
#        rightBoundary = 400 - fish/2
#     if xCoordinate >= rightBoundary or xCoordinate <= leftBoundary:
#        xSpeed = -xSpeed
#     xCoordinate += xSpeed
    
           
                         
                
def setColor (colorName):
    if colorName == "orange" :
       fill(255, 128, 0)
      
    elif colorName == "green" :
         fill(0, 0, 255,)
