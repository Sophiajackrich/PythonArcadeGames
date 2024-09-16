import arcade as a
class OurPicture(a.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
    def on_draw(self):
        # To start the rendering(drawing) process
        a.start_render()
        # Command to set the background
        a.set_background_color(a.color.DARK_GREEN)
        # Command for the circle
        a.draw_circle_filled(300, 300, 200, a.color.BLIZZARD_BLUE)
        # To draw the first eye
        a.draw_circle_filled(380, 350, 20, a.color.BLACK)
        # To draw the second eye
        a.draw_circle_filled(220, 350, 20, a.color.BLACK)
        # COMMAND FOR THE MOUTH
        center_x = 300 # x co-ordinate for the center
       
        center_y = 230 # x co-ordinate for the center
        
        width = 150 # To set the width 

        height = 80 # To set height

        start_angle = 180 # To set where the arc angle begins

        end_angle = 360 # To set where the arc angle ends

        line_width = 10 # set width of the line for smile
       
        # Now apply the variables inside the command below
        a.draw_arc_outline(center_x, center_y, 
                           width, height, a.color.BLACK,
                             start_angle, end_angle, 
                             line_width)


# create an object for "OurPicture" class
window = OurPicture(600,600,"Smile")
a.run()