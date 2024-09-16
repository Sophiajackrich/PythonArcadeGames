import arcade
#import os

# set the width, height and title of the window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Template"

# Create a Ball class from "arcade sprite"
class Ball(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y
        if self.left<0 or self.right>SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.bottom<0 or self.top>SCREEN_HEIGHT:
            self.change_y = -self.change_y 
        
        print("Left: ", self.left)
        print("Right: ", self.right)


# Create a Racket class
class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x

class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball("ball.png", 0.7)
        self.bar = Bar("bar.png", 0.5)
     
    # # logic
    def setup(self):
        self.ball.center_x = 300
        self.ball.center_y = 300
        self.ball.change_x = 5
        self.ball.change_y = 5
        self.bar.center_x = 300
        self.bar.center_y = 150
        self.bar.change_x = 1
        
    # objects drawing
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLUE)
        self.ball.draw()
        self.bar.draw()
        


    # updating the "game" class
    def update(self, delta_time):
        self.ball.update() 
        self.bar.update() 

game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

print("Hello")

#call the "setup" method 
game.setup() 
#game.maximize()


arcade.run()

