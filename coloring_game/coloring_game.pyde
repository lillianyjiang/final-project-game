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
    global yellow_circle
    global pink_circle
    global blue_circle
    global yellow_triangle
    
    size(600,400)
    colorMode(HSB, 3600, 100, 100)
    background(0, 0, 100)
    
    # create orange triangle 
    orange_triangle = createShape()
    orange_triangle.beginShape()
    orange_triangle.fill(color(240,100,100))
    orange_triangle.stroke(0)
    orange_triangle.stroke(color(240,100,100))
    orange_triangle.strokeWeight(3)
    orange_triangle.vertex(0, 10)
    orange_triangle.vertex(50, 80)
    orange_triangle.vertex(40,20)
    orange_triangle.vertex(0,10)
    orange_triangle.endShape()
    
    # create a blue square 
    blue_square = createShape()
    blue_square.beginShape()
    blue_square.fill(color(150,50,100))
    blue_square.stroke(0)
    blue_square.stroke(color(150,50,100))
    blue_square.vertex(100,200)
    blue_square.vertex(200,200)
    blue_square.vertex(200,300)
    blue_square.vertex(100,300)
    blue_square.vertex(100,200)
    blue_square.endShape()
    
    # create a purple star
    # HSB color code for purple is 280,100,100
    
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
    
def draw():
    print(mouseX)

    shape(orange_triangle)
    
    if mouseX > width/2:
        orange_triangle.setFill(color(240,100,100))
    else:
        orange_triangle.setFill(color(0,0,100))
    
    shape(blue_square)
    
    shape(yellow_circle)
    
    shape(yellow_triangle)
    
    shape(pink_circle)
    
    shape(blue_circle)
    
