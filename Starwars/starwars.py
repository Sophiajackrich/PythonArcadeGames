#import libs
import arcade

import random


# CONSTANTS
SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

SCREEN_TITLE = "Star Wars" 

LASER_SPEED = 5

ENEMY_SPEED = 1

ENEMY_DISTANCE = 50


# Add milennium falcon sprite to game and pass in parent sprite
class MillenniumFalcon(arcade.Sprite):
    # call the instance of the "MilenniumFalcon", allows you to directly pass information to the class
    def __init__(self): 
        super().__init__('falcon.png', 0.3) # inherit from parents class constructor
        #call the attribute of the screen width and save to an object of the "Game" class
        self.center_x = SCREEN_WIDTH/2  # ship would be middle of the screen on x-coordinate
        
        self.center_y = 100 #ship would be at bottom close to 0, on y-axis


    # Add changes to the "MillenniumFalcon" class
    def update(self):
        
        self.center_x+=self.change_x

        
        

# create a "Lazer" class that would be a regular sprite
class Lazer (arcade.Sprite):

    def __init__(self): 
        super().__init__('laser.png', 0.8)

        # call the game class attribute and assign it as an object of the "Lazer" class
        self.center_x = window.falcon.center_x 

        # call the game class attribute and assign it as an object in this class
        self.bottom = window.falcon.top 

        # assign a value to the upward movement attribute of this class
        self.change_y = LASER_SPEED  

        # load sound from arcade library to an object of this class
        self.laser_sound = arcade.load_sound('laser.wav') 

    # create an update method
    def update(self):
        
        # increase laser position along y axis to change position of lazer
        self.center_y+=self.change_y 

        # Check if attribute of class center is greater than "Screen height"
        if self.center_y > SCREEN_HEIGHT:
            #if condition is true, Removes recorded values in the Ram
            self.kill() 


#Create enemy class
class TieFighter(arcade.Sprite):
    def __init__(self): 
        #call parent constructor
        super().__init__('TieFighter.png', 0.2) 
        # set angle rotation attribute facing downwards
        self.angle = 90
        #set change top/bottom speed attribute
        self.change_y = ENEMY_SPEED 

    # create an update method
    def update(self):

        self.center_y -= self.change_y
        
        # delete, if movement is beyond screen boarder
        if self.center_y < 0:

            self.kill() 


# Add Mteorite Sprite
class Meteor(arcade.Sprite):

    def __init__(self): 
        super().__init__('meteorit.png', 0.5) 

        # sprite position at x coordinate should start from left to right randomly
        self.center_x = random.randint(0, SCREEN_WIDTH) 

        #sprite position at y coordinate should start at screen height and then randomly move by 3times the screen height(downwards)
        self.center_y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT*3) 
        
        # increase movement to be faster than both existing sprites speed in game
        self.change_y = ENEMY_SPEED + LASER_SPEED 

     #create update for sprite class
    def update(self):
        
        # decrease sprite movement to change its position downwards
        self.center_y-=self.change_y 

        # check that the top of the sprite goes beyond the bottom border of the screen
        if self.top < 0:
            
            #randomly take sprite back to top and then to bottom again
            self.center_y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT * 3) 


# Game class
class Game(arcade.Window):

    # create game instance with parameters
    def __init__(self, width, height, title): 
        # inherit the Parent parametrs into Game class
        super().__init__(width, height, title)  

        # load screen background to an object
        self.bg = arcade.load_texture('background.jpg') 

        # call the Flacon class in the game class and save to an object
        self.falcon = MillenniumFalcon() 

        # set visbility of mouse on window at start of game to "True/False"
        self.set_mouse_visible(False) 

        # call the "spritelist" attribute from arcade and assign it as an oject of this class
        self.lasers = arcade.SpriteList() 

        #create an empty list from arcade lib to store all the "enemies".
        self.enemies = arcade.SpriteList() 
        
        # call the method that would place sprites in the right places
        self.setup()

        # create victory and save to an object of this class
        self.game = True 

        # load win texture into game
        self.win = arcade.load_texture('win.png')

        #Create an instance of Meteor class and assign to an object of this class
        self.meteor = Meteor()  


    
    # create setup method
    def setup(self):
        #loop through 50 enemies
        for i in range(50):
            # create an object for "TieFighter" class .
            tie_fighter = TieFighter() 

            #location of enemies in game along x co-ordinates
            tie_fighter.center_x = random.randint(0, SCREEN_WIDTH) 
            
            #location of enemies along y co-ordinate in game
            tie_fighter.center_y = SCREEN_HEIGHT + (i * ENEMY_DISTANCE)

            #append object to list
            self.enemies.append(tie_fighter) 


    #create a method for mouse control for ship shooting the lazers on the window 
    def on_mouse_press(self, x, y, button, modifiers): 
       
        # create condition for mouse press to work, (i.e if game is on)
        if self.game:
            #Condition for pressing "Left mouse button"
            if button == arcade.MOUSE_BUTTON_LEFT: 

                #call the Lazer class to an object
                laser = Lazer() 

                #play sound attribute from arcade lib
                arcade.play_sound(sound=laser.laser_sound, volume=0.5)

                #append the lazers to list
                self.lasers.append(laser) 

            


    # create the "on_mouse_motion" to control movement of ship
    def on_mouse_motion(self, x, y, dx, dy):

        # create condition for mouse movement to work, (i.e if game is on)
        if self.game:
            # assign parameters to Sprite class (Falcon) attribute "center_x"
            self.falcon.center_x = x 

    def on_draw(self):
        # Student with old mac and using arcade version, use the following
        # def on_draw(self):

        #     self.background_color = (255,255,255)

        #     self.clear()

        # Set background to be very bright
        self.clear((255,255,255)) 

        # draw background on screen
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg) 
        
        # draw it to appear on screen
        self.falcon.draw() 
  
        # draw lazers on screen
        self.lasers.draw() 
 
        # draw enemies sprite on screen
        self.enemies.draw()

        # draw meteor sprite on screen
        self.meteor.draw() 

        if len(self.enemies) == 0:

            self.game = False

            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.win) 
        

    # Set Game class update
    def update(self, delta_time):

        # create condition for mouse control to work, (i.e if game is on)
        if self.game:

            # update falcon sprite class
            self.falcon.update()

            # update lazer sprite class
            self.lasers.update()

            #create a condition and check for collision 
            for laser in self.lasers:

                hit_list = arcade.check_for_collision_with_list(laser, self.enemies) 

                # create a condition to check "hit_list" to be true 
                if hit_list:
                    #if condition is true, remove target(lazer)
                    laser.kill() 

                    for enemy in hit_list:

                        enemy.kill() 

            #update enemies
            self.enemies.update() 

            #update meteor in game class
            self.meteor.update() 

            #Add a condition to stop game if the following sprites in condition collides
            if arcade.check_for_collision(self.meteor, self.falcon):

                self.game = False 


         


# assign the instance of the game class to a variable
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# call the "run" command to keep the window loop running
arcade.run() 