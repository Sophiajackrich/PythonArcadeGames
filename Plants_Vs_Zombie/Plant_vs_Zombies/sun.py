import arcade
import time


class Sun(arcade.Sprite):

    def __init__(self, center_x, center_y):

         super().__init__('items/sun.png', 0.12)

         self.center_x = center_x

         self.center_y = center_y

         #the current time for sun
         #self.live = time.time()

    def update(self):
         #increase rotation angle by 1degree
         self.angle += 0.1
         #check if subtraction btw current time and suns time planted more or equal to 3 seconds
     #     if time.time() - self.live >= 3:
     #         #kill, if condition is True
     #         self.kill()