# import arcade lib
import arcade

# import random lib
import random

# screen width
SCREEN_WIDTH = 960

#screen height
SCREEN_HEIGHT = 720

# screen title
SCREEN_TITLE = "Race"

# car angle rotation
CAR_ANGLE = 20

# car speed
CAR_SPEED = 5

# wall speed
WALL_SPEED = 5

#Estimate of center_y bottom
CENTRE_Y_BOTTOM = 100

# create a car claa, for the game
class Car(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x
        

# create a war obstacle sprite class
class Wall(arcade.Sprite):
    def update(self):
        self.center_y-=self.change_y
        #condition if wall top becomes less than 0
        if self.top < 0:
            # let self bottom always go back to screen's height 
            # The random is to appear randomly within specified range
            self.bottom = SCREEN_HEIGHT + random.randint(0, SCREEN_HEIGHT) 
            
            # update login on sprite wall
            self.center_x = random.randint(168, SCREEN_WIDTH-168)
        

# creating class, alongside with Parent class
class MyGame(arcade.Window):
    def __init__ (self, width, height,title):
        # link to calling constructor of parent class
        super().__init__(width, height, title)

        # load the in-built arcade texture(picture) program
        self.bg = arcade.load_texture('bg.png')

        # create an instance of the Car class
        self.car = Car("blue_car.png", 0.8)

        # create an instance of the Car class
        self.wall = Wall("wall.png", 0.8)
        
        # create a logical check object
        self.game = True

    # convenient mtd of assigning values to objects on a constructor
    def setup(self):
        self.car.center_x = SCREEN_WIDTH/2
        # estimate of y center at bottom
        self.car.center_y = CENTRE_Y_BOTTOM
        self.wall.center_y = SCREEN_HEIGHT
        #  place obstacle at an intial spot
        #(N/b calculation: 56-Width measurementh of screen edges. 281: full measurement of wall,
        # half of wall: 281/2 - 140.5, 140.5*0.8(compression of sprite ratio/size). Finally add 56+112.4=168.4)
        self.wall.center_x =  random.randint(168, (SCREEN_WIDTH-168))
        # indicate how much, wall moves down
        self.wall.change_y = WALL_SPEED

        
        

    # Release key controls for car to stop when keys aren't pressed
    def on_key_release (self, key, modifiers):
        # condition for releasing LEFT or RIGHT key
        if (key == arcade.key.LEFT) or (key == arcade.key.RIGHT):
            # movement should not take place(stop)
            self.car.change_x = 0
            self.car.angle = 0
         


    # key controls for game window 
    def on_key_press (self, key, modifiers):
        # condition that check if game is on
        #if self.game:
            # condition for moving to the left
        if key == arcade.key.LEFT:
            self.car.change_x = CAR_SPEED
            self.car.angle = CAR_ANGLE
            # condition for moving to the right
        if key == arcade.key.RIGHT:
            self.car.change_x =  CAR_SPEED
            self.car.angle =  -CAR_ANGLE

    # method for drawing to see changes on window
    def on_draw(self):
        #fill background with color
        self.clear()
        # property to draw the background, to display texture
        arcade.draw_texture_rectangle((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        # draw car sprite on window
        self.car.draw()

        # draw wall to reflect on window
        self.wall.draw()

        # condition to describe game stopped
        if not self.game:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH/2 - 220, SCREEN_HEIGHT/2, arcade.color.CYAN, font_size=60)
        
    # method to prescribe movement after appearing on window
    def update(self, delta_time):
        # make a conditiion to track sprite movement
        if self.game:
            self.car.update()
            self.wall.update()
        # create a collide check mtd for car and wall
        if arcade.check_for_collision(self.car, self.wall):
            # return False to "self.game object" to stop controls
            self.game = False


#  create an object for the class and call it
window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)   

window.setup()

arcade.run()
    


