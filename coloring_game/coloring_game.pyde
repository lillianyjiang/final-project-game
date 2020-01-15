hue = 0

def create_circle(x, y, radius, fill_color, stroke_color):
    custom_circle = createShape(ELLIPSE, x, y, radius * 2, radius * 2)
    custom_circle.fill(fill_color)
    custom_circle.stroke(stroke_color)
    custom_circle.endShape()
    return custom_circle


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
    global blue_zigzag
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
    
    # create a light green triangle
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
    
    #create a blue zigzag 
    blue_zigzag = createShape()
    blue_zigzag.beginShape()
    blue_zigzag.fill(color(0, 0, 100))
    blue_zigzag.stroke(color(187, 23, 90))
    blue_zigzag.vertex(200, 20)
    blue_zigzag.vertex(220, 30)
    blue_zigzag.vertex(220, 50)
    blue_zigzag.vertex(240, 70)
    blue_zigzag.vertex(240, 90)
    blue_zigzag.vertex(200, 50)
    blue_zigzag.vertex(200, 20)
    blue_zigzag.endShape()
    
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
    
def draw():
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
    shape(blue_zigzag)
    shape(reset_button)
    textSize(32)
    fill(0)
    text("reset", 10, 30)
    
def mouseInRect(x, y, x2, y2):
    return mouseY > y and mouseY < y2 and mouseX > x and mouseX < x2
    
def mousePressed():
    # runs once each time mouse is pressed

    #for orange_triangle
    if mouseX < width/7.5 and mouseY < height/5:
        orange_triangle.setFill(color(33, 100, 100))
        
    # for a yellow triangle 
    if dist(mouseX,mouseY, 450,62.5) < 25 :
        yellow_triangle.setFill(color(60, 100, 100))
        
    # for a purple triangle 
    if dist(mouseX,mouseY, 330,320) < 25 :
        purple_triangle.setFill(color(249, 56, 93))

    # for a green triangle 
    if dist(mouseX,mouseY, 425,200) < 25 :
        green_triangle.setFill(color(120, 39, 98))
    
    #for blue_square
    if mouseInRect(100, 200, 200, 300):
        blue_square.setFill(color(207, 61, 71))

    #for pink_square
    if mouseInRect(500,100,600,200):
        pink_square.setFill(color(305, 24, 100))

    #for purple_rectangle
    if mouseInRect(80,60,180,120):
        purple_rectangle.setFill(color(300, 100, 50))
    
    #for green_rectangle 
    if mouseInRect(250, 100, 300, 200):
        green_rectangle.setFill(color(143, 71, 63))
        
    #for yellow_circle
    if dist(mouseX,mouseY, 100,300) < 60 :
        yellow_circle.setFill(color(60, 100, 100))
        
    # for a pink_circle
    if dist(mouseX,mouseY, 500,300) < 50 :
        pink_circle.setFill(color(340, 49, 86))
        
    # for a blue circle
    if dist(mouseX, mouseY, 300, 200) <40:
        blue_circle.setFill(color(195, 100, 100))
        
    # for a blue_zigzag 
    
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
        
        
    
