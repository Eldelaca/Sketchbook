def setup():
    size(500, 500)
    colorMode(RGB)
    background(0)
    global x
    global y
    
    global a
    global b

    global c
    global d
    
    global e
    global f
    
    x = width / 2
    y = height / 2
    
    a = width / 2
    b = height / 2
    
    c = width / 2
    d = height / 2

    e = width / 2
    f = height / 2

def draw():
    background(0)
    global x
    global y
    noStroke()
    fill(255)
    circle(x, y, 50)
    x = x + 1
    y = y + 1
    
    global a
    global b
    circle(a, b, 50)
    a = a + 1
    b = b - 1
    
    global c
    global d
    circle(c, d, 50)
    c = c - 1
    d = d - 1
    
    global e
    global f
    circle(e, f, 50)
    e = e - 1
    f = f + 1
    
