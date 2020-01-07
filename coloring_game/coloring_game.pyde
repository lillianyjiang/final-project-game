hue = 0

def setup():
    global path
    size(600,400)
    colorMode(HSB, 3600, 100, 100)
    background(0, 0, 100)
    # create shape 
    path = createShape()

    path = createShape()
    path.beginShape()
    path.fill(color(240,100,100))
    path.stroke(0)
    path.stroke(color(240,100,100))
    path.strokeWeight(3)
    path.vertex(0, 10)
    path.vertex(50, 80)
    path.vertex(40,20)
    path.vertex(0,10)
    path.endShape()

def draw():
    shape(path)
    print(mouseX)
    
    if mouseX > width/2:
        path.setFill(color(240,100,100))
    else:
        path.setFill(color(0,0,100))
    
    
    
    
    
