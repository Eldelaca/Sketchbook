def setup():
    global x
    global y
    size(1000, 1000)
    colorMode(HSB)
    x = width / 2
    y = height / 2
    background(0)

x = 0
y = 0
c = 0

xpos = 20
ypos = 20

w = 50
rad = w / 2

def draw():
    global x
    global y
    global rad
    global xpos
    global ypos
    global c
    
    
    colorMode(HSB)
    blendMode(SUBTRACT)
    rect(0, 0, width * 4, height * 4)
    blendMode(BLEND)
    colorMode(HSB)
    
    noStroke()
    fill(c, 255, 255)
    circle(x,y,200)
    
    x = x + xpos
    y = y + ypos
    c = c + 1
    
    if c > 255:
        c = 0
        
    if (x > width-rad or xpos < rad):
        xpos *= -1
        
    if (ypos > height - rad or 
    
         
         
         
