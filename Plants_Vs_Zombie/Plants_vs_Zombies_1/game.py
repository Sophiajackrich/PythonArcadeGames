'''
    + Повторение
    + Познакомиться с правилами игры
    + Сделать заготовку игрового класса
    + Загрузить фон и игровое меню
    + Научиться определять нажатия по меню
    + Создать базовый класс для растений
    + Создать класс подсолнуха
    + Сделать выбор саженцев
    + Научиться перемещать саженец
    + Сделать посадку растений
    + Сделать так, чтобы растение размещалось по центру лужайки
    + Убрать возможность посадить несколько растений на одну лужайку
    + Сделать выводы урока
    + Получить домашнее задание

'''
import arcade
import plants



SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Plants VS Zombies'
CELL_WIDTH = 78
CELL_HEIGHT = 100

def lawn_x(x):
    right_x = 248 + CELL_WIDTH
    column = 1
    while right_x <= x:
        right_x += CELL_WIDTH
        column += 1
    center_x = right_x - CELL_WIDTH / 2
    return (center_x, column)

def lawn_y(y):
    top_y = 24 + CELL_HEIGHT
    line = 1
    while top_y <= y:
        top_y += CELL_HEIGHT
        line += 1
    center_y = top_y - CELL_HEIGHT / 2 
    return center_y, line

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        #Текстуры
        self.background = arcade.load_texture("textures/background.jpg")
        self.menu = arcade.load_texture("textures/menu_vertical.png")
        #спрайтлист
        self.plants = arcade.SpriteList()
        #поля
        self.seed = None
        self.lawns = []
        #Звуки
        self.seeding_sound = arcade.load_sound('sounds/seed.mp3')
        #Позиционирование объектов при старте
        self.setup()


    def setup(self):
        pass
    
    def on_draw(self):
        self.clear((255,255,255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_texture_rectangle(67, SCREEN_HEIGHT / 2, 134, SCREEN_HEIGHT, self.menu)
        self.plants.draw()
        if self.seed != None:
            self.seed.draw()


    def update(self, delta_time):
        self.plants.update_animation(delta_time)
        self.plants.update()

    def on_mouse_press(self, x, y, button, modifiers):
        if 16 <= x <= 116:
            if 370 <= y <= 480:
                self.seed = plants.SunFlower()
            if 255 <= y <= 365:
                print('PeaShooter')
            if 140 <= y <= 250:
                print('WallNut')
            if 25 <= y <= 135:
                print('TorchWood')
        if self.seed != None:
            self.seed.center_x = x
            self.seed.center_y = y
            self.seed.alpha = 150
    def on_mouse_motion(self, x, y, dx, dy):
        if self.seed != None:
            self.seed.center_x = x
            self.seed.center_y = y

    def on_mouse_release(self, x, y, button, modifiers):
        if 248 <= x <= 950 and 24 <= y <= 524 and self.seed != None:
            center_x, column = lawn_x(x)
            center_y, row = lawn_y(y)
            if (row, column) in self.lawns:
                self.seed = None
                return
            self.lawns.append((row, column))
            self.seed.planting(center_x, center_y, row, column)
            self.seed.alpha = 255
            self.plants.append(self.seed)
            self.seed = None
            arcade.play_sound(self.seeding_sound, 0.2)
        else:
            self.seed = None


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
