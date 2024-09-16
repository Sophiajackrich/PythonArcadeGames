import arcade

# set the width, height and title  of the window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Template"

class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_x = 300 
        self.center_y = 300 
        self.radius = 50
        self.change_x = 5
        self.change_y = 5 

    # objects drawing
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, arcade.color.BLUE)

    # logic
    def update(self, delta_time):
        # Add the change_x to the center_x
        self.center_x+=self.change_x
        # create a condition for bouncing off the left/right edge
        if ((self.center_x + self.radius) > SCREEN_WIDTH) or ((self.center_x- self.radius) < 0) :
            self.change_x = -self.change_x
        # Add the change_y to the center_y
        self.center_y += self.change_y
        # create a condition for bouncing off the top/bottom edge
        if self.center_y + self.radius > SCREEN_HEIGHT or self.center_y - self.radius < 0: 
            self.change_y =-self.change_y
        
            

game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
