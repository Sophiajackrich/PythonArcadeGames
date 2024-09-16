'''
    Цель   урока: запрограммировать вторую часть игры «Танки»: добавить базы, врагов, а также сделать видимые рабочие полоски здоровья.
    
    + повторить команды прошлых уроков;
    + добавить базы для танков; 
    + запрограммировать для них полоски здоровья;
    + добавить возможность наносить урон красной базе, играя за зеленый танк;
    + создать полоску здоровья для зеленого танка;
    + добавить красные танки и полоски здоровья для них;
    + сделать выводы урока;
    + получить домашнее задание.
'''
import arcade
import base
import green
from constants import *
import bullete
import red


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        #Текстуры
        self.background = arcade.load_texture("background.png")
        #Спрайты
        self.green = green.Green_Tank()
        self.green_base = base.Base("green_base.png", self, (255, 255, 0))
        self.red_base = base.Base("red_base.png", self,(255, 165, 0))
        #Спрайтлисты
        self.projectiles = arcade.SpriteList()
        self.red_tanks = []
        #Поля
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        #Инициализация координат спрайтов 
        self.setup()

    def setup(self):
        self.green.center_x = 90
        self.green.center_y = 190
        self.green_base.center_x = 165
        self.green_base.center_y = 350
        self.red_base.center_x = 1035
        self.red_base.center_y = 350
        for i in range(1, 4):
            tank = red.Red_Tank()
            tank.center_x = 800
            tank.center_y = 200 * i - 50
            self.red_tanks.append(tank)




    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.green.draw()
        self.projectiles.draw()
        self.green_base.draw()
        self.red_base.draw()
        for tank in self.red_tanks:
            tank.draw()



    def update(self, delta_time):
        self.green.update()
        self.projectiles.update()
        self.red_base.update()
        self.green_base.update()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.green.change_angle = 2.5
            self.left_pressed = True
            self.right_pressed = False
        if key == arcade.key.UP:
            self.green.change_x = 4
            self.green.change_y = 4
            self.up_pressed = True
            self.down_pressed = False

        if key == arcade.key.DOWN:
            self.green.change_x = -3
            self.green.change_y = -3
            self.up_pressed = False
            self.down_pressed = True

        if key == arcade.key.RIGHT:
            self.green.change_angle = -2.5
            self.left_pressed = False
            self.right_pressed = True
        
        if key == arcade.key.SPACE:
            shell = bullete.Bullet("green_bullet.png", self.green)
            self.projectiles.append(shell)
            

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


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
