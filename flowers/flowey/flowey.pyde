def setup():
    size(500,500)
    colorMode(HSB)
    global cx , cy
    global r
    cx = width / 2
    cy = height / 2

cx = 0
cy = 0
r = 200
    
def draw():
    global cx, cy
    global r
    
#    current = 1
#    start = 1
#    for i in range(100):
#        newcurrent = current + start
#       newcurrent = current + newcurrent
#        print(newcurrent)
        
    num = 12
    theta = TWO_PI / 12
        
    background(0)
    noStroke()
    
    for i in range(num):
        angle = theta * i
        c = (i / float(num)) * 255
        print(c)
        fill(c, 255, 255)
        
        x = cx + sin(angle) * r
        y = cy + cos(angle) * r
        stroke(200, 255, 255)
        line(cx, cy, x ,y)
        circle(x,y, 30)
