def setup():
    size(500, 500)
    colorMode(HSB)
# For loops:
    for i in range(10):
        print(i)
    
    for i in range(20, 30):
        print(i)
    
    for i in range(20, 30, 2):
        print(i)
        
    for i in range(20, 0):
        print(i)
        
# Calculating this directly
    for y in range(100, 180, 20):
        line(100, y, 400, y)
# This is calculating, 4 times
    for y in range(4):
        y = 300 + (i * 20)
        line(100, y, 400, y)

# While loops:
    i = 0
    while i < 4:
        y = map(i, 0, 3, 450, 480)
        line(100, y, 400, y)
        i = i + 1
        
    line(100, 100, 400, 100)
    line(100, 120, 400, 120)
    line(100, 140, 400, 140)
    line(100, 160, 400, 160)


def draw():
    background()
    noStroke()
    
