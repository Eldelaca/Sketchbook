def setup():
    global cx
    global cy
    global r
    global c
    global theta
    global px
    global py
    
    fullScreen()
    # size(1000, 1000)
    cx = width / 2
    cy = height /2
    
    px = cx
    py = cy
    
    colorMode(HSB)
    
    background(0)
    
cx = 0
cy = 0
r = 1
theta = 0

px = 0
py = 0
c = 0
x = 0
y = 0

def draw():
    
    global cx
    global cy
    global px
    global py
    global r
    global c
    global x
    global y
    global theta
    
    #rect(x, y, x, y)
    #x = cx + sin(theta) * r
    y = cy + cos(theta) * r
    
    stroke(c, c, 250, c)
    strokeWeight(50)
    line(px, py, x, y)
    #circle(x, y, 50)
    
    r = r + 1
    c = (c + 15) % 255
    theta = theta + 100
    
    px = x
    py = y
    x = y + 1
    
    
    
