def setup():
    size(500, 500)
    colorMode(HSB)
coff = 0

def draw():
    global coff

    num_cols = 1 + (mouseX / 10)
    gap = width / float(num_cols)
    cgap = 255 / float(num_cols)
    noStroke()
    for i in range(num_cols):
        x = gap * i
        c = cgap * i
        fill(90, c, c)
        rect(x, 0, gap, height)

    num_circles = 5
    gap = width / float(num_circles)
    rad = gap / 2
    cgap = mouseY / 2
    start_c = mouseX / 2
    for i in range(num_circles):
        x = rad + (gap * i)
        c = (start_c + coff + (i * cgap)) % 256
        fill(150, c, 255)
        circle(x, height / 2, gap)

    num_circles = 10
    coff += 1
    gap = width / float(num_circles)
    rad = gap / 2
    cgap = mouseY / 2
    start_c = mouseX / 2
    for i in range(num_circles):
        x = rad + (gap * i)
        c = (start_c + coff + (i * cgap)) % 270
        fill(c, 255, 255)
        w = width - (i * gap)
        circle(width / 2, height / 2, w)

    num_circles = 5
    angle = TWO_PI / num_circles
    cx = width / 2
    cy = height / 2
    for i in range(num_circles):
        theta = i * angle
        x = sin(theta + c / 20) * (width / 3)
        y = cos(theta + c / 15) * (height / 3)
        ellipse(cx + x, cy + y, 30, c)
