import arcade

# set the width, height and title of the window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Template"

class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    # оobjects drawing
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)

    # logic
    def update(self, delta_time):
        pass

game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
