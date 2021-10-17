#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import time

from PIL import Image, ImageDraw, ImageFont
from lib import epd5in65f


class BilibiliInfo:

    dir_path = os.path.dirname(__file__)
    font_file = os.path.join(dir_path, 'fonts', 'font.ttf')

    epd = None

    font18 = None
    font24 = None
    font40 = None

    def __init__(self):
        self.font18 = ImageFont.truetype(self.font_file, 18)
        self.font24 = ImageFont.truetype(self.font_file, 24)
        self.epd = epd5in65f.EPD()

    def generate_image(self):
        image = Image.new('RGB', (self.epd.width, self.epd.height), 0xffffff)
        draw = ImageDraw.Draw(image)

        draw.line((0, 0, self.epd.width - 1, self.epd.height - 1), fill=0)
        return image

    def save_image(self, image):
        image.save('test.bmp')

    def display(self, image):
        self.epd.init()
        self.epd.Clear()

        self.epd.display(self.epd.getbuffer(image))
        time.sleep(3)
        self.epd.sleep()


if __name__ == '__main__':
    obj = BilibiliInfo()
    image = obj.generate_image()
    obj.save_image(image)
