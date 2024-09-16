import arcade
import math
from constants import * 

class Green_Tank(arcade.Sprite):
    def __init__(self, window):
        super().__init__("tank_game_part1/green.png", 0.12)        
        #Fields-activate
        self.active =True
        self.shots = 0
        self.window = window

    def draw(self):
        super().draw() 
        #draw rectangle outline
        arcade.draw_rectangle_outline(self.center_x, self.center_y + 50, 50, 15, (255, 255, 255), 1)
        indent = self.shots*10
        # draw a filled rectangle
        arcade.draw_rectangle_filled(self.center_x-indent/2, self.center_y + 50, 50-indent, 13, (255, 255, 0)) 

    def update(self):
        if self.active:
            self.angle += self.change_angle #change/rotate angle direction
            #fields if moving diagonally
            self.part_x = math.cos(math.radians(self.angle))# cal. of the cosine angle 
            self.part_y = math.sin(math.radians(self.angle)) # cal. of the sine angle
            self.center_x += self.change_x * self.part_x #move along x direction
            self.center_y += self.change_y * self.part_y #move along y direction
            if self.top > SCREEN_HEIGHT:
                self.top = SCREEN_HEIGHT
            elif self.bottom < 0:
                self.bottom = 0

            elif self.right > SCREEN_WIDTH:
                self.right = SCREEN_WIDTH

            elif self.left < 0:
                self.left = 0
   
            hits = arcade.check_for_collision_with_list(self, self.window.projectiles)
            for bullet in hits:
                if not bullet.side:
                    self.shots += 1 
                    bullet.kill()
            if self.shots >= 5:
                self.texture = arcade.load_texture("tank_game_part1/tank_game3/green_broken.png")
                self.shots = 5
                self.active = False 
                    