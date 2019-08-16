from PIL import Image

import argparse

'''

Image模块是PIL中最重要的模块，它提供了诸多图像操作的功能，比如创建、打开、显示、保存图像等功能，合成、裁剪、滤波等功能，获取图像属性功能，如图像直方图、通道数等。

'''

#直接输出至控制台

IMG ='G1.jpg'

HEIGHT =80   #设置输出也是压缩后图片高度

WIDTH =100   #设置输出后也是压缩后图片的宽度

ascii_char =list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")    #用来绘制字符画所用到的字符



def get_char(r,g,b,alpha =256):

    if alpha ==0:

        return ' '

    length =len(ascii_char)

    gray =int(0.2126 * r +0.7152 * g +0.0722 * b)

    unit = (256.0 +1)/length

    return ascii_char[int(gray/unit)]



im = Image.open(IMG)

print(im.getbands())#图片所拥有的波段，比如 R G B A

print(im.mode)#图片颜色模式

im = im.resize((WIDTH,HEIGHT),Image.NEAREST)    #实现图片的缩放功能

txt =""

for i in range(HEIGHT):

    for j in range(WIDTH):

        txt += get_char(*im.getpixel((j,i)))

    txt +='\n'

print(txt)
