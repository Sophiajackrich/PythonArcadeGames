import arcade
import random

# Set constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dinosaur"
GRAVITATION = 0.5
DINO_HEIGHT = 12
CACTUS_SPEED = 5 

# create an Animate class to inherit from Parent
class Animate(arcade.Sprite):
    # create counter field
    i = 0 

    # create a time field
    time = 0

    # create an animation update method
    def update_animation(self, delta_time):   
        # increases the "self.time" by each "delta_time"
        self.time += delta_time
        
        # sets a condition for when "Self.time >= 1"
        if self.time >= 0.1:
            #if condition is true, then let it set back to zero
            self.time = 0
            
            # if condition is true, #check if "self.i" is equal to last index on the texture list
            if self.i == len(self.textures)-1:
                self.i = 0 # if it is equal to last index on list, set i back to 0

            else:
                # otherwise, increase the i(animation) by 1
                self.i += 1 
        
            # set the texture to the right animation
            self.set_texture(self.i) 

# dinusor class
class Dino(Animate):
    #create a boolean False variable
    jump = False
    def update(self):
         self.center_y += self.change_y

         #reduction of change in y
         self.change_y -= 0.5 

         #set a fall limit for dino center in y coordinate
         if self.center_y < 200:
            self.center_y = 200 
            self.jump = False 

    
#create cactus class
class Cactus(Animate):

    def update(self):
        self.center_x -= self.change_x

        # condition to control cactus right side of x coordinate
        if self.right < 0:
            self.left = SCREEN_WIDTH + random.randint(0, SCREEN_WIDTH) 
            print(self.left)
        

#Game class
class Game(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        #instantiate/load a texture to an object
        self.bg = arcade.load_texture('materials/images/bg.png') 
        
        # instantiate a dinusor object
        self.dino = Dino("materials/images/dino1.png",0.5) 
        
        # instantiate a cactur=s object
        self.cactus = Cactus("materials/images/cactus1.png",0.5) 

        # create a logical truth object
        self.game = True

        # create instance for game over texture
        self.game_over = arcade.load_texture('materials/images/game_over.png') 

    def setup(self):
        # place the Dino on the screen
        self.dino.center_x = 200

        self.dino.center_y = 200 

        # place the cactus on the screen
        self.cactus.center_x = SCREEN_WIDTH

        self.cactus.center_y = 200
       
        # append texture to list of textures from arcade lib that can be applied to the sprite
        self.dino.append_texture(arcade.load_texture("materials/images/dino2.png"))

        # append 3rd texture of dino
        self.dino.append_texture(arcade.load_texture("materials/images/dino3.png"))
        
        # append 3rd texture of cactus
        self.cactus.append_texture(arcade.load_texture("materials/images/cactus2.png"))

        # cactus movement to the right
        self.cactus.change_x = CACTUS_SPEED 


    # method for key controls
    def on_key_press (self, key, modifiers):
        if self.game: 
            # set a condition for if space key is pressed
            if (key == arcade.key.SPACE) and (not self.dino.jump): 
                # dino should change in y direction
                self.dino.change_y = DINO_HEIGHT
                # check true value of dino jump
                self.dino.jump = True 

    def on_draw(self):

        self.clear()

        #set a condition for game to be true
        if self.game:
                arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg) 
        # create a condition for gameover
        else:
           arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.game_over) 

        # call draw method for dinusor
        self.dino.draw() 
 
        # call draw method for dinusor
        self.cactus.draw()

    def update(self, delta_time):
        # check if game is on
        if self.game:
             
             #call the dino update method
             self.dino.update()

             #call the dino update method
             self.cactus.update()

             #call the dino update_animation method
             self.dino.update_animation(delta_time) 
             print(delta_time)
            
             #call the cactus update_animation method
             self.cactus.update_animation(delta_time)

        # check for collision and stop all game
        if arcade.check_for_collision(self.dino, self.cactus):
            self.game = False 


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()

arcade.run() 
