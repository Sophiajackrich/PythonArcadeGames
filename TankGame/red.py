import arcade
import math
import time
import bullet as bul
from constants import *

class Red_Tank(arcade.Sprite):

    def __init__(self, window):
        super().__init__("tank_game_part1/tank_game_part2/red.png", 0.12)
        self.active = True 
        self.angle = 180 
        self.shots = 0
        self.window = window
        self.bullet_time = time.time()
        self.part_x = 0
        self.part_y = 0 
        self.change_x = 1
        self.change_y = 1

    def fire(self):
        if time.time() - self.bullet_time >= 2: 
            self.part_x = math.cos(math.radians(self.angle))
            self.part_y = math.sin(math.radians(self.angle))
            shell = bul.Bullet("tank_game_part1/tank_game3/red_bullet.png", self, 0) 
            self.window.projectiles.append(shell)
            self.bullet_time = time.time() 

    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x, self.center_y + 50, 50, 15, (255, 255, 255), 1)
        indent = self.shots*10
        arcade.draw_rectangle_filled(self.center_x-indent/2, self.center_y + 50, 50-indent, 13, (255, 0, 0)) 
       
    def update(self):
        if self.active:
            hits = arcade.check_for_collision_with_list(self, self.window.projectiles)
            for bullet in hits:
                if bullet.side:
                    bullet.kill()
                    self.shots += 1 
            if self.shots >= 5:
                self.texture = arcade.load_texture("tank_game_part1/tank_game3/red_broken.png")
                self.shots = 5 
                self.active = False

            delta_x = self.window.green.center_x - self.center_x
            delta_y = self.window.green.center_y - self.center_y 

            radius = arcade.get_distance_between_sprites(self, self.window.green)
            if radius <= 250:
                self.angle = math.degrees(math.atan2(delta_y, delta_x))
                self.fire()
                self.part_x = math.cos(math.radians(self.angle))
                self.part_y = math.sin(math.radians(self.angle))
                self.center_x += self.part_x * self.change_x
                self.center_y += self.part_y * self.change_y

            elif arcade.get_distance_between_sprites(self.window.green_base, self) <= 400:
                delta_x = self.window.green_base.center_x - self.center_x
                delta_y = self.window.green_base.center_y - self.center_y
                self.angle = math.degrees(math.atan2(delta_y, delta_x))
                self.fire()

            else:
                self.angle = 180 
                self.center_x -= 1