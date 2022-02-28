'''
Image Gallery
- Create an image abstract class and then a class that inherits from it for each image type.
- Put them in a program which displays them in a gallery style format for viewing.
- My solution for https://github.com/karan/Projects-Solutions (Image Gallery Abstract Classes) see lib.py
'''

import arcade
import glob
from lib import Image
from pathlib import Path

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"
MOVEMENT_SPEED = 63


class ImageGallery(arcade.Window):
    """
    Main application class.

    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.DARK_TAN)
        self.image_sprites = arcade.SpriteList()
        self.images = []

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        x = 60
        y = 60
        for file in glob.glob('images' + '/*.*'):
            print(file)
            self.images.append(Image(file, x, y))
            x += 120
        for image in self.images:
            self.image_sprites.append(image.sprite)

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        self.image_sprites.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        for _image in self.images:
            _image.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        """

        if key == arcade.key.LEFT or key == arcade.key.A:
            for sprite in self.image_sprites:
                sprite.center_x = sprite.center_x - MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            for sprite in self.image_sprites:
                sprite.center_x = sprite.center_x + MOVEMENT_SPEED


def main():
    """ Main function """
    game = ImageGallery(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
