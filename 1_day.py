'''使用help()了解类中实现的方法和函数'''

# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageDraw
im  = Image.open("C:/Users/zhangkuoru/Pictures/头像.jpg")
draw = ImageDraw.Draw(im)
#draw.line((0, 0) + im.size, fill=128)
#draw.rectangle([0,0,60,60],(255,244,142),width=100)
draw.text((im.size[0]-40,0),'hello',(255,0,255),draw.getfont(),None,4,"left","rtl")
print(draw.getfont())
im.rotate(0).show()
