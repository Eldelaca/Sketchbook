def setup():
    global cx, cy
    global px, py
    size(500, 500)
    # fullScreen()
    colorMode(RGB)
    cx = width / 2
    cy = height /2
    px = cx
    py = cy
    
cx = 0
cy = 0
r = 150
angle2 = 0

px = 0
py = 0
    
def draw():    
    global cx, cy
    global px, py
    num = 10
    theta = TWO_PI / num
    
    background(0)
    stroke(255)
    strokeWeight(5)
    translate(cx, cy)

    for i in range(num):
        angle = theta * i
        pushMatrix()
        rotate(angle)
        noStroke()
        fill(255,255,255)
        ellipse(0, 10, 300, 100)        
        popMatrix()
        
    ellipse(0,100,20,300)
    
    fill(0, 50, 0)
    circle(0,10,40)
    
    fill(0, 255, 0)
    circle(0,10,30)
        
        
    
