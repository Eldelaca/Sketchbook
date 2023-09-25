def setup():
    global x
    global y
    global cx
    global cy
    global rad

    cx = width / 2
    cy = height / 2
    size(500, 500)
    # fullScreen()
    background(0)

x = 0
y = 0

cx = 0
cy = 0

rad = 50

def draw():
    background(0)
    noStroke()
    fill(x, 255, 255)
    global x 
    global y
    global rad
    fill(255)
    circle(cx + x, cy + y, rad)
    #circle(cx + x, cy - y, rad)
    #circle(cx - x, cy - y, rad)
    #circle(cx - x, cy + y, rad)
    
    
    x = x + 1
    y = y + 1
    rad -= 1
