import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 680
MOVEMENT_SPEED = 7
COIN_SPEED = 1

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.5
COIN_COUNT = 600

def write_high_score(result):
    f = open('highscore.txt','w')  # w : writing mode  /  r : reading mode  /  a  :  appending mode
    f.write('{}'.format(result))
    f.close()

class Player(arcade.Sprite):

    def update(self):
        self.center_y += self.change_y
        self.center_x += self.change_x

        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.left < 0:
            self.left = 0

        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
        
        if self.bottom < 0:
           self.bottom = 0

class Coin(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 600)
        self.center_x = random.randrange(SCREEN_WIDTH)
    
    def update(self):
        self.center_y -= COIN_SPEED
        if self.top < 0:
            self.reset_pos()
            self.lives = self.lives - 1

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Goblin Gobbler")

        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        self.player_sprite = None
        self.score = 0
        self.lives = 3
        self.highscore = 0
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLUE_GRAY)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.score = 0
        self.lives = 10
        self.highscore = 0

        self.player_sprite = Player("hughby.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = Coin("gobbo.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(400, 5000)

            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 400, 20, arcade.color.WHITE, 20)
        output = f"Lives: {self.lives}"
        arcade.draw_text(output, 500, 20, arcade.color.WHITE, 20)

        result = self.score
        write_high_score(result)

        #convert the following three lines to a read_high_score functiom
        #check that it still works fine!
        #now, instead of just write_high_score(result), you can put an if statement (to check if the self.score is bigger than the high score that we read)

        f = open('highscore.txt', 'r')
        highscore = f.readline()
        f.close()
        output = f"Highscore: {self.highscore}"
        arcade.draw_text(output, 250, 20, arcade.color.WHITE, 20)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

#    def on_key_press(self, key, modifiers):
 #       if key == arcade.key.LEFT:
  #          self.player_sprite.change_x = -MOVEMENT_SPEED
   #     elif key == arcade.key.RIGHT:
    #        self.player_sprite.change_x = MOVEMENT_SPEED
     #   elif key == arcade.key.UP:
      #      self.player_sprite.change_y = MOVEMENT_SPEED
       # elif key == arcade.key.DOWN:
        #    self.player_sprite.change_y = -MOVEMENT_SPEED

#    def on_key_release(self, key, modifiers):
 #      if key == arcade.key.LEFT or key == arcade.key.RIGHT:
  #         self.player_sprite.change_x = 0
   #    elif key == arcade.key.UP or key == arcade.key.DOWN:
    #       self.player_sprite.change_y = 0

    def update(self, delta_time):
        self.bullet_list.update()
        self.coin_list.update()
        self.player_list.update() 
        
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            global COIN_SPEED
            coin.remove_from_sprite_lists()
            self.score += 1
            COIN_SPEED = COIN_SPEED + 0.05

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
