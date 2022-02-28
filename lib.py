from abc import ABC, abstractmethod
from pathlib import Path
from arcade import Sprite


class ImageAbstract(ABC):
    @abstractmethod
    def rescale(self, size):
        pass

    @abstractmethod
    def alpha(self, alpha):
        pass

    @abstractmethod
    def update(self, alpha):
        pass


class Image(ImageAbstract):

    def __init__(self, file_name, cx, cy):
        #self.path = Path(f'{file_name}')
        self.sprite = Sprite(file_name, center_x=cx, center_y=cy)
        self.active = False
        self.rescale(.3)

    def rescale(self, size):
        self.sprite.scale = size

    def alpha(self, alpha):
        self.sprite.alpha = alpha

    def update(self):
        if self.sprite.center_x < 60 or self.sprite.center_x > 780:
            self.sprite.alpha = 150
        else:
            self.sprite.alpha = 255

        if 400 < self.sprite.center_x < 450:
            self.rescale(1.2)
            self.sprite.center_y = 360
        else:
            self.rescale(.3)
            self.sprite.center_y = 60
