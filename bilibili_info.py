#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import time

from PIL import Image, ImageDraw, ImageFont

import fetch_bilibili_info
from lib.driver import epd5in65f


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
        self.font40 = ImageFont.truetype(self.font_file, 40)
        self.epd = epd5in65f.EPD()

    def draw_image(self, data):
        image = Image.new('RGB', (self.epd.width, self.epd.height), 0xffffff)
        draw = ImageDraw.Draw(image)

        draw.text((0, 0), str(data['myFollower']), font=self.font40, fill=self.epd.BLUE)

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

    fetchBilibiliInfo = fetch_bilibili_info.FetchBilibiliInfo()

    myFollower = fetchBilibiliInfo.fetch_my_follower()

    data = {
        "myFollower": myFollower,
    }
    image = obj.draw_image(data)
    obj.display(image)
