models = []

def setup():
    global models
    size(1000, 1000, P3D)
    colorMode(HSB)
    
    for i in range(100):    
        msx_model = Model("msx.obj", random(-250, 250), random(-250, 250), 0, random(20, 50), random(256))
        models.append(msx_model)
               
def draw():
    global models
    # colorMode(RGB)
    # blendMode(SUBTRACT)
    # fill(255, 50)
    # rect(0, 0, width * 4, height * 4)
    # blendMode(BLEND)
    colorMode(HSB)
    background(0)
    lights()
    strokeWeight(5)
    translate(width / 2, height / 2)
    
    for msx_model in models:
        msx_model.render()

# A class consists of fields and methods
class Cube:
    
    # Constructor
    def __init__(self, x, y, z, s, h):
        # These are now fields!! Thats what the self word does
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.theta = 0
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(self.theta)
        rotateX(self.theta)
        scale(self.s)
        
        stroke((self.h + mouseX) % 256, 255, 255)
        noFill()
        box(100)
        popMatrix()
        self.theta += 0.5
        
class Model:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        self.theta = 0
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(self.theta * 5)
        rotateZ(self.theta * 2)
        rotateX(-HALF_PI)
        
        scale(mouseY / 2)        
        stroke((self.h + mouseX) % 256, 255, 255)
        noFill()
        shape(self.sh)
        popMatrix()
        self.theta += 0.01
    
