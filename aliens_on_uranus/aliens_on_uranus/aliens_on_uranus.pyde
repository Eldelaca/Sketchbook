'''
Theme: Aliens on Uranus
Credits:
    Stars - Ciaran Farrely
    Alien Crowd - Sam O'Reilly
    DJ Booth - Daniele Uzpoleviciute
    UFOs - Albus Gallardo
    DJ - Kurtis Brady
'''


# star stuff
stars = [] # List for the stars

# UFO stuff
ships = [] # ufo will be placed into this list
lastFrame = 0

def setup():
    size(1920, 1080, P3D)
    frameRate(30)
    colorMode(HSB)
    background(0)
    
    ### star setup
    global stars


    ### crowd setup    
    global img1, img2, img3, img4, img5, img6
    # 2 hands up, 284p x 580p
    img1 = loadImage("alien_crowd/alien1.png")
    img2 = loadImage("alien_crowd/alien2.png")
    img3 = loadImage("alien_crowd/alien3.png")
    # 1 hand up, 196p x 488p
    img4 = loadImage("alien_crowd/alien4.png")
    img5 = loadImage("alien_crowd/alien5.png")
    img6 = loadImage("alien_crowd/alien6.png")
    
    global crowd_x, crowd_y1, crowd_y2, crowd_y_switch
    crowd_x = 500
    crowd_y1 = 500
    crowd_y2 = 525
    crowd_y_switch = 0
    ydir = 5 #Y Direction
    rydir = -10 #Reverse Y Direction
    
    ### dj desk setup
    global angle1, angle2, radius, speed
    angle1 = 0
    angle2 = 40  # Set a different starting angle
    radius = 100
    speed = 2
    
    global table_x, table_y, speed, direction
    table_x = 770
    table_y = 730
    speed = 2
    direction = 1  # 1 for moving right, -1 for moving left
    
    ### ufo setup
    
    global lastFrame # remember to add this global variable or the ships won't spawn in
    '''
    If you want fewer ships just lower the range below, 
    personally I think 5 is good because I made it in a way every 10 seconds disappears and new ones appear very quickly
    you can change the values down below I made comments everywhere
    '''
    for i in range(5):    
        ufo = UFO_Model("lil_ufo.obj", random(-700, 700), random(20, 50), random(20, 50), random(256))
        ships.append(ufo)
    
    ### dj animation setup
    
    # 30 frames per second, fps == 30 means cycle == 1, cycle is 1 calculated second, used for changing poses
    # wf = wireframe, triggers the noFill() version of the render, binary boolean
    global fps, cycle, wf
    fps = 0
    cycle = 0
    wf = 0
    
    global r, g, b, a
    r = random(0, 256)
    g = random(0, 256)
    b = random(0, 256)
    a = 255
    
    # assigning animation frames
    global pR, p1f1, p1f2, p1f3, p1f4, p2f1, p2f2, p2f3, p2f4
    assign_pose()
    
    ### msx logo setup
    global msx_left, msx_right
    msx_left = MSX_Model("msx.obj", width*0.25, height*0.75, 300, 35, 200)
    msx_right = MSX_Model("msx.obj", width*0.75, height*0.75, 300, 35, 200)
    
    
    
    
def draw():
    background(0)
    global fps, cycle, wf, crowd_y_switch
    global r, g, b
    global msx_left, msx_right
    
    # fps counter to manage cycles
    if fps == 5:
        fps = 0
        # increase/reset cycle
        if cycle == 25:
            cycle = 0
            # trigger wireframe after a solid cycle, and vice versa
            if wf == 0:
                wf = 1
            else:
                wf = 0
        else:
            cycle = cycle + 1
            
            # swap y values to make crowd bounce in time with dj
            if crowd_y_switch == 0:
                crowd_y_switch = 1
            else:
                crowd_y_switch = 0
            
            r = random(0, 256)
            g = random(0, 256)
            b = random(0, 256) 
    else:
        fps = fps + 1
    
    draw_stars()
    noStroke()
    fill(r/2, g*2, b/2)
    rect(0, height/1.5, width, height/1.5)
    
    spawn_crowd()
    draw_table()

    msx_left.render()
    msx_right.render_reverse()
    
    translate(width/2, height/2)
    
    ufo_spawner()
    dj_animation()
    
    
    
# # # # Stars Function+Class    
    
def draw_stars():
    global stars
  
    # Randomly generating new stars onto the screen
    if random(1) < 0.5:
        new_star = Star()
        stars.append(new_star) # "new_star" is placed onto the list
    
    # Update and display existing stars
    for star in stars:
        star.update() # This updates the stars transparency every frame
        star.display() # Displays the star object on to the screen
    
    stars = [star for star in stars if star.alpha > 0]
    '''
    the first section "star for star in stars" states the star before "for" is declaring a new variable called "star" variable in a new "stars list"
    for whenever star.alpha is greater than 0
    It puts the new variable "star" into the new stars list
    The star.alpha > 0 allows us to remove any stars that are equal to 0 which makes the fading effect
    '''
    
class Star:
    def __init__(self):
        self.x = random(width) # random X co-ordinate
        self.y = random(height) # random Y co-ordinate
        self.size = random(5, 10) # random scale of size
        self.alpha = 255 # alphas is transparency 
        self.stretch = random(1,1.5) # how long or wide the object will look

    def update(self):
        self.alpha -= 1 # This updates its transparency every frame it will go down
        
    def display(self): # This method displays the stars into the screen
        fill(255, self.alpha)
        ellipse(self.x, self.y, self.size, (self.stretch)*(self.size))
        
# # # # Crowd Spawn+Control Function
def spawn_crowd():
    global img1, img2, img3, img4, img5, img6
    global crowd_x, crowd_y1, crowd_y2, crowd_y_switch
    
    noStroke()

    if crowd_y_switch == 0:
        pushMatrix()
        for i in range (40):
            crowd_x = i * 50
            image(img5, crowd_x - 20, crowd_y1, 196/1.5, 488/1.5)
        
        for i in range(25):
            crowd_x = i * 100
            image(img6, crowd_x - 20, crowd_y2, 284/2, 580/2)
            
        for i in range(20):
            crowd_x = i * 250
            image(img2, crowd_x - 20, crowd_y1, 284/2, 580/2)
        
        for i in range(25):
            crowd_x = i * 100
            image(img1, crowd_x - 20, crowd_y2, 284/2, 580/2)
        
        for i in range (20):
            crowd_x = i * 150
            image(img4, crowd_x - 20, crowd_y1, 196/1.5, 488/1.5)
            
        for i in range (20):
            crowd_x = i * 200
            image(img3, crowd_x - 20, crowd_y2, 284/1.75, 580/1.75)
        popMatrix()
    else:
        pushMatrix()
        for i in range (40):
            crowd_x = i * 50
            image(img5, crowd_x, crowd_y2, 196/1.5, 488/1.5)
        
        for i in range(25):
            crowd_x = i * 100
            image(img6, crowd_x, crowd_y1, 284/2, 580/2)
            
        for i in range(20):
            crowd_x = i * 250
            image(img2, crowd_x, crowd_y2, 284/2, 580/2)
        
        for i in range(25):
            crowd_x = i * 100
            image(img1, crowd_x, crowd_y1, 284/2, 580/2)
        
        for i in range (20):
            crowd_x = i * 150
            image(img4, crowd_x, crowd_y2, 196/1.5, 488/1.5)
            
        for i in range (20):
            crowd_x = i * 200
            image(img3, crowd_x, crowd_y1, 284/1.75, 580/1.75)
        popMatrix()
    
    
# # # # DJ Desk Function
def draw_table():
    global angle1, angle2, radius, speed
    global table_x, table_y, speed, direction
    fill(200)
    stroke(0)
    strokeWeight(4)
    rect(460, 700, 1000, 500)
    
    
    #DISC 1
    # Calculate the positions of the moving points
    moving_point1_x =1340 + cos(radians(angle1)) * radius
    moving_point1_y = 825 + sin(radians(angle1)) * radius

    moving_point2_x = 1340 + cos(radians(angle2)) * radius
    moving_point2_y = 825 + sin(radians(angle2)) * radius

    # Draw the circle
    stroke(0)
    fill(0)
    ellipse(1340, 825, radius * 2, radius * 2)

    # Draw the first line
    stroke(200)
    strokeWeight(10)  # Set the line thickness
    line(1340, 825, moving_point1_x, moving_point1_y)

    # Draw the second line
    stroke(200)  # Different color for the second line
    line(1340, 825, moving_point2_x, moving_point2_y)
    
    
    #DISC 2
    moving_point3_x =580 + cos(radians(angle1)) * radius
    moving_point1_y = 825 + sin(radians(angle1)) * radius

    moving_point4_x = 580 + cos(radians(angle2)) * radius
    moving_point2_y = 825 + sin(radians(angle2)) * radius

    # Draw the circle
    stroke(0)
    fill(0)
    ellipse(580, 825, radius * 2, radius * 2)

    # Draw the first line
    stroke(200)
    strokeWeight(10)  # Set the line thickness
    line(580, 825, moving_point3_x, moving_point1_y)

    # Draw the second line
    stroke(200)  # Different color for the second line
    line(580, 825, moving_point4_x, moving_point2_y)    
    # Update the angles for the next frame
    angle1 += speed
    angle2 += speed
    # Draw the central circle with changing color
    noStroke()
    fill(random(255),200,200)
    ellipse(1340,825, 30, 30)
    ellipse(580, 825, 30, 30)


    # Update the position of the line
    table_x += speed * direction


    #SLIDERS
    for i in range(3):
        stroke(0)
        strokeWeight(4)
        circle(750, 740+(25*i), 20)
        rect(770, 730+(25*i), 100, 20)
        line(table_x+20, table_y+(25*i), table_x+20 , table_y+20+(25*i))  # Adjust the length of the line if needed
        
    fill(random(255),200,200)
    if table_x >= width -1070 or table_x <= 750:
        direction *= -1  # Change the direction when reaching the boundary
        
        
    #SECTION W TRIANGLES
    line(950,730,1150,730)
    line(950,730, 930,760)
    line(1150,730,1170,760)
    line(1170,800,1170,760)
    line(930,800, 930,760)
    for i in range(3):
        triangle(960+(65*i),750,1000+(65*i),750,980+(65*i),770)
    for i in range(2):
        triangle(1040+(65*i),800,990+(65*i),800,1015+(65*i),780)
        
        
    #BOXE W CIRCLES
    fill(200)
    rect(698,820,520,70)
    fill(200, random(255), random(255))
    for a in range (34):
        for i in range(4):
            fill(200, random(255), random(255))
            circle(710+(15*a), 832+(15*i),12)
            
    #TEXT 
    textSize(18)
    textAlign(CENTER, CENTER)
    for i in range(12):
        fill(200,200,random(255))
        text("URANUS", 504+(83*i), 710)
    
        
# # # # UFO Function+Class

def ufo_spawner():
    global lastFrame
        
    strokeWeight(5)
    #translate(width / 2, height / 2)

    # Randomly spawn new UFOs 
    if len(ships) < 50 and random(1) < 0.05:  # Quick reminder I looked it up and this is 0.05 = 5% chance of it spawning I think...
        newUfo = UFO_Model("lil_ufo.obj", random(-700, 700), random(20, 50), random(120, 150), random(256)) # this just puts a new ship wherever in the plain
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
    
class UFO_Model:
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
                
# # # # DJ Function+Class    
    
def dj_animation():
    global pR, p1f1, p1f2, p1f3, p1f4, p2f1, p2f2, p2f3, p2f4
    global fps, cycle, wf
    global r, g, b, a
    lights()
    #translate(width/2, height/2)

    
    # animation loop
    # simple if statements to check stage of cycle and if wireframe is on/off
    
    # frame 1
    if cycle == 0:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            pR.render()
        else:      
            fill(r, g, b, a)
            pR.render()
    # frame 2
    if cycle == 1:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f1.render()
        else:  
            fill(r, g, b, a)
            p1f1.render()
    # frame 3
    if cycle == 2:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f2.render()
        else:     
            fill(r, g, b, a)
            p1f2.render()
    # frame 4
    if cycle == 3:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f3.render()
        else:     
            fill(r, g, b, a)
            p1f3.render()
    # frame 5
    if cycle == 4:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f4.render()
        else:     
            fill(r, g, b, a)
            p1f4.render()
    # frame 6
    if cycle == 5:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f3.render()
        else:     
            fill(r, g, b, a)
            p1f3.render()
    # frame 7
    if cycle == 6:        
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f4.render()
        else:     
            fill(r, g, b, a)
            p1f4.render()
    # frame 8
    if cycle == 7:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f3.render()
        else:     
            fill(r, g, b, a)
            p1f3.render()
    # frame 9
    if cycle == 8:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f4.render()
        else:     
            fill(r, g, b, a)
            p1f4.render()
    # frame 10
    if cycle == 9:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f3.render()
        else:     
            fill(r, g, b, a)
            p1f3.render()
    # frame 11
    if cycle == 10:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f3.render()
        else:     
            fill(r, g, b, a)
            p1f3.render()
    # frame 12
    if cycle == 11:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f2.render()
        else:     
            fill(r, g, b, a)
            p1f2.render()
    # frame 13
    if cycle == 12:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p1f1.render()
        else:     
            fill(r, g, b, a)
            p1f1.render()    
    # frame 14
    if cycle == 13:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            pR.render()
        else:     
            fill(r, g, b, a)
            pR.render()
    # frame 15
    if cycle == 14:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f1.render()
        else:     
            fill(r, g, b, a)
            p2f1.render()
    # frame 16
    if cycle == 15:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f2.render()
        else:     
            fill(r, g, b, a)
            p2f2.render()
    # frame 17
    if cycle == 16:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f3.render()
        else:     
            fill(r, g, b, a)
            p2f3.render()
    # frame 18
    if cycle == 17:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f4.render()
        else:     
            fill(r, g, b, a)
            p2f4.render()
    # frame 19
    if cycle == 18:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f3.render()
        else:     
            fill(r, g, b, a)
            p2f3.render()
    # frame 20
    if cycle == 19:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f4.render()
        else:     
            fill(r, g, b, a)
            p2f4.render()        
    # frame 21
    if cycle == 20:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f3.render()
        else:     
            fill(r, g, b, a)
            p2f3.render()        
    # frame 22
    if cycle == 21:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f4.render()
        else:     
            fill(r, g, b, a)
            p2f4.render()        
    # frame 23
    if cycle == 22:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f3.render()
        else:     
            fill(r, g, b, a)
            p2f3.render()
    # frame 24
    if cycle == 23:
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f2.render()
        else:     
            fill(r, g, b, a)
            p2f2.render()
    # frame 25
    if cycle == 24:
        #cycle == 0
        if wf == 1:
            noFill()
            strokeWeight(3)
            stroke(r, g, b)
            p2f1.render()
        else:     
            fill(r, g, b, a)
            p2f1.render()

    

    
# to assign all models to their specific pose+frame variable, only ran at setup    
def assign_pose():
    
    # pR = resting pose
    # pXfY = pose X frame Y
    
    global pR, p1f1, p1f2, p1f3, p1f4, p2f1, p2f2, p2f3, p2f4

    # models with y 700 spawned slightly higher due to error in exporting    
    pR = DJ_Model("dj_anims/dj_anim_rest.obj", 0, 500, 500, 5)

    p1f1 = DJ_Model("dj_anims/p1/dj_anim_p1_f1.obj", 0, 700, 500, 5)
    
    p1f2 = DJ_Model("dj_anims/p1/dj_anim_p1_f2.obj", 0, 700, 500, 5)
    
    p1f3 = DJ_Model("dj_anims/p1/dj_anim_p1_f3.obj", 0, 700, 500, 5)
    
    p1f4 = DJ_Model("dj_anims/p1/dj_anim_p1_f4.obj", 0, 700, 500, 5)
    
    p2f1 = DJ_Model("dj_anims/p2/dj_anim_p2_f1.obj", 0, 500, 500, 5)
    
    p2f2 = DJ_Model("dj_anims/p2/dj_anim_p2_f2.obj", 0, 500, 500, 5)
    
    p2f3 = DJ_Model("dj_anims/p2/dj_anim_p2_f3.obj", 0, 500, 500, 5)
    
    p2f4 = DJ_Model("dj_anims/p2/dj_anim_p2_f4.obj", 0, 500, 500, 5)
    
class DJ_Model:
    def __init__(self, file_name, x, y, z, s):
        self.pos = PVector(x, y, z)
        self.s = s
        self.spawn = loadShape(file_name)
        self.spawn.disableStyle()
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(PI)
        rotateZ(PI)
        scale(200)        
        shape(self.spawn)
        popMatrix()
        
# # # # msx class
class MSX_Model:
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
        rotateY(self.theta)
        rotateX(-HALF_PI)
        scale(self.s)        
        
        strokeWeight(5)
        stroke(0)
        noFill()
        shape(self.sh)
        popMatrix()
        self.theta += 0.05
        
    def render_reverse(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(self.theta)
        rotateX(-HALF_PI)
        scale(self.s)        
        
        strokeWeight(5)
        stroke(0)
        noFill()
        shape(self.sh)
        popMatrix()
        self.theta -= 0.05
