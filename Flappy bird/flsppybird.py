import arcade


# CONTANTS
SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

SCREEN_TITLE = "Flappy Bird"

BIRD_SPEED = 5

GRAVITATION = 0.4

ANGLE_INCLINE = 0.4

LIMIT_ANGLE = 45

PIPE_SPEED = 4

DISTANCE = 150

END_LABEL_SIZE = 3

# Animate class inherited from parent
class Animate(arcade.Sprite):

    i = 0

    time = 0

    def update_animation(self, delta_time):

        self.time += delta_time

        if self.time >= 0.1:

            self.time = 0

            if self.i == len(self.textures)-1:

                self.i = 0

            else:

                self.i += 1

                self.set_texture(self.i) 

#

class Bird(Animate):

    def __init__(self):
        #inherit from Parent
        super().__init__("bird/bluebird-downflap.png", 1) 
       
        # create an angle class attribute
        self.angle = 0 

        # create a first sound class attribute for collision
        self.hit_sound = arcade.load_sound('audio/hit.wav') 

        # create a second sound class attribute for flapping wings
        self.wing_sound = arcade.load_sound('audio/wing.wav') 

        #append bird images to already made list of textures
        self.append_texture(arcade.load_texture("bird/bluebird-midflap.png"))
       
        self.append_texture(arcade.load_texture("bird/bluebird-upflap.png")) 

        # construct location(along x & y coordinates) the bird would be when game starts
        self.center_x = 50

        self.center_y = SCREEN_HEIGHT/2 

    def update(self):

        self.center_y += self.change_y 

        # create gravity effect on change y
        self.change_y -= GRAVITATION
 
        # Create a flight limit condiotion for going up
        if self.center_y > SCREEN_HEIGHT:

            self.center_y = SCREEN_HEIGHT 

        # Create a flight limit condiotion for coming down
        if self.center_y < 0:

            self.center_y = 0 
        
        # update the angle's movement
        self.angle += self.change_angle 
        self.change_angle -= ANGLE_INCLINE 
        # change to negative angle 45degree when going down
        if self.angle <= -LIMIT_ANGLE:

            self.angle = -LIMIT_ANGLE 
        
        # change to positive angle 45degree when going up
        if self.angle >= LIMIT_ANGLE:

            self.angle = LIMIT_ANGLE 

#Create Pipe class
class Pipe(arcade.Sprite):

    def __init__(self, is_up):
        super().__init__('pipe.png', 0.2, flipped_vertically=is_up) 

        # create an "is_up" attribute
        self.is_up = is_up 
    
    # update the following movement(changes) right to left
    def update(self):

        self.center_x -= self.change_x 
        if self.right < 0: 
            self.left = SCREEN_WIDTH # coordinate of right wall of window


# Game class
class Game(arcade.Window):

    def __init__(self, width, height, title):

         super().__init__(width, height, title)

         self.bg =  arcade.load_texture('bg.png') 

         #add bird object to screen
         self.bird = Bird() 

         #initialize the spritelist from arcade lib. to an object
         self.pipelist = arcade.SpriteList() 

         # add a grass teture to screen
         self.grass = arcade.load_texture('grass.png') 

         # add True boolean logic attribute to a variable
         self.game = True 

         # create a text for game over and save as an object the game class
         self.endgame = arcade.load_texture('gameover.png') 

    def setup(self):

         for i in range(6): 
             # instance class object for columns at the bottom
             pipe_bottom = Pipe(is_up = False) 
             
             #position at bottom of y & equate to 0
             pipe_bottom.center_y = 0
             
             #position at bottom of y & equate to 0
             pipe_bottom.center_x = DISTANCE * i + SCREEN_WIDTH

             # bottom change x value
             pipe_bottom.change_x =  PIPE_SPEED  

             # append the list to an empty list created
             self.pipelist.append(pipe_bottom) 

             # instance class object for columns at the top 
             pipe_top = Pipe(is_up = True) 
             
             # set the pipe centre at x
             pipe_top.center_x = DISTANCE * i + SCREEN_WIDTH

             # set the pipe centre at y
             pipe_top.center_y = SCREEN_HEIGHT 

             # set the movement at the x-axis for the top
             pipe_top.change_x = PIPE_SPEED 

             #append top pipe
             self.pipelist.append(pipe_top)





    # method for key controls of bird flight
    def on_key_press(self, key: int, modifiers: int):
        # if game is active, do the following within
        if self.game:
            # condition for flight to take place
            if key == arcade.key.SPACE: 
                self.bird.change_y = BIRD_SPEED 
                # add speed to angle change
                self.bird.change_angle = BIRD_SPEED 
                # play sound for flapping wings
                arcade.play_sound(self.bird.wing_sound, 0.2) 


# Draw on screen
    def on_draw(self):

        self.clear()

        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg) 
 
        #draw bird
        self.bird.draw()
 
        # draw pipe list on screen
        self.pipelist.draw() 

        # draw added portion of grass on screen
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.grass) 

        # If game is false(i.e is not on), draw a game over
        if not self.game:

            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / END_LABEL_SIZE, self.endgame.width*END_LABEL_SIZE, self.endgame.height*3, self.endgame) 


    def update(self, delta_time):
         # if game is on, perform the following within
         if self.game:
            #call the "update_animation" update
            self.bird.update_animation(delta_time) 

            #call the bird update
            self.bird.update()

            #call the pipelist update
            self.pipelist.update()

            # create a variable to store the collision btw list and sprite
            hit_list = arcade.check_for_collision_with_list(self.bird, self.pipelist)

            if len(hit_list) > 0: 
       
                # set game to False, if the condition above is true
                self.game = False

                # play sound, when collision happens
                arcade.play_sound(self.bird.hit_sound, 0.2)
                
                # stop bird controls
                self.bird.stop() 

                # loop through each pipe in list and stop it, if condition is true
                for pipe in self.pipelist:
                    pipe.stop()    
             


         

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

window.setup()

arcade.run() 