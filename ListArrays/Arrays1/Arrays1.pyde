class Planet:
    aliens_count = 0
    name = ""
    
    
    # Constructor 
    def __init__(self, aliens, name):
        self.alien_count = aliens
        self.names = name
    
    def print_alien(self):
        print(alien_count)
        print(names)
        
def setup():
    global planets, aliens
    colorMode(HSB)
    size(500,500)

    mars = Planet(10, "Mars")
    mars.planet_alien
    

#    for planet in planets:
#        print(planet)
#    for alien in aliens:
#        print(alien)

# this will print out the planets and the aliens living there beside the planet
#    for i in range(len(planets)):
 #       print(planets[i] + " " + str(aliens[i]))
#    reverse(range()) will also reverse sorted array


# this reverse the function backwards from element -1, -1, -1
#    for i in range(len(planets) -1, -1, -1):
#       print(planets[i] + " " + str(aliens[i]))


# this the planet with least number of aliens
    least_index = 0
    for i in range(len(planets)):
        if aliens[i] < aliens[least_index]:
            least_index = i
    print("The planet with the least number of aliens is : " + str(planets[least_index] + " with number of " + str(aliens[least_index])))
    print("\n")
# this the planet with most number of aliens
    most_index = 0
    for i in range(len(planets)):
        if aliens[i] > aliens[most_index]:
            most_index = i
    print("The planet with the least number of aliens is : " + str(planets[most_index] + " with number of " + str(aliens[most_index])))
    print("\n")
    
# this is the total number of planets
    total = 0
    for i in range(len(planets)):
        total = total + aliens[i]
    # this is the average of the total number of aliens
    average = total / len(planets)
    
    print("This is the total number of aliens in the universe is " + str(total))
    print("This is the average number of aliens in the universe is " + str(average))
    
    
planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
aliens = [500, 130, 350, 300, 250, 340, 200, 200, 150]

def draw():
    global planets, aliens
    
    background(0)
    w = width / len(planets)
    for i in range(len(planets)):
        x = w * i
        rect(x, height, w, - aliens[i])
        rectMode(CENTER)
        fill((i / float(len(planets))) * 255, 255, 255)
        text(planets[i], x + (w * 0.5), height - 20)
    pass
