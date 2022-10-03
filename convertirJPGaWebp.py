import os
from PIL import Image
import pillow_avif

path = input("Writte the name of the file to convert: ")

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    change_width = Image.open(f"{path}/{filename}")

    clean_name = os.path.splitext(filename)[0]
    
    img.save(f'{path}/{clean_name}.webp')
    img.save(f'{path}/{clean_name}.png')
    img.save(f'{path}/{clean_name}.AVIF')

    change_width.thumbnail((640, 640))

    change_width.save(f'{path}/{clean_name}640.jpg')
    change_width.save(f'{path}/{clean_name}640.webp')
    change_width.save(f'{path}/{clean_name}640.png')
    change_width.save(f'{path}/{clean_name}640.AVIF')
    
for filename in os.listdir(path):
    
    img = Image.open(f"{path}/{filename}")
    img.thumbnail((1280, 1280))
    
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{path}/{clean_name}1280.jpg')
    img.save(f'{path}/{clean_name}1280.webp')
    img.save(f'{path}/{clean_name}1280.png')
    img.save(f'{path}/{clean_name}1280.AVIF')