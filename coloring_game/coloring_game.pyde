hue = 0

def create_circle(x, y, radius, fill_color, stroke_color):
    custom_circle = createShape(ELLIPSE, x, y, radius * 2, radius * 2)
    custom_circle.fill(fill_color)
    custom_circle.stroke(stroke_color)
    custom_circle.endShape()
    return custom_circle

def setup():
    global orange_triangle
    global blue_square
    global pink_square
    global purple_rectangle
    global green_rectangle
    global yellow_circle
    global pink_circle
    global blue_circle
    global yellow_triangle
    global purple_triangle
    
    size(600,400)
    colorMode(HSB, 360, 100, 100)
    background(0, 0, 100)
    
    # create orange triangle 
    orange_triangle = createShape()
    orange_triangle.beginShape()
    orange_triangle.fill(color(0,0,100))
    orange_triangle.stroke(0)
    orange_triangle.stroke(color(29, 91, 84))
    orange_triangle.strokeWeight(3)
    orange_triangle.vertex(0, 10)
    orange_triangle.vertex(50, 80)
    orange_triangle.vertex(40,20)
    orange_triangle.vertex(0,10)
    orange_triangle.endShape()
    
    # create a blue square 
    blue_square = createShape()
    blue_square.beginShape()
    blue_square.fill(color(0,0,100))
    blue_square.stroke(0)
    blue_square.stroke(color(150,50,100))
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
    purple_rectangle.stroke(color(143, 71, 63))
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
    blue_circle = create_circle(300, 200, 40, color(255), color(0))
    
    # create a yellow triangle
    yellow_triangle = createShape()
    yellow_triangle.beginShape()
    yellow_triangle.fill(color(150,40,100))
    yellow_triangle.stroke(0)
    yellow_triangle.stroke(color(150,40,100))
    yellow_triangle.vertex(500, 50)
    yellow_triangle.vertex(400, 50)
    yellow_triangle.vertex(450, 75)
    yellow_triangle.vertex(500,50)
    yellow_triangle.endShape()
    
    # create a purple triangle
    purple_triangle = createShape()
    purple_triangle.beginShape()
    purple_triangle.fill(color(150,40,100))
    purple_triangle.stroke(0)
    purple_triangle.stroke(color(150,40,100))
    purple_triangle.vertex(300, 300)
    purple_triangle.vertex(400, 300)
    purple_triangle.vertex(325, 350 )
    purple_triangle.vertex(300,300)
    purple_triangle.endShape()   
    
def draw():
    shape(orange_triangle)
    shape(blue_square)
    shape(pink_square)
    shape(purple_rectangle)
    shape(green_rectangle)
    shape(yellow_circle)
    shape(yellow_triangle)
    shape(purple_triangle)
    shape(pink_circle)
    shape(blue_circle)
    
def mouseInRect(x, y, x2, y2):
    return mouseY > y and mouseY < y2 and mouseX > x and mouseX < x2
    
def mousePressed():
    # runs once each time mouse is pressed
    
    #for orange_triangle
    if mouseX < width/7.5 and mouseY < height/5:
        orange_triangle.setFill(color(29, 91, 84))

    #for blue_square
    if mouseInRect(100, 200, 200, 300):
        blue_square.setFill(color(100, 100, 50))

    #for pink_square
    if mouseInRect(500,100,600,200):
        pink_square.setFill(color(305, 24, 100))

    #for green_rectangle 
    if mouseInRect(250, 100, 300, 200):
        green_rectangle.setFill(color(143, 71, 63))
        
    
