xCoordinate = 400
speed = -8
yCoordinate = 650
yspeed = -8
side = 800
breadth = 700
ellipseSize = 30
rectCoordX = 340

brick1 = True
brick2 = True
brick3 = True
brick4 = True
brick5 = True
brick6 = True
paddle = True




def setup():
    global side
    size(side, breadth)
    background(0)
    
def draw():

    global xCoordinate, speed, yspeed, yCoordinate, red, green, blue, ellipseSize, xCoordinate1, speed1, yspeed1
    global yCoordinate1, rectCoordX, brick1, brick2, brick3, brick4, brick5, brick6
    background(0)
    
   
    
   
    
    topBoundary = ellipseSize / 2
    bottomBoundary = breadth - ellipseSize / 2
    layer2 = 60
    
    leftBoundary = ellipseSize / 2
    rightBoundary = side - ellipseSize / 2
    
    xCoordinate += speed
    yCoordinate += yspeed
    
    
    if xCoordinate >= rightBoundary or xCoordinate <= leftBoundary:
        speed = -speed
    if yCoordinate <= topBoundary:
        yspeed = -yspeed
    
    
    if brick1:
        rect(0, 0, 147, 30)
    if brick2:
        rect(130, 0, 147, 30)
    if brick3:
        rect(260, 0, 147, 30)
    if brick4:
        rect(390, 0, 147, 30)
    if brick5:
        rect(520, 0, 147, 30)
    if brick6:
        rect(650, 0, 149, 30)
    if paddle:
        rect(mouseX, 650, 130, 30, 100, 100, 100, 100)
    if yCoordinate <= 30: 
        if brick1 and xCoordinate <=147:
            brick1 = False
        elif brick2 and xCoordinate>147 and xCoordinate <= 294:
            brick2 = False
        elif brick3 and xCoordinate>294 and xCoordinate <= 420:
            brick3 = False
        elif brick4 and xCoordinate>420 and xCoordinate <= 588:
            brick4 = False
        elif brick5 and xCoordinate>588 and xCoordinate <= 735:
            brick5 = False
        elif brick6 and xCoordinate>735 and xCoordinate <= 882:
            brick6 = False
    if paddle and (xCoordinate >=  mouseX and xCoordinate <= mouseX+130) and (yCoordinate >= 635 and yCoordinate <= 665):
            yspeed = -yspeed
        
        
        
    fill(255)
    ellipse(xCoordinate, yCoordinate, ellipseSize, ellipseSize)
    
    if brick1 == False and brick2 == False and brick3 == False and brick4 == False and brick5 == False and brick6 == False:
        print("GAME OVER")
    
    

   


           
    
     
      
       
        
         
          
           
            
             
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
    
