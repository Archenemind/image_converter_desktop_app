import os
import pillow_avif
from PIL import Image

def manage_exception_for_RGBA(image, clean_name,path640, path_out_webp640,path_out_png640,path_out_avif640):
    image.convert('RGB')
    image.thumbnail((640, 640))
    image.save(f'{path640}/{clean_name}.jpg')
    image.save(f'{path_out_webp640}/{clean_name}.webp')
    image.save(f'{path_out_png640}/{clean_name}.png')
    image.save(f'{path_out_avif640}/{clean_name}.AVIF')
