def setup():
    size(500, 500)
    background(0)
    colorMode(HSB)


def draw():
    
    num_cols = 11
    gap = width / num_cols
    cgap = 255 / num_cols
    noStroke()
    for i in range(num_cols):    
        x = gap * i 
        c = cgap * i
        fill(c, 255, 255)
        rect(x, 0, gap, height)

 
