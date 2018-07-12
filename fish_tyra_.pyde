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
    
           
                         
                
def setColor (colorName):
    if colorName == "orange" :
       fill(255, 128, 0)
      
    elif colorName == "green" :
         fill(0, 0, 255,)
