'''
    Цель   урока: начать программировать игру «Танки». Создать фон, главного персонажа и дать ему возможность стрелять.
    + повторить команды из прошлых уроков;
    + обсудить правила игры;
    + загрузить фон;
    + создать зеленый танк;
    + запрограммировать вращение танка;
    + запрограммировать движение танка;
    + создать класс Bullet;
    + запрограммировать возможность выстрела;
    + настроить полет пули;
    + сделать выводы урока;
    + получить домашнее задание.

'''
import arcade
import math
import time

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Arcade Tanks"

class Bullet(arcade.Sprite):
    def __init__(self, image, tank):
        super().__init__(image, 0.1)
        self.center_x = tank.center_x
        self.center_y = tank.center_y
        self.change_x = 12*tank.part_x
        self.change_y = 12*tank.part_y
        self.angle = tank.angle
        

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left > SCREEN_WIDTH or self.right < 0 or self.bottom > SCREEN_HEIGHT or self.top < 0:
            self.kill()



class Green_Tank(arcade.Sprite):
    def __init__(self):
        super().__init__("green.png", 0.12)
        self.active = True

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



class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        #Текстуры
        self.background = arcade.load_texture("background.png")
        #Спрайты
        self.green = Green_Tank()
        #Спрайтлисты
        self.projectiles = arcade.SpriteList()
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


    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.green.draw()
        self.projectiles.draw()

    def update(self, delta_time):
        self.green.update()
        self.projectiles.update()


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
            shell = Bullet("green_bullet.png", self.green)
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
