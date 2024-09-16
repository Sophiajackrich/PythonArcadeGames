import arcade  # we connect the necessary libraries
import random
import time

SCREEN_WIDTH = 800  # create a variable to store the screen width
SCREEN_HEIGHT = 600  # create a variable to store the screen height

class Animate(arcade.Sprite):
    '''
        This is our animation class, you know it well.
    '''
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

class Chicken(Animate):  # we create a class that will be responsible for the work of the chickens
    def __init__(self):  # create an initialization method to create parameters for the chicken
        super().__init__(f"chicken/chicken_0.png",0.9)  # load the initial texture for the chickens, set its size to 90%
        self.frames = 4 # number of chicken textures 4
        for i in range(self.frames): # let's run through the textures
            self.append_texture(arcade.load_texture(f"chicken/chicken_{0}.png")) # and add textures to the sprite for subsequent animation

class Wolf:  # we create a class that will be responsible for the wolf's work
    def __init__(self):  # create an initialization method to create parameters for the wolf
        super().__init__("wolf_left_bottom.png", 0.9)  # load the initial texture for the wolf, set its size to 90%
        self.left_dir = True  # logical variable: wolf looks left
        self.right_dir = False  # logical variable: wolf looks to the right
        self.top_dir = False # logical variable: wolf up
        self.bottom_dir = True# logical variable: wolf below
        # below we download textures for all four possible positions of the wolf
        self.left_top = arcade.load_texture("wolf_right_top.png")
        self.left_bottom = arcade.load_texture("wolf_right_bottom.png")
        self.right_top = arcade.load_texture("wolf_left_top.png")
        self.right_bottom = arcade.load_texture("wolf_left_bottom.png")

    def update(self):  # we create a method responsible for the wolf's game behavior
        # below we check which corner the wolf is looking at: top right, bottom right, top left or bottom left
        # after checking we change the wolf's texture to the one that matches its direction
        if self.left_dir and self.bottom_dir:
            self.texture = self.left_bottom
        elif self.left_dir and self.top_dir:
            self.texture = self.left_top
        elif self.right_dir and self.bottom_dir:
            self.texture = self.right_bottom
        elif self.right_dir and self.top_dir:
            self.texture = self.right_top


class Egg(arcade.Sprite):  # we create a class that is responsible for creating eggs
    def __init__(self):  # create an initialization method to create parameters for all eggs
        super().__init__("egg.png", 0.1)  # load the initial texture for the egg, set its size to 110%
        self.pos = 0  # variable that will be responsible for choosing the position of the egg before it hatches
        # (on which of the four shelves will it appear)
        self.change_angle = 4  # set the rate of change of angle
        self.change_x = 0.5  # set the rate of change of horizontal position
        self.change_y = 0.2  # set the speed of change of vertical position
        self.missed = False  # a sensor variable to track whether an egg was missed

    def setup(self):  # create a method to set initial values
        self.pos = random.randint(3,4)  # randomly select one of four positions
        # (1 - left lower, 2 - left upper, 3 - right upper, 4 - right lower)
        if self.pos == 1: 
            self.center_x = 25   # initial coordinates for the first position
            self.center_y = 290  # initial coordinates for the first position
        elif self.pos == 2:
            self.center_x = 25   # initial coordinates for the second position
            self.center_y = 470  # initial coordinates for the second position
        elif self.pos == 3:
            self.center_x = 775  # initial coordinates for the third position
            self.center_y = 470  # initial coordinates for the third position
        elif self.pos == 4:
            self.center_x = 775  # initial coordinates for the fourth position
            self.center_y = 290  # initial coordinates for the fourth position

    def update(self):  # create a method to set the game behavior of eggs
        if self.pos == 1 or self.pos == 2:  # if the egg appears on the left, then rotate it and gradually move it to the right
            self.angle -= self.change_angle  # rotate right
            self.center_x += self.change_x  # shift to the right
            if self.center_x > 210:  # force vertical thrust after point x = 210 to create the effect of falling
                self.change_y += 0.5
        elif self.pos == 3 or self.pos == 4:  # if the egg appears on the right, then rotate it and gradually move it to the left
            self.angle += self.change_angle  # rotate left
            self.center_x -= self.change_x  # shift to the left
            if self.center_x < 590:  # force vertical thrust after point x = 590 to create the effect of falling
                self.change_y += 0.5
        self.center_y += self.change_y  # we give a general uniform fall downwards so that the eggs roll down under a small
        # angle

        self.change_x += 0.02  # we give a general uniform horizontal thrust so that the eggs roll down with acceleration
        self.change_y += 0.015  # we give a general uniform vertical thrust so that the eggs fall with acceleration

        if arcade.check_for_collision(self, window.wolf):  # check for a collision between the wolf and the eggs
            if self.pos == 1:  # if an egg falls from the bottom left shelf
                if window.wolf.left_dir and window.wolf.bottom_dir:  # and if the wolf holds the basket on the bottom left
                    window.score += 1  # then we count the egg as caught
                    self.kill()  # we remove the model of this egg from the screen
                elif not self.missed:  # otherwise, if the egg has not yet been considered missed
                    window.missed += 1  # add one to the counter of missed eggs
                    # remember that this egg was already counted as fallen
            elif self.pos == 2:  # if an egg falls from the top left shelf
                if window.wolf.left_dir and window.wolf.top_dir:  # and if the wolf holds the basket on the top left
                    window.score += 1  # then we count the egg as caught
                    self.kill()  # we remove the model of this egg from the screen
                elif not self.missed:  # otherwise, if the egg has not yet been considered missed
                    window.missed += 1  # add one to the counter of missed eggs
                    # remember that this egg was already counted as fallen
            elif self.pos == 3:  # if an egg falls from the right top shelf
                if window.wolf.right_dir and window.wolf.top_dir:  # and if the wolf holds the basket on the top right
                    window.score += 1  # then we count the egg as caught
                    self.kill()  # then we count the egg as caught
                elif not self.missed:  # otherwise, if the egg has not yet been considered missed
                    window.missed += 1  # add one to the counter of missed eggs
                    # remember that this egg was already counted as fallen
            elif self.pos == 4:  # if an egg falls from the right bottom shelf
                if window.wolf.right_dir and window.wolf.bottom_dir:  # and if the wolf holds the basket on the bottom right
                    window.score += 1  # then we count the egg as caught
                    self.kill()  # we remove the model of this egg from the screen
                elif not self.missed:  # otherwise, if the egg has not yet been considered missed
                    window.missed += 1  # add one to the counter of missed eggs
                    # remember that this egg was already counted as fallen

class Health(arcade.Sprite):    # Creating a life class
    def __init__(self):     # creating a class initialization method (constructor)
        super().__init__("3_heart.png", 0.7) # load the initial texture for life, set its size to 70%
        self.append_texture(arcade.load_texture("2_heart.png"))  # additionally load a texture with a picture of 2 hearts
        self.append_texture(arcade.load_texture("1_heart.png"))  # additionally load a texture with a picture of 1 hearts
        self.center_x = SCREEN_WIDTH/2 + 300  # similarly, the initial coordinates for the health bar, here x
        self.top = SCREEN_HEIGHT - 5  # position the top edge of the sprite with an indent of 5 pixels from the top border of the window
    
    def update(self):
        if window.missed == 1:  # if 1 egg is missed
            self.set_texture(1)  # then we change the texture of the health bar to 2 hearts
        elif window.missed == 2:  # if 2 missed
            self.set_texture(2)  # then we change it to 1 heart
        elif window.missed >= 3:  # if there are 3 or more missed (you never know)
            self.kill()  # remove the health bar
            window.run = False  # "turn off the game"


class MyWindow(arcade.Window):  # create a class for the game window
    def __init__(self):  # create an initialization method to create in-game parameters
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Волк и яйца")  # we create a window directly with the size 800x600 and with the title "Wolf and eggs"
        self.bg = arcade.load_texture("bg.png")  # Load texture for background
        self.go = arcade.load_texture("go.jpg")  # Load texture for background
        self.lines = arcade.load_texture("lines.png")  # loading shelf texture
        self.wolf = Wolf()  # создаем волка
        self.eggs = arcade.SpriteList()  # create a sprite list to store all egg objects
        self.timer = time.time()  # remember the game launch time
        self.score = 0  # create a counter variable for the points scored
        self.missed = 0  # create a counter variable for missed eggs
        self.health_bar = Health()  # create a sprite with a texture in the form of three hearts (number of lives)
        self.run = True  # logical variable, if true, then the game is considered to be running
        self.chickens = arcade.SpriteList() # list for storing chicken sprites
        self.setup()  # we call the setup method so that the characters have initial values ​​for coordinates and speeds
        self.sound = arcade.load_sound("sound.mp3") # loading background music



    def setup(self):  # create a method to set initial values
        self.wolf.center_x = SCREEN_WIDTH/2  # initial coordinates of the wolf, in this line x
        self.wolf.center_y = SCREEN_HEIGHT/2 - 150  # and in this line he has
        self.coords = [(25,290), (25,290),(25,290), (25, 290)] # hens coordinates
        for pos in self.coords: # iterate over the list of coordinates
            chicken = Chicken()   # create an instance of the class
            x, y = pos  # we parse the coordinates into variables x and y
            chicken.center_x = x # we place the chicken horizontally
            chicken.center_y = y # we place the chicken vertically
            self.chickens.append(chicken) # add chicken to sprite sheet

    def on_draw(self):  # create a rendering method
        self.clear()
        if self.run:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)  # draw the background texture to the entire screen
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT/2, self.lines)  # we draw the texture of the shelves only on half the screen
            self.wolf.draw()  # draw a wolf
            self.eggs.draw()  # draw eggs
            self.health_bar.draw()  # draw hearts to indicate remaining health
            self.chickens.draw() # we draw chickens 
        else:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.go)
        

    def update(self, delta_time: float):  # create a method for setting game behavior and game logic
        if self.run:  # check if the game is running
            self.wolf.update()  # call wolf update
            self.eggs.update()  # call update on eggs
            if time.time() - self.timer > 1:  # we measure 1 second from the moment recorded in self.timer
                egg = Egg()  # create an egg
                egg.setup()  # we place the egg on the shelf
                self.eggs.append(egg)  # add egg to the list of eggs
                self.timer = time.time()  # updating the timer
                self.health_bar.update()
        self.chickens.update_animation(delta_time) # we start the animation for the chickens
    def on_key_press(self, symbol: int, modifiers: int):  # create a method to track keyboard presses
        if symbol == arcade.key.RIGHT:  # if the right arrow is pressed
            self.wolf.right_dir = True  # wolf we start looking to the right
            self.wolf.left_dir = False  # and to the left it stops
        elif symbol == arcade.key.LEFT:  # if the left arrow is pressed
            self.wolf.left_dir = True  # then the wolf looks to the left
            self.wolf.right_dir = False  # and to the right it stops
        elif symbol == arcade.key.UP:  # if the up arrow is pressed
            self.wolf.top_dir = True  # then the wolf looks up
            self.wolf.bottom_dir = False  # and it stops going down
        elif symbol == arcade.key.DOWN:  # if the down arrow is pressed
            self.wolf.bottom_dir = True  # then the wolf looks down
            self.wolf.top_dir = False  # and it stops going up


window = MyWindow()  # create a game window
arcade.run()  # keep the game window open 
