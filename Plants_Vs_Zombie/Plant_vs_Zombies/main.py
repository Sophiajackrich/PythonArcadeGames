import arcade
import plant
from constants import *

SCREEN_WIDTH = 1000

SCREEN_HEIGHT = 600

SCREEN_TITLE = 'Plants VS Zombies'

"""determine the row / column of field to plant at the center of each cells
#cell width - 950 - 248 = 702 / 9 horizontal cells = 78
#cell height - 524 - 24 = 500 / 5 vertical cells = 100
"""
# Cell width & Cell column Constants
CELL_WIDTH = 78

CELL_HEIGHT = 100




#determine x of playing center
def lawn_x(x):
    """To calculate the coordinate of the right edge of the first cell,
       if the field starts at coordinate 248 and
       the cell width is 78, 
       which is written in the CELL_WIDTH constant.
       That's right, add 248 and CELL_WIDTH ."""
    # first cell from the right at coordinate x
    right_x = 248 + CELL_WIDTH

    column = 1
    #while the right_x is less or equal to x
    while right_x <= x:
        #add cell_width to the right_x
        right_x += CELL_WIDTH
        #while loop goes on, increase its column
        column += 1
        # calculate center_x of a cell 
    center_x = right_x - CELL_WIDTH / 2 #subtract current right_x - (78/2)
        #return center_x and the column
    return center_x, column
    

# function to determine center of cell & row number
def lawn_y(y):
    top_y = 24 + CELL_HEIGHT
    row = 1
    while top_y <= y:
        top_y += CELL_HEIGHT
        row += 1
    #det center of the cell
    center_y = top_y - CELL_HEIGHT / 2 #subtract current top_y - (100/2)
    return center_y, row

#create game class
class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        #Textures

        self.background = arcade.load_texture("textures/background.jpg")

        self.menu = arcade.load_texture("textures/menu_vertical.png")

        #spritelist

        self.plants = arcade.SpriteList()
        self.spawn_suns = arcade.SpriteList()
        self.peas = arcade.SpriteList()

        #fields

        self.seed = None
        #number of row and column on field
        self.lawns = [] #store an empty list

        self.sun = 300
        
        #Positioning of objects at start
        self.setup()


    def setup(self):

        pass


    def on_draw(self):
        self.clear((255,255,255))

        #draw background
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        #draw menu
        arcade.draw_texture_rectangle(67, SCREEN_HEIGHT / 2, 134, SCREEN_HEIGHT, self.menu)
        
        arcade.draw_text(f'{self.sun}', 34, 490, (165, 42, 42), 30)
        
        #draw plants
        self.plants.draw()

        #draw seed, if condition is met
        if self.seed is not None:

            self.seed.draw()

        self.spawn_suns.draw()
        self.peas.draw()


    #mouse control
    def on_mouse_press(self, x, y, button, modifiers):
        if 16 <= x <= 116:
            if 370 <= y <= 480:
                self.seed = plant.Sunflower(self)
                print("SunFlower")
            if 255 <= y <= 365:
                self.seed = plant.PeaShooter(self)
                print('PeaShooter')

            if 140 <= y <= 250:

                print('WallNut')

            if 25 <= y <= 135:

                print('TorchWood')

        # placing seedling where mouse is, if selected
        if self.seed is not None:

            self.seed.center_x = x

            self.seed.center_y = y

            self.seed.alpha = 150

        for sun in self.spawn_suns:

            if sun.left <= x <= sun.right and sun.bottom <= y <= sun.top:

                sun.kill()

                self.sun += 25

        print(x, y)

    def on_mouse_motion(self, x, y, dx, dy):
        #if seed is not none
        if self.seed is not None:
            #set seed position_x wherever mouse is
            self.seed.center_x = x
            #set seed position_y wherever mouse is
            self.seed.center_y = y

    def on_mouse_release(self, x, y, button, modifiers):
        #if mouse x&y coordinates meet the condition and seed is not none
        if 248 <= x <= 950 and 24 <= y <= 524 and self.seed is not None:
            # center of cell on oordinate x & y
            center_x, column = lawn_x(x)

            center_y, row = lawn_y(y)

            #check if rows and columns exists in "self.lawns"
            if (row, column) in self.lawns or self.sun < self.seed.cost:
                self.seed = None
                return #return empty value i.e nothing
            self.sun -= self.seed.cost
            #if empty, append lawns
            
            self.lawns.append((row, column))
            
            #call the planting method to plant seeds
            self.seed.planting(center_x, center_y, column,row)
            #make the plant opaque
            self.seed.alpha = 255
            #add to the plants list 
            self.plants.append(self.seed)
            #Now make the seed object "None"
            self.seed = None
        #if condition "if" is not met i.e releasing sead outside condition
        else:

            self.seed = None

        #Game class update
    def update(self, delta_time):
        self.plants.update_animation(delta_time)

        self.plants.update()
        self.peas.update()

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()