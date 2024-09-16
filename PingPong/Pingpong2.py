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
        
        # print("Left: ", self.left)
        # print("Right: ", self.right)


# Create a Racket class
class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        # add a condition for "Racket" touching left & right edges
        if self.right > SCREEN_WIDTH: 

            self.right = SCREEN_WIDTH 

        if self.left < 0: 

            self.left = 0

class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball("ball.png", 0.7)
        self.bar = Bar("bar.png", 0.5)
     
    # # logic
    def setup(self):
        # setup for "Ball" class
        self.ball.center_x = 300
        self.ball.center_y = 300
        self.ball.change_x = 5
        self.ball.change_y = 5

        # setup for "Bar" class
        self.bar.center_x = 300
        self.bar.center_y = 150
        self.bar.change_x = 0

        # create a score property
        self.score = 0

        # create an attempts property
        self.attempts = 3
        
    # objects drawing
    def on_draw(self):
        # start draw process
        arcade.start_render()
        # set background for window
        arcade.set_background_color(arcade.color.BLUE)
        #draw ball
        self.ball.draw()
        #draw bar
        self.bar.draw()

        # create a text string for score on window
        text_score = f"Score: {self.score}"

        # display/place text on window
        arcade.draw_text(text_score, 10, 570, arcade.color.GLITTER, 20)

        # text description for attempts
        text_attempts = f" Attempts : { self.attempts}"
        arcade.draw_text(text_attempts, 370, 570, arcade.color.BLACK, 20)

    # create a keyboard method functionality
    def on_key_press(self, key, modifiers):
          if key == arcade.key.RIGHT:
              self.bar.change_x=5
          if key == arcade.key.LEFT: 
              self.bar.change_x = -5
    # control/checks the keys release movement
    def on_key_release ( self, key, modifiers):
          if key == arcade.key.RIGHT or key == arcade.key.LEFT: 
              self.bar.change_x = 0

        


    # updating the "game" class
    def update(self, delta_time):
        self.ball.update() 
        self.bar.update() 
        # checking if ball&racket collide
        if arcade.check_for_collision(self.ball, self.bar):
            #if the condition is True,

            #move the ball above the racket, and
            self.ball.bottom= self.bar.top

            #change its direction of flight
            self.ball.change_y=-self.ball.change_y

            #Increase score
            self.score+=1 
            # print score
            print(self.score)

        # check if the racket does not hit the ball, then reduce attempts,.
        if self.ball.bottom < 0: 
            self.attempts -= 1
            print(self.attempts)

            # put ball straight back up, after fall
            self.ball.center_y = 500

        # stop game, if attempts is exhausted
        if self.attempts == 0: 

            self.ball.stop() 

            self.bar.stop()
            



game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

print("Hello")

#call the "setup" method 
game.setup() 
#game.maximize()


arcade.run()

