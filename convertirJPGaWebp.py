import os
from PIL import Image
import pillow_avif

path = './imgs'
path_out_webp = '/convertedImgsWebp'
path_out_png = '/convertedImgsPng'
path_out_avif = '/convertedImgsAvif'

path640 = '/imgs640'
path_out_webp640 = '/convertedImgsWebp640'
path_out_png640 = '/convertedImgsPng640'
path_out_avif640 = '/convertedImgsAvif640'

path1280 = '/imgs1280'
path_out_webp1280 = '/convertedImgsWebp1280'
path_out_png1280 = '/convertedImgsPng1280'
path_out_avif1280 = '/convertedImgsAvif1280'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    change_width = Image.open(f"{path}/{filename}")

    clean_name = os.path.splitext(filename)[0]
    
    img.save(f'.{path_out_webp}/{clean_name}.webp')
    img.save(f'.{path_out_png}/{clean_name}.png')
    img.save(f'.{path_out_avif}/{clean_name}.AVIF')

    change_width.thumbnail((640, 640))

    change_width.save(f'.{path640}/{clean_name}.jpg')
    change_width.save(f'.{path_out_webp640}/{clean_name}.webp')
    change_width.save(f'.{path_out_png640}/{clean_name}.png')
    change_width.save(f'.{path_out_avif640}/{clean_name}.AVIF')
    
for filename in os.listdir(path):
    
    img = Image.open(f"{path}/{filename}")
    img.thumbnail((1280, 1280))
    
    clean_name = os.path.splitext(filename)[0]
    img.save(f'.{path1280}/{clean_name}.jpg')
    img.save(f'.{path_out_webp1280}/{clean_name}.webp')
    img.save(f'.{path_out_png1280}/{clean_name}.png')
    img.save(f'.{path_out_avif1280}/{clean_name}.AVIF')