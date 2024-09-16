# Continuation of MotionAnimation
import arcade

# set the width, height and title  of the window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Template"

class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_x1 = 300 

        self.center_y1 = 300 

        self.center_x2 = 300 

        self.center_y2 = 300

        self.side1 = 60 

        self.side2 = 60

        self.change_x = 5 

        self.change_y = 5

    # objects drawing
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        
        # draw first square using “draw_rectangle_filled” command
        arcade.draw_rectangle_filled(self.center_x1, self.center_y1, self.side1, self.side1, arcade.color.BLACK)
        
        # draw second square using “draw_rectangle_outline” command
        arcade.draw_rectangle_outline(self.center_x2, self.center_y2, self.side2, self.side2, arcade.color.PURPLE, 5)
    
    # Update method
    def update(self, delta_time): 
        #  add a shift to the coordinate of the center horizontally
        self.center_x1 += self.change_x
        # add a condition for 1st square  to bounce off edge
        if ((self.center_x1 + self.side1/2) > SCREEN_WIDTH) or ((self.center_x1 - self.side1/2) < 0): 

            self.change_x = -self.change_x

        # add a condition for 1st square to bounce off edge(up/down)
        self.center_y1 += self.change_y 
        if ((self.center_y1 + self.side1) > SCREEN_WIDTH) or ((self.center_y1 - self.side1) < 0): 

            self.change_y = -self.change_y  
    

        # SECOND SQUARE
        # add a condition for 2nd square  to bounce off edge(up/down)
        self.center_y2 += self.change_y 
        if ((self.center_y2 + self.side2) > SCREEN_WIDTH) or ((self.center_y2 - self.side2) < 0): 

            self.change_y = -self.change_y  

game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
