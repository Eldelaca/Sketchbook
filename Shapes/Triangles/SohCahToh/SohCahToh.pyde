def setup():
    size(500, 500)
    colorMode(RGB)
distance = 12.0
angle = 53
flag_height = 0

def draw():

    global distance
    global angle
    global flag_height
    
    flag_height = tan(radians(angle)) * distance
    
    
    # this is the structure of the triangle
    distance = mouseX / 15
    
    border = mouseY + 2
    stroke(175)
    line(border, height - border, (border + distance * 15), height - border)
    line(border, height - border, (border + distance * 15), height - border - flag_height * 15)
    
    line(border + (distance * 15), height - border, border + (distance * 15), height - border - flag_height * 15)
    
    
    
    # this the text to alignt to the left side of the triangle
    textAlign(LEFT, CENTER)
    x1 = 
    
    x = border + (distance * 15) + 20
    y = (height - border) - (flag_height * 15)
    fill(255)
    text("Flag height: " + str(flag_height), x, y)
