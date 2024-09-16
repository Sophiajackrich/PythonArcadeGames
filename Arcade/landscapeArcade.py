import arcade 

class Landscape(arcade.Window):
    # set constructor(initialization-initials)
    def __init__(self, width, height, title):
        # assigning parent parameters to this class
        super().__init__(width, height, title)
    
    # create a method for bird
    def bird(self, x, y):
        arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90) # left wing
        arcade.draw_arc_outline(x + 20, y, 20, 20, arcade.color.BLACK, 90, 180) # right wing

    # create a function for Tree
    def tree(self, x, y):
        arcade.draw_rectangle_filled(x, y, 20, 90, arcade.color.DARK_BROWN)

        arcade.draw_circle_filled(x + 10, y + 40, 40, arcade.color.DARK_GREEN)
  
    def house(self, x, y):
        arcade.draw_rectangle_filled(x, y, 100, 80, arcade.color.CORN) # wall

        arcade.draw_rectangle_filled(x, y, 30, 30, arcade.color.LIGHT_BLUE) # window

        arcade.draw_triangle_filled(x1=x, y1=y+80, x2=x-50, y2=y+40, x3=x+50, y3=y+40, color=arcade.color.RED_BROWN) # roof


    def on_draw(self):
        # start process
        arcade.start_render()
        # set background
        arcade.set_background_color(arcade.color.BABY_BLUE)
        # set command to draw a rectangle for landscape shape
        arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.color.GREEN)
        # draw circle for sun
        arcade.draw_circle_filled(100, 350, 20, arcade.color.YELLOW)
        # call thhe bird method
        self.bird(300,300)
        self.bird(400,350)

        # call the Tree method
        self.tree(500, 120) 
        self.tree(120, 100)

        # calling house function
        self.house(330, 125)





landscape = Landscape(600,400,"Scenery")

arcade.run()