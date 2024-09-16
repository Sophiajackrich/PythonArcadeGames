import arcade
import random
import animate # sprite animation import
import time #import time

# SET CONSTANTS
SCREEN_TITLE = "Bomberman" # title of screen

CELL_WIDTH = 60 # cell width for one cell

CELL_HEIGHT = 60 # cell height for one cell

ROW_COUNT = 11 # no of rows of containing each cell on screen

COLUMN_COUNT = 11 # no of columns containing each cell on screen

SCREEN_WIDTH = CELL_WIDTH * COLUMN_COUNT # full screen width of Cell_width * number of columns

SCREEN_HEIGHT = CELL_HEIGHT * ROW_COUNT  # full screen height Cell_width * number of columns

PLAYER1_SPEED = 10

PLAYER2_SPEED = 10 

PLAYER1_BOMB_COUNT = 1

PLAYER2_BOMB_COUNT = 1

PLAYER1_POWER = 3

PLAYER2_POWER = 3

#left - 1;
#right - 2; 
#up -3; 
#down - 4.





# creat a function
def difference(coordinate, distance): 
    """This is a function that will take a certain coordinate , 
as well as a distance , 
and will calculate points using the formula that we previously wrote manually. 
That is, the x or y grid coordinate will be multiplied by the CELL_WIDTH or CELL_HEIGHT distance ,
and half the CELL_WIDTH / 2 or CELL_HEIGHT / 2 distance will be added to the resulting value

coordinate - x or y
distance - width or height

"""

    return coordinate * distance + distance/2


#create a function for bomb placement per square
def justify_x(position_x):
    """receive coordinate x as input, and
      then return coordinates that correspond to the placement rules.
     """
    #loop through column count and store in x
    for x in range(COLUMN_COUNT):
        #center x of cell width = 30
        cell_center_x = difference(x, CELL_WIDTH)
        #check if bomb position - 30(cell_center_x), is <= 30(cell_Width/2)
        if position_x - cell_center_x <= CELL_WIDTH / 2:
            #if condition is true, place bomb at the cell_center_x
            return cell_center_x 
    

def justify_y(position_y):
    """receive coordinate y as input, and
      then return coordinates that correspond to the placement rules.
     """
    for y in range(ROW_COUNT):
        #center x of cell width = 30
        cell_center_y = difference(y, CELL_HEIGHT)

        #check if bomb position - 30(cell_center_x), is <= 30(cell_Width/2)
        if position_y - cell_center_y <= CELL_HEIGHT / 2:
        #if condition is true, place bomb at the cell_center_x
            return cell_center_y  

#N/b: to get center of each cell, divide the entire cell by 2

#Create a class for adding sprites - solidblock
class SolidBlock(arcade.Sprite):
    
    #create instance of this class
    def __init__(self):
        # call instance of parent's class
        super().__init__('Blocks/SolidBlock.png', 1) 


# create another spritelist - explodable block
class ExplodableBlock(arcade.Sprite):

    def __init__(self):

        super().__init__('Blocks/ExplodableBlock.png', 1)



#create explosion class
class Explosion(animate.Animate):
    def __init__(self):

        super().__init__('Flame/Flame_f00.png', 0.7)

        for i in range(5):

            self.append_texture(arcade.load_texture(f'Flame/Flame_f0{i}.png'))
        #assign time attribute to an object of this class
        self.explosion_timer = time.time()
    
    #create an update methd for explosion class
    def update(self):

        if time.time() - self.explosion_timer > 2:

            self.kill() 

    # creat a method that checks collision with solidblock
    def check(self):

        hits = arcade.check_for_collision_with_list(self, window.solid_blocks)

        return len(hits) > 0 
    

# create a class for "Bomb"
class Bomb(animate.Animate):

    def __init__(self):

        super().__init__('Bomb/Bomb_f00.png',0.7)

        #create instance of time to an object
        self.bomb_timer = time.time() 

        #create a power attreibute for explosion
        self.power = 3

        #create a for loop to load bomb textures
        for i in range(3):

            self.append_texture(arcade.load_texture(f'Bomb/Bomb_f0{i}.png')) 
            print(i)

    #create a condition in an "update function" for the explosion to appear,
    # based on the difference between two periods of time:
    def update(self):
        #means cond should be met if 3secs have passed since the bomb appeared
        if time.time() - self.bomb_timer > 3: 
            #create an instance of the class and store to object
            exp = Explosion()
            #let explosion center and bomb center be same at x
            exp.center_x = self.center_x
            #let explosion center and bomb center be same at x
            exp.center_y = self.center_y
            #append instance to window explosions
            window.explosions.append(exp)
            
            # left direction of explosion
            left = True
            # right direction of explosion
            right = True
            # top direction of explosion
            top = True
            # bottom direction of explosion
            bottom = True

           
            #remove bomb
            self.kill() 

            #create a loop that diverge's bomb further
            for i in range(1, self.power+1):
                # add condition for all directions
                if left:
                    # create second explosion object - exp 1
                    exp1 = Explosion()

                    exp1.center_x = exp.center_x - CELL_WIDTH * i #30-60 = -30(left)

                    exp1.center_y = exp.center_y

                    window.explosions.append(exp1)

                    if exp1.check():
                        left = False

                #explosion 2
                if right:
                    exp2 = Explosion()

                    exp2.center_x = exp.center_x + CELL_WIDTH * i #30+60 = 90(left)

                    exp2.center_y = exp.center_y

                    window.explosions.append(exp2)
                    if exp2.check():
                        right = False
                
                #explosion 3
                if bottom:
                    exp3 = Explosion()

                    exp3.center_x = exp.center_x

                    exp3.center_y = exp.center_y - CELL_WIDTH * i #30-60 = -30(down)

                    window.explosions.append(exp3)
                    if exp3.check():
                        bottom = False
                
                #explosion 4
                if top:
                    exp4 = Explosion()

                    exp4.center_x = exp.center_x

                    exp4.center_y = exp.center_y + CELL_WIDTH * i #30+60 = 90(up)

                    window.explosions.append(exp4) #append to explosion lists
                    if exp4.check():
                        top = False

         
#create a class for main character
class Bomberman(animate.Animate):
    def __init__(self, speed, bomb_count, power):
        super().__init__("Bomberman/Front/Bman_F_f00.png",0.5)

        # Bomberman lists of textures
        self.walk_down_frames = [] # Front

        self.walk_up_frames = [] #Back

        self.walk_right_frames = [] #Right

        self.walk_left_frames = [] # Left

        for i in range(8):

            self.walk_down_frames.append(arcade.load_texture(f"Bomberman/Front/Bman_F_f0{i}.png")) 

            self.walk_up_frames.append(arcade.load_texture(f"Bomberman/Back/Bman_B_f0{i}.png"))

            self.walk_right_frames.append(arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png"))

            self.walk_left_frames.append(arcade.load_texture(f"Bomberman/Side/Bman_S_f0{i}.png", flipped_horizontally = True) )

        
        # Bomberman direction
        self.direction = 4 

        #track bomberman's movement
        self.motion = 0

        #set speed
        self.speed = speed

        #set initial bomb limit
        self.bomb_count = bomb_count

        #set explosion power
        self.power = power

        #win attribute
        self.win = False 

    # create a costume change method
    def costume_change(self):

        if self.direction == 1:

            self.textures = self.walk_left_frames

        elif self.direction == 2:

            self.textures = self.walk_right_frames

        elif self.direction == 3:

            self.textures = self.walk_up_frames

        elif self.direction == 4:

            self.textures = self.walk_down_frames 

    #create method for moving up,down,lef & right
    def to_up(self): #-part2
        #set condition for movement -part2
        if not self.motion:
            #set it to motion - part2
            self.motion = 1
            #set direction up(backing us)
            self.direction = 3
            #set movement along y axis(up) - part2
            self.change_y = self.speed

    #create method for moving down -=art2
    def to_down(self):
        #set condition for movement -part2
        if not self.motion:
            #set it to motion - part2
            self.motion = 1
            #set direction down, facing us - part2
            self.direction = 4
            #set movement along y axis(down) - part2
            self.change_y = -(self.speed)

    #create method for moving left -part2
    def to_left(self):
        #set condition for movement -part2
        if not self.motion:
            #set it to motion - part2
            self.motion = 1
            #set direction left - part2
            self.direction = 1
            #set movement in x direction - part2
            self.change_x = -(self.speed)

    #create method for moving up -part2
    def to_right(self):
        #set condition for movement -part2
        if not self.motion:
            #set it to motion - part2
            self.motion = 1
            #set direction right - part2
            self.direction = 2
            #change movement in y axis
            self.change_x = self.speed

    #method to stop movement - part2
    def to_stop(self):

        self.change_x = 0

        self.change_y = 0

        self.motion = 0 

    #define a method for checking collision
    def collisions(self, spritelist):
        # assign a variable to check for collision with solid block  -part2
        block_hit = arcade.check_for_collision_with_list(self, spritelist)
            # loop through var 
        for block in block_hit:
            #set conditions to check collisions
            if self.left <= block.right and self.direction == 1:
                self.left = block.right

            if self.right >= block.left and self.direction == 2:
                self.right = block.left

            if self.top >= block.bottom and self.direction == 3:
                self.top = block.bottom

            if self.bottom <= block.top and self.direction == 4:
                self.bottom = block.top 



    #update method
    def update(self):
        #adding movement to bomberman's position at x- part2
        self.center_x += self.change_x 
        #adding movement to bomberman's position at y- part2
        self.center_y += self.change_y 
        
        # seting condition for boarder and block awereness
        if self.left < 0:

            self.left = 0

        if self.right > SCREEN_WIDTH:

            self.right = SCREEN_WIDTH

        if self.bottom < 0:

            self.bottom = 0

        if self.top > SCREEN_HEIGHT:

            self.top = SCREEN_HEIGHT 

        #call collision method for both sides
        self.collisions(window.solid_blocks)

        self.collisions(window.explodable_blocks)            
        
       
#Create "Game" class
class Game(arcade.Window):
    # instance of game class
    def __init__(self, width, height, title):
        #parent constructs
        super().__init__(width, height, title)

        #load background image into this class(textures)
        self.bg = arcade.load_texture('Blocks/BackgroundTile.png') 
        #load win textures
        self.win1 = arcade.load_texture('win/win1.png')
        self.win2 = arcade.load_texture('win/win2.png')
        
        #load spritelists
        self.solid_blocks = arcade.SpriteList() #spritelist for solid blocks
        self.explodable_blocks = arcade.SpriteList() #spritelist for explodable blocks
        self.bombs_player1 = arcade.SpriteList() #spritelist for bomb
        self.explosions = arcade.SpriteList() # spritelist for explosion


        #Initializing Bomberman sprite

        self.bomberman = Bomberman(PLAYER1_SPEED, PLAYER1_BOMB_COUNT, PLAYER1_POWER)

        ##self.bomberman2 = Bomberman(PLAYER2_SPEED, PLAYER2_BOMB_COUNT, PLAYER2_POWER)
        
        #fields - check game on

        self.game = True

        #call setup method -Initializing sprites
        self.setup()




    # create a setup method
    def setup(self):
        #loop through the rows of the texture
        for y in range(ROW_COUNT):
            #in the rows, loop through their columns
            for x in range(COLUMN_COUNT): 
                #select only rows & columns that are odd
                if x % 2 == 1 and y % 2 == 1: 
                    #create an instance of class and save to an object
                    solid_block = SolidBlock()
                    # get center_x & center_y
                    solid_block.center_x = difference(x, CELL_WIDTH)

                    solid_block.center_y = difference(y, CELL_HEIGHT)

                    self.solid_blocks.append(solid_block)
                #select rows & columns if first condition doesn't select it
                elif random.randint(1, 2) == 1:
                    #create a negate(exception) block, for bomberman's appearance
                    if (not (x == 0 and y <= 2) and not (y == 0 and x <= 2) and  not (x == ROW_COUNT - 1 and y >= COLUMN_COUNT - 3) and not (y == COLUMN_COUNT - 1 and x >= ROW_COUNT - 3)):
                            exp_block = ExplodableBlock()
                        
                            exp_block.center_x = difference(x, CELL_WIDTH)

                            exp_block.center_y = difference(y, CELL_HEIGHT)

                            self.explodable_blocks.append(exp_block)
      
        #Getting the position of bomberman and assigning to x & y variables
        x = SCREEN_WIDTH / COLUMN_COUNT - CELL_WIDTH / 2

        y = SCREEN_HEIGHT / ROW_COUNT - CELL_HEIGHT / 2
 
        #setting bomberman's position on screen
        self.bomberman.set_position(x, y)
        ##self.bomberman2.set_position(x, y)
        print(x)
        print(y)

    #create a method that holds drawing background blocks
    def draw_background(self):
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                arcade.draw_texture_rectangle((difference(x, CELL_WIDTH)), (difference(y, CELL_HEIGHT)),CELL_WIDTH, CELL_HEIGHT, self.bg)


    # create draw method
    def on_draw(self):
        #window background
        self.clear()

        #draw texture background
        self.draw_background() 

        #draw spritelists
        self.solid_blocks.draw() 
        self.explodable_blocks.draw() 
        self.bombs_player1.draw() #player_1 bomb list
        self.explosions.draw() # draw explosion spritelist

        #main character class
        self.bomberman.draw() 
        ##self.bomberman2.draw()

        if self.bomberman.win:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH,SCREEN_HEIGHT, self.win1)
        self.game = False


    #create methods for keyboard control
    def on_key_press(self,key,modifiers):
        if self.game:
            if key == arcade.key.LEFT:
                #call left movement method -part2
                self.bomberman.to_left()

            elif key == arcade.key.RIGHT:
                #call right movement method
                self.bomberman.to_right()

            elif key == arcade.key.UP:
                #call up movement method -part2
                self.bomberman.to_up()

            elif key == arcade.key.DOWN:
                #call down movement method -part2
                self.bomberman.to_down()

            self.bomberman.costume_change() 

            #add bomb control
            if key == arcade.key.SPACE:
                # creat condition to limit the placement of bombs. 
                if len(self.bombs_player1) < self.bomberman.bomb_count:
                    bomb = Bomb() 
                    bomb.center_x = justify_x(self.bomberman.center_x)

                    bomb.center_y =  justify_y(self.bomberman.center_y)
                    # bomberman power attribute
                    bomb.power = self.bomberman.power
                    #append the bomb textures in the empty list on the game class
                    self.bombs_player1.append(bomb) 
                    
                  

    #create methods for keyboard control release
    def on_key_release(self,key,modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.UP or key == arcade.key.DOWN:
            self.bomberman.to_stop()

# create update method to make the objects move
    def update(self, delta_time):
        if self.game:
            #call bomberman animate method 
            self.bomberman.update_animation(delta_time)
           

            #call the bomberman's update method -part2
            self.bomberman.update() 
           

            # update spritelist bomb
            self.bombs_player1.update()
            
            # update animation for spritelist
            self.bombs_player1.update_animation(delta_time)
            

            # # update spritelist bomb
            self.explosions.update()
            #update nimation for spritelist
            self.explosions.update_animation() 

            # use a for loop to create a list of collision
            for flame in self.explosions:
                #store the collisions btw flames and explodable blocks  
                explosions = arcade.check_for_collision_with_list(flame,self.explodable_blocks)
                # use a condition to check if the explosion list is greater than 0
                if len(explosions) > 0:
                    #for every item in list
                    for block in explosions:
                        #kill the item
                        block.kill()

                # create a variable to store collision
                hit_list = arcade.check_for_collision_with_list(flame,self.solid_blocks)
                # condition if hit_list > 0
                if len(hit_list) > 0:
                    #if condition met, kill only flame
                    flame.kill()  

                #condition to check for collision between flame and bomberman characters
                if arcade.check_for_collision(flame, self.bomberman):
                    self.bomberman.color = (0,0,0)
                    self.bomberman.win = True

            

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


window.setup() 

arcade.run() 



