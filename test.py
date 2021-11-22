import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import math
import random

# image = Image.open("1.png")
# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype("Candy.ttf", 50)
# draw.text((10, 25), "world", font=font)
# image.save("22.png", "PNG")


def getmaincolor(img):
    img = img.convert('RGB')
    # 缩小图片，以减少计算量和限制最大色彩数
    img = img.resize((256, 256), Image.ANTIALIAS)
    colors = img.getcolors(maxcolors=256 * 256)
    colors_sorted_freq = sorted(colors, key=lambda x: x[0], reverse=True)

    # 提取颜色数
    color_num = 1

    # 获取主要色彩RGB列表
    main_RGB_list = [list(color[1]) for color in colors_sorted_freq[:color_num]]
    mainrgb = main_RGB_list[0]
    print(mainrgb)
    for i in range(0,len(mainrgb)):
        print(i)
        t = mainrgb[0]
        mainrgb[0] = mainrgb[2]
        mainrgb[2] = t
    # mainrgb[3] = 244
    print(mainrgb)
    return tuple(mainrgb)


img1 = Image.open("3.png")
img1 = img1.resize((400, 300), Image.ANTIALIAS)
af = getmaincolor(img1)
# img1 = img1.filter(ImageFilter.GaussianBlur(radius=5))
img1 = img1.filter(ImageFilter.MedianFilter(size=3))
img1 = img1.convert('RGBA')
draw = ImageDraw.Draw(img1)
font = ImageFont.truetype("Candy.ttf", 70)
draw.text((0, 105), "我的封面", font=font, fill=af)
img1.show()
# img2.save("blend2.png")


