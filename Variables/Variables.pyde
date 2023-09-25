def setup():
    # size() = pixels visible
    size(500, 500)
    # colorMode(RGB)
    colorMode(HSB)
        
        
def draw():
    # Greyscale
    # RBG
    # RBGA
    background(0)

    f = 10.0
    g = 20.0
    h = 5
    
    # addition
    f = f + 1
    f += 1
    
    # subtraction
    g -= 30
    g = g - 27
    
    # Multiply
    g = f * h
    h *= 2
    
    #Division
    g = f / h
    h = h / 2.5
    
    f = pow(g, 2)
    
    h = h - 7
    g += f
    f += g
    h = f - (g + 5)
     
    println("f: " + str(f))
    println("g: " + str(g))
    println("h: " + str(h))

    
    
    f = 10.0
    print(f/2)
    println(f)
    
    stroke(80, 255, 255)
    line(mouseX, 10, 100, mouseY)
    # rect(x, y, w, h)
    # rectMode(CORNER, CORNERS, CENTER, or RADIUS)
    rectMode(CORNERS)
    rect(20, 20, 50, 100)
    noStroke()

    # circle (x, y, r)
    circle(100, mouseY, 5)
    fill(90, mouseX / 2, 255)
    ellipse(200, 200, 100, 10)
    point(90, 100)
