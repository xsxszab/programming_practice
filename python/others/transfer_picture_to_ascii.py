#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:19:14 2018

@author: xsxsz
"""

from PIL import Image

ASCII_CHARS = [' ', '#', '?', '%', '.', '+', '.', '*', ':', ',', '"']
img_name='1.png'
               
def scale(img,width=60):
    (original_width, original_height) = img.size
    height=int(width*original_height/float(original_width)*0.5)
    new_img=img.resize((width,height))
    return new_img

def transform(img,charlist,range=25):
    img=img.convert('L')
    pixels_in_image = list(img.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range)] for pixel_value in pixels_in_image]
    return img,"".join(pixels_to_chars)

def convert(img_name,new_width=60):
    img=Image.open(img_name)
    img=scale(img)
    img,pixel_to_chars=transform(img,ASCII_CHARS)
    length=len(pixel_to_chars)
    image_ascii = [pixel_to_chars[index: index + new_width] for index in range(0, length, new_width)]
    return "\n".join(image_ascii)

print('-------------------------------------------')
print(convert(img_name=img_name))
print('-------------------------------------------')
