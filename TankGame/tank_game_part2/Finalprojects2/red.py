import arcade
import math
from constants import *

class Red_Tank(arcade.Sprite):
    def __init__(self):
        super().__init__("red.png", 0.12)
        self.active = True
        self.angle = 180
        self.shots = 0
    
    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x, self.center_y + 50, 50, 15, (255, 255, 255), 1)
        indent = self.shots*10
        arcade.draw_rectangle_filled(self.center_x-indent/2, self.center_y + 50, 50-indent, 13, (255, 165, 0))
