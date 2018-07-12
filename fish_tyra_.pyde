xSpeed=2
xCoordinate = random (50, 200)
ySpeed=2
yCoordinate = random (50, 200)
    
def setup():
    size(700,500)
    background(0, 0, 255)
    setColor("green")
    fish(200,200)
    setColor("orange")
    fish(350,350)

    
     
    
 
       
def fish(xCoordinate, yCoordinate):
   
    ellipse(xCoordinate, yCoordinate, 40,30)
    triangle(xCoordinate + 20, yCoordinate, xCoordinate + 50, xCoordinate + 20, xCoordinate + 50, xCoordinate - 20)
    
def draw():
    global xCoordinate, yCoordinate, ySpeed, xSpeed, fish
          
    
    yCoordinate = yCoordinate + ySpeed
    xCoordinate += ySpeed   
                                  
                
def setColor (colorName):
    if colorName == "orange" :
       fill(255, 128, 0)
      
    if colorName == "green" :
         fill(0, 128, 0)
