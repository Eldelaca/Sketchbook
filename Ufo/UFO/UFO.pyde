ships = [] # ufo will be placed into this list
lastFrame = 0

def setup():
    global lastFrame # remember to add this global variable or the ships won't spawn in
    size(1980, 1080, P3D)
    colorMode(HSB)
    frameRate(30)  # change this value to whatever you want but it does change 1 variable I think when spawning new ships you 
    '''
    If you want fewer ships just lower the range below, 
    personally I think 5 is good because I made it in a way every 10 seconds disappears and new ones appear very quickly
    you can change the values down below I made comments everywhere
    '''
    for i in range(5):    
        ufo = Model("lil_ufo.obj", random(-700, 700), random(20, 50), random(20, 50), random(256))
        ships.append(ufo)

def draw():
    global lastFrame
    colorMode(HSB)
    background(0)
    lights()
    strokeWeight(5)
    translate(width / 2, height / 2)

    # Randomly spawn new UFOs 
    if len(ships) < 50 and random(1) < 0.05:  # Quick reminder I looked it up and this is 0.05 = 5% chance of it spawning I think...
        newUfo = Model("lil_ufo.obj", random(-700, 700), random(20, 50), random(20, 50), random(256)) # this just puts a new ship wherever in the plain
        ships.append(newUfo) # Creates new ufo

    # Make the ufo appear
    for ufo in ships:
        ufo.render()

    # this lets me set up the frameCount and check within every 10 seconds a new ufo will appear
    if frameCount - lastFrame >= 300:  # 30 frames per second * 10 seconds
        '''
        Removes the first UFO (oldest one) from the list 
        Remove the oldest Ufo from the "ships list" on line 1
        The thing below just checks if said ship = 0 then pop(0) removes the oldest ship on the list from line 1    
        '''
        if len(ships) > 0:
            ships.pop(0)
        lastFrame = frameCount

class Model:
    def __init__(self, file_name, x, y, z, h):
        self.pos = PVector(x, y, z)
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        self.theta = 0
        self.scale_factor = random(0.5, 2) 
        '''
        had to add this wouldn't scale properly, if you just leave it random in scale() 
        it stars giving you an epilepsy i don't know why
        '''

    def render(self):
        pushMatrix()
        # rotation
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(self.theta) # just using theta to adjust the speed you can change the parameters if you want instead of theta
        rotateZ(PI)

        # Random scaling as well as color
        scale(750 * self.scale_factor) # This is how you change the scaling refering back to line 72
        noStroke()
        fill((self.h + mouseX + frameCount) % 255, 255, 255) # You can change this if you want from frameCount to mouseX if you wish on the background
        shape(self.sh) # calls in the obj file from the constructor
        popMatrix()
        self.theta += 0.005 # this is the changes the value of its speed
