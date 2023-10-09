def setup():
    global y
    size(500, 500)
    y = height / 2
    colorMode(HSB)
    
# variables
w = 50 # width of circle
hw = w / 2 # half-width of circle
x = hw
y = 0
xdir = 1

def draw():
    global x
    global xdir
    background(0)
    noStroke()
    # this changes slowly changes the color of the circle
    fill(x / 2, 255, 255)
    circle(x, y, w)
    x = x + xdir
    
    println("x; " + str(x))
    println("x; " + str(xdir))
    
    if x == width + hw:
        xdir = -1
