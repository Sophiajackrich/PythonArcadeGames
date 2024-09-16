import arcade

from constants import *

# class for bullet
class Bullet(arcade.Sprite):

    def __init__(self, image, tank, side):
        super().__init__(image, 0.1)
        self.center_x = tank.center_x # register x coordinate for tank
        self.center_y = tank.center_y # register y coordinate for tank
        self.change_x = 12*tank.part_x # value for move in x direction
        self.change_y = 12*tank.part_y # value for move in y direction
        self.angle = tank.angle # angle of bullet should be tank angle
        self.side = side

        def update(self):
            self.center_x += self.change_x # move from x coordinate
            self.center_y += self.change_y # move from y coordinate
            # check if one of conditions is true, then kill bullet
            if self.left > SCREEN_WIDTH or self.right < 0 or self.bottom > SCREEN_HEIGHT or self.top < 0:
                self.kill()

