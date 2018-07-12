xCoordinate = 400
speed = 4
yCoordinate = 200
yspeed = 4
red = random (0, 255)
green = random(0,255)
blue = random(0, 255)
side = 800
breadth = 700
ellipseSize = 30
rectCoordX = 340





xCoordinate1 = 785
yCoordinate1 = 685
speed1 = 5
yspeed1 = 5





def setup():
    global side
    size(side, breadth)
    background(0)
    
def draw():

    global xCoordinate, speed, yspeed, yCoordinate, red, green, blue, ellipseSize, xCoordinate1, speed1, yspeed1
    global yCoordinate1, rectCoordX
    background(0)
    
    rect(0, 0, 147, 30)
    rect(130, 0, 147, 30)
    rect(260, 0, 147, 30)
    rect(390, 0, 147, 30)
    rect(520, 0, 147, 30)
    rect(650, 0, 149, 30)
    
    rect(60, 30, 147, 30)
    rect(190, 30, 147, 30)
    rect(320, 30, 147, 30)
    rect(450, 30, 147, 30)
    rect(580, 30, 147, 30)
    
   
    
    topBoundary = ellipseSize / 2
    bottomBoundary = breadth - ellipseSize / 2
    layer2 = 60
    
    leftBoundary = ellipseSize / 2
    rightBoundary = side - ellipseSize / 2
    
    xCoordinate += speed
    yCoordinate += yspeed
    xCoordinate1 -= speed1
    yCoordinate1 -= yspeed1
    
    
    if xCoordinate >= rightBoundary or xCoordinate <= leftBoundary:
        speed = -speed
    if yCoordinate == layer2 or yCoordinate <= topBoundary:
        yspeed = -yspeed
    if (yCoordinate >= 645 and yCoordinate <= 665) or yCoordinate <= topBoundary:
        yspeed = -yspeed
    
    fill(255)
    ellipse(xCoordinate, yCoordinate, ellipseSize, ellipseSize)
    
    
    def mouseDragged():
        global rectCoordX
    if mouseX >= 340:
        rect(pmouseX, 650, 130, 30)
    else:
        rect(pmouseX, 650, 130, 30)

           
    
     
      
       
        
         
          
           
            
             
    # second ellipse
    #if xCoordinate1 >= rightBoundary or xCoordinate1 <= leftBoundary:
     #   speed1 = -speed1
      #  red = random(255)
        #green = random(255)
        #blue = random(255)
    #if yCoordinate1 >= bottomBoundary or yCoordinate1 <= topBoundary:
       # yspeed1 = -yspeed1
       # red += random(255)
       # green += random(255)
       # blue += random(255)
    #fill(red, green, blue)
    #ellipse(xCoordinate1, xCoordinate1, ellipseSize, ellipseSize)
    
