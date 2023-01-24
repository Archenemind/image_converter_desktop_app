import os
import pillow_avif
from PIL import Image
from create_convertion_folders import check_existence_of_convertion_folders


def directory_script(path):
       
    path_out_webp = f'{path}/convertedImgsWebp'
    path_out_png = f'{path}/convertedImgsPng'
    path_out_avif = f'{path}/convertedImgsAvif'

    path640 = f'{path}/imgs640'
    path_out_webp640 = f'{path}/convertedImgsWebp640'
    path_out_png640 = f'{path}/convertedImgsPng640'
    path_out_avif640 = f'{path}/convertedImgsAvif640'

    path1280 = f'{path}/imgs1280'
    path_out_webp1280 = f'{path}/convertedImgsWebp1280'
    path_out_png1280 = f'{path}/convertedImgsPng1280'
    path_out_avif1280 = f'{path}/convertedImgsAvif1280'

    check_existence_of_convertion_folders(path, path_out_avif)
    check_existence_of_convertion_folders(path, path_out_avif1280)
    check_existence_of_convertion_folders(path, path_out_avif640)

    check_existence_of_convertion_folders(path, path640)
    check_existence_of_convertion_folders(path, path_out_png)
    check_existence_of_convertion_folders(path, path_out_png1280)
    check_existence_of_convertion_folders(path, path_out_png640)

    check_existence_of_convertion_folders(path, path1280)
    check_existence_of_convertion_folders(path, path_out_webp)
    check_existence_of_convertion_folders(path, path_out_webp1280)
    check_existence_of_convertion_folders(path, path_out_webp640)
    
    # j = 0 
    # z = 0
    # for filename in os.listdir(path):
    #     if not filename.lower().endswith(('.jpg','.png','webp','AVIF')):
    #         j+=1
            
   
    for filename in os.listdir(path): 
   
        try:                           
            clean_name = os.path.splitext(filename)[0]
            img = Image.open(f"{path}/{filename}")
            img.save(f'{path_out_webp}/{clean_name}.webp')
            img.save(f'{path_out_png}/{clean_name}.png')
            img.save(f'{path_out_avif}/{clean_name}.AVIF')

            change_width640 = Image.open(f"{path}/{filename}")
            change_width640.thumbnail((640, 640))
            change_width640.save(f'{path640}/{clean_name}.jpg')
            change_width640.save(f'{path_out_webp640}/{clean_name}.webp')
            change_width640.save(f'{path_out_png640}/{clean_name}.png')
            change_width640.save(f'{path_out_avif640}/{clean_name}.AVIF')

            change_width1280 = Image.open(f"{path}/{filename}")
            change_width1280.thumbnail((1280, 1280))
            change_width1280.save(f'{path1280}/{clean_name}.jpg')
            change_width1280.save(f'{path_out_webp1280}/{clean_name}.webp')
            change_width1280.save(f'{path_out_png1280}/{clean_name}.png')
            change_width1280.save(f'{path_out_avif1280}/{clean_name}.AVIF')
        except:
            continue
            