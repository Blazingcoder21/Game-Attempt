import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'ARCADE'
SCALING = 2.0
print("hello 1")

class SpaceShooter(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.run()



    def on_draw(self):
        arcade.start_render()
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.setup()

    def setup(self):
        self.player = arcade.Sprite("Jet.png", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)
        arcade.schedule(self.add_enemy, 0.25)
        arcade.schedule(self.add_cloud, 1.0)

    def add_enemy(self, delta_time: float):
        enemy = FlyingSprite("Missile.png", SCALING)
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)
        enemy.velocity = (random.randint(-20, -5), 0)
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)
        print("Enemy")




    def add_cloud(self, delta_time: float):
        cloud = FlyingSprite("Cloud.png", SCALING)
        cloud.left = random.randint(self.width, self.width + 80)
        cloud.top = random.randint(10, self.height - 10)
        cloud.velocity = (random.randint(-20, -5), 0)
        self.clouds_list.append(cloud)
        self.all_sprites.append(cloud)
        print("Hello")


class FlyingSprite(arcade.Sprite):
    def update(self):
        super().update()

        if self.right < 0:
            self.remove_from_sprite_lists()


x = SpaceShooter(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
x.on_draw()




#arcade.finish_render()


