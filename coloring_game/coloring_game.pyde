hue = 0
# count stores how many elements have been filled in
# every time you fill in a shape it updates the color array 
count = 0
colored = []

# function to create a circle 
def create_circle(x, y, radius, fill_color, stroke_color):
    custom_circle = createShape(ELLIPSE, x, y, radius * 2, radius * 2)
    custom_circle.fill(fill_color)
    custom_circle.stroke(stroke_color)
    custom_circle.endShape()
    return custom_circle

# function for creating the shapes
def setup():
    global orange_triangle
    global yellow_triangle
    global purple_triangle
    global green_triangle
    global blue_square
    global pink_square
    global purple_rectangle
    global green_rectangle
    global yellow_circle
    global pink_circle
    global blue_circle
    global red_circle
    global reset_button
    
    size(600,400)
    colorMode(HSB, 360, 100, 100)
    background(0, 0, 100)
    
    # create orange triangle 
    orange_triangle = createShape()
    orange_triangle.beginShape()
    orange_triangle.fill(color(0,0,100))
    orange_triangle.stroke(0)
    orange_triangle.stroke(color(33, 100, 100))
    orange_triangle.strokeWeight(3)
    orange_triangle.vertex(0, 10)
    orange_triangle.vertex(50, 80)
    orange_triangle.vertex(40,20)
    orange_triangle.vertex(0,10)
    orange_triangle.endShape()

    # create a yellow triangle
    yellow_triangle = createShape()
    yellow_triangle.beginShape()
    yellow_triangle.fill(color(0,0,100))
    yellow_triangle.stroke(0)
    yellow_triangle.stroke(color(60, 100, 100))
    yellow_triangle.vertex(500, 50)
    yellow_triangle.vertex(400, 50)
    yellow_triangle.vertex(450, 75)
    yellow_triangle.vertex(500,50)
    yellow_triangle.endShape()
    
    # create a purple triangle
    purple_triangle = createShape()
    purple_triangle.beginShape()
    purple_triangle.fill(color(0,0,100))
    purple_triangle.stroke(0)
    purple_triangle.stroke(color(249, 56, 93))
    purple_triangle.vertex(300, 300)
    purple_triangle.vertex(400, 300)
    purple_triangle.vertex(325, 350 )
    purple_triangle.vertex(300,300)
    purple_triangle.endShape()
    
    # create a green triangle
    green_triangle = createShape()
    green_triangle.beginShape()
    green_triangle.fill(color(0,0,100))
    green_triangle.stroke(0)
    green_triangle.stroke(color(120, 39, 98))
    green_triangle.vertex(425, 150)
    green_triangle.vertex(400, 230)
    green_triangle.vertex(450, 250)
    green_triangle.vertex(425, 150)
    green_triangle.endShape()
    
    # create a blue square 
    blue_square = createShape()
    blue_square.beginShape()
    blue_square.fill(color(0,0,100))
    blue_square.stroke(0)
    blue_square.stroke(color(207, 61, 71))
    blue_square.vertex(100,200)
    blue_square.vertex(200,200)
    blue_square.vertex(200,300)
    blue_square.vertex(100,300)
    blue_square.vertex(100,200)
    blue_square.endShape()

    #create a pink square 
    pink_square = createShape()
    pink_square.beginShape()
    pink_square.fill(color(0,0,100))
    pink_square.stroke(0)
    pink_square.stroke(color(305, 24, 100))
    pink_square.vertex(500,200)
    pink_square.vertex(500,100)
    pink_square.vertex(600,100)
    pink_square.vertex(600,200)
    pink_square.vertex(500,200)
    pink_square.endShape()
    
    #create purple_rectangle 
    purple_rectangle = createShape()
    purple_rectangle.beginShape()
    purple_rectangle.fill(color(0,0,100))
    purple_rectangle.stroke(0)
    purple_rectangle.stroke(color(300, 100, 50))
    purple_rectangle.vertex(80,60)
    purple_rectangle.vertex(80,120)
    purple_rectangle.vertex(180,120)
    purple_rectangle.vertex(180,60)
    purple_rectangle.vertex(80,60)
    purple_rectangle.endShape()
       
    # create a green rectangle 
    green_rectangle = createShape()
    green_rectangle.beginShape()
    green_rectangle.fill(color(0,0,100))
    green_rectangle.stroke(0)
    green_rectangle.stroke(color(143, 71, 63))
    green_rectangle.vertex(250,100)
    green_rectangle.vertex(250,200)
    green_rectangle.vertex(300,200)
    green_rectangle.vertex(300,100)
    green_rectangle.vertex(250,100)
    green_rectangle.endShape()
    
    # create a yellow cricle
    yellow_circle = create_circle(100, 300, 60, color(255), color(0))
    
    # create a pink circle
    pink_circle = create_circle(500, 300, 50, color(255), color(0))
    
    # create a blue circle 
    blue_circle = create_circle(300, 200, 40, color(195), color(0))
    
    #create a red circle 
    red_circle = create_circle(250, 50, 30, color(195), color(0))

    
    #create a reset button
    reset_button= createShape()
    reset_button.beginShape()
    reset_button.fill(color(0, 100, 100))
    reset_button.stroke(0)
    reset_button.stroke(color(0, 100, 100))
    reset_button.vertex(600,0)
    reset_button.vertex(600,25)
    reset_button.vertex(550,25)
    reset_button.vertex(550,0)
    reset_button.vertex(600,0)
    reset_button.endShape()
    
    for i in range(12):
        colored.append(False)
    
#function for drawing the shapes
def draw():
    # when all the shapes have been filled in (the count is full) it sets the background color as salmon 
    if count == 12: 
        background(color(5,55,100))
    else:
        background(color(0, 0, 100));
    shape(orange_triangle)
    shape(yellow_triangle)
    shape(purple_triangle)
    shape(green_triangle)
    shape(blue_square)
    shape(pink_square)
    shape(purple_rectangle)
    shape(green_rectangle)
    shape(yellow_circle)
    shape(pink_circle)
    shape(blue_circle)
    shape(red_circle)
    shape(reset_button)
    textSize(20)
    fill(0)
    text("reset", 550, 20)
    
# function for coloring an object in a rectangle 
def mouseInRect(x, y, x2, y2):
    return mouseY > y and mouseY < y2 and mouseX > x and mouseX < x2
    
# runs once each time mouse is pressed
def mousePressed():
    global count
    
    #for orange_triangle
    if mouseX < width/7.5 and mouseY < height/5:
        orange_triangle.setFill(color(33, 100, 100))
        if not colored[0]:
            count += 1
            colored[0] = True
        
    # for a yellow triangle 
    if dist(mouseX,mouseY, 450,62.5) < 25 :
        yellow_triangle.setFill(color(60, 100, 100))
        if not colored[1]:
            count += 1
            colored[1] = True
        
    # for a purple triangle 
    if dist(mouseX,mouseY, 330,320) < 25 :
        purple_triangle.setFill(color(249, 56, 93))
        if not colored[2]:
            count += 1
            colored[2] = True

    # for a green triangle 
    if dist(mouseX,mouseY, 425,200) < 25 :
        green_triangle.setFill(color(120, 39, 98))
        if not colored[3]:
            count += 1
            colored[3] = True
    #for blue_square
    if mouseInRect(100, 200, 200, 300):
        blue_square.setFill(color(207, 61, 71))
        if not colored[4]:
            count += 1
            colored[4] = True

    #for pink_square
    if mouseInRect(500,100,600,200):
        pink_square.setFill(color(305, 24, 100))
        if not colored[5]:
            count += 1
            colored[5] = True

    #for purple_rectangle
    if mouseInRect(80,60,180,120):
        purple_rectangle.setFill(color(300, 100, 50))
        if not colored[6]:
            count += 1
            colored[6] = True
    
    #for green_rectangle 
    if mouseInRect(250, 100, 300, 200):
        green_rectangle.setFill(color(143, 71, 63))
        if not colored[7]:
            count += 1
            colored[7] = True
        
    #for yellow_circle
    if dist(mouseX,mouseY, 100,300) < 60 :
        yellow_circle.setFill(color(60, 100, 100))
        if not colored[8]:
            count += 1
            colored[8] = True
        
    # for a pink_circle
    if dist(mouseX,mouseY, 500,300) < 50 :
        pink_circle.setFill(color(340, 49, 86))
        if not colored[9]:
            count += 1
            colored[9] = True
        
    # for a blue circle
    if dist(mouseX, mouseY, 300, 200) <40:
        blue_circle.setFill(color(195, 100, 100))
        if not colored[10]:
            count += 1
            colored[10] = True
        
    # for a red circle
    if dist(mouseX, mouseY, 250, 50) <30:
        red_circle.setFill(color(348, 91, 86))
        if not colored[11]:
            count += 1
            colored[11] = True
        
    # a reset button 
    if mouseInRect(550,0,600,25):
        orange_triangle.setFill(color(0, 0, 100))
        yellow_triangle.setFill(color(0, 0, 100))
        purple_triangle.setFill(color(0, 0, 100))
        green_triangle.setFill(color(0, 0, 100))
        blue_square.setFill(color(0, 0, 100))
        pink_square.setFill(color(0, 0, 100))
        purple_rectangle.setFill(color(0, 0, 100))
        green_rectangle.setFill(color(0, 0, 100))
        yellow_circle.setFill(color(0, 0, 100))
        pink_circle.setFill(color(0, 0, 100))
        blue_circle.setFill(color(0, 0, 100))
        red_circle.setFill(color(0,0,100))
        
        for i in range(12):
            colored[i] = False
        count = 0
