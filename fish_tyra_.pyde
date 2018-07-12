xSpeed=2
xCoordinate = random (50, 200)



def setup():
    size(400,400)
    background(0, 0, 255)
    fish(200,200)
    setColor("orange")
    
     
    
 
       
def fish(xCoordinate, yCoordinate):
    fill(255, 128, 0)
    ellipse(xCoordinate, yCoordinate, 40,30)
    triangle(xCoordinate + 20, yCoordinate, xCoordinate + 50, xCoordinate + 20, xCoordinate + 50, xCoordinate - 20)
    
   
                                  
                
def setColor (colorName):
    if colorName == "orange" :
       fill(255, 128, 0)
      
    elif colorName == "green" :
         fill(0, 0, 255,)
