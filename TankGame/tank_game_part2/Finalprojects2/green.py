import arcade
import math
from constants import *

class Green_Tank(arcade.Sprite):
    def __init__(self):
        super().__init__("green.png", 0.12)
        self.active = True
        self.shots = 0

    def update(self):
        if self.active:
            self.angle += self.change_angle
            self.part_x = math.cos(math.radians(self.angle))
            self.part_y = math.sin(math.radians(self.angle))
            self.center_x += self.part_x * self.change_x
            self.center_y += self.part_y * self.change_y
            if self.top > SCREEN_HEIGHT:
                self.top = SCREEN_HEIGHT
            elif self.bottom < 0:
                self.bottom = 0
            elif self.right > SCREEN_WIDTH:
                self.right = SCREEN_WIDTH
            elif self.left < 0:
                self.left = 0
    
    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x, self.center_y + 50, 50, 15, (255, 255, 255), 1)
        indent = self.shots*10
        arcade.draw_rectangle_filled(self.center_x-indent/2, self.center_y + 50, 50-indent, 13, (255, 255, 0))
