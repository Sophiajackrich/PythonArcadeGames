import arcade
import math
import time
import green
import red
from tank_game_part2 import base
from constants import *
import bullet


class Game(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)
           
        #Textures
        self.background = arcade.load_texture("tank_game_part1/background.png")

        #Sprites
        self.green = green.Green_Tank(self)
        self.green_base = base.Base("tank_game_part1/tank_game_part2/green_base.png", self,(255, 255, 0))
        self.red_base = base.Base("tank_game_part1/tank_game_part2/red_base.png", self, (255, 0, 0))

        #Fields
        self.left_pressed = False
        self.right_pressed = False 
        self.up_pressed = False
        self.down_pressed = False
        self.run = True
        self.result = 'run'

        #Spritelists/regularList
        self.projectiles = arcade.SpriteList()
        self.red_tanks = []


        #Initialize sprite coordinates

        self.setup() 



    def setup(self):
        self.green.center_x = 90
        self.green.center_y = 110
        self.green_base.center_x = 165
        self.green_base.center_y = 350
        self.red_base.center_x = 1035
        self.red_base.center_y = 350
        for i in range(1, 4):
            tank = red.Red_Tank(self)
            tank.center_x = 800
            tank.center_y = 200 * i - 50
            self.red_tanks.append(tank) 



    def on_draw(self):
        self.clear((255,255,255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.green.draw()
        self.projectiles.draw() #draw all bullets in list
        self.green_base.draw()
        self.red_base.draw() 
        if self.result == 'win':
            arcade.draw_text("You won!!!", 300, SCREEN_HEIGHT/2, (255,255,0), 80)

        elif self.result == 'losing':
            arcade.draw_text("You lost :(", 300, SCREEN_HEIGHT/2, (255,135,0), 80) 

        # add a draw method for each red tank in the regular tank list
        for tank in self.red_tanks:
            tank.draw() 

    def on_key_press(self, key, modifiers):
        if self.green.active:
            if key == arcade.key.LEFT:
                self.green.change_angle = 2.5
                self.left_pressed = True #activate when pressed
                self.right_pressed = False #deactivate if left is pressed

            if key == arcade.key.RIGHT:
                self.green.change_angle = -2.5
                self.right_pressed = True #activate when pressed
                self.left_pressed = False #deactivate if right is pressed
            
            if key == arcade.key.UP:
                self.green.change_x = 4
                self.green.change_y = 4
                self.up_pressed = True #activate if pressed
                self.down_pressed = False #deactivate if up_pressed

            if key == arcade.key.DOWN:
                self.green.change_x = -3
                self.green.change_y = -3
                self.down_pressed = True #activate if pressed
                self.up_pressed = False #deactivate if up_pressed
                
            if key == arcade.key.SPACE:
                shell =  bullet.Bullet("tank_game_part1/green_bullet.png", self.green, 1) #variable to store green bullet
                self.projectiles.append(shell) #append green bullet to bullet list
        


    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT and not self.right_pressed:
            self.green.change_angle = 0
        
        if key == arcade.key.RIGHT and not self.left_pressed:
            self.green.change_angle = 0

        if key == arcade.key.UP and not self.down_pressed:
            self.green.change_x = 0
            self.green.change_y = 0

        if key == arcade.key.DOWN and not self.up_pressed:
            self.green.change_x = 0
            self.green.change_y = 0

    def update(self, delta_time):
        if self.run:
            red_destroyed = 0
            self.green.update()
            self.projectiles.update() #update bullet list
            self.red_base.update()
            self.green_base.update() 
            for red_tank in self.red_tanks:
                red_tank.update()
                if red_tank.shots >= 5:
                    red_destroyed += 1
            if self.green.shots >= 5 or self.green_base.shots >= 10:
                self.run = False 
                self.result = 'losing'
            # if there ae 3 broken red tanks or 10 or greater hits on red base, then victory and stop game
            if self.red_base.shots >= 10 and red_destroyed == 3:
                self.run = False 
                self.result = 'win' 


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run() 