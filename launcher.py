import utils
import random

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

DIR_NAME = '0001'

img_width  = 28
img_height = 28
font_path = "/Library/Fonts/Arial Unicode.ttf"

rgb_bg  = (255, 255, 255)
rgb_letter = (0, 0, 0)

for i in range(10000):

    font_size = random.randrange(10, 20)
    font_width = font_size
    font_height = font_size + 1

    img_l_padding = random.randrange(0, int(img_width - font_width) + 1)
    img_t_padding = random.randrange(0, int(img_height - font_height) + 1)

    letter = utils.gen_korean_letter()
    font = ImageFont.truetype(font_path, font_size)
    img = Image.new("RGBA", (img_width, img_height), rgb_bg)
    draw = ImageDraw.Draw(img)
    draw.text((img_l_padding, img_t_padding), letter, rgb_letter, font=font)
    draw = ImageDraw.Draw(img)

    img_filename = str(ord(letter)) + '_' + utils.randomword(16)
    img.save("_data/" + DIR_NAME + '/' + img_filename + ".png")
