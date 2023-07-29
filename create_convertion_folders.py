import os
from shutil import rmtree


def check_convertion_folders(path, convertion_path) -> None:
    """Creates the folders in which the converted images will output 
    if they don't exist, otherwise it doesn't create them"""
    for file in os.listdir(path):
        it_exists = os.path.exists(convertion_path)

        if not it_exists:
            os.makedirs(convertion_path)


def delete_all_convertion_folders(path):
    """Function executes if there is an exception"""
    rmtree(f'{path}/converted_imgs_webp')
    rmtree(f'{path}/converted_imgs_png')
    rmtree(f'{path}/converted_imgs_avif')
    rmtree(f'{path}/imgs_640')
    rmtree(f'{path}/converted_imgs_webp640')
    rmtree(f'{path}/converted_imgs_png640')
    rmtree(f'{path}/converted_imgs_avif640')
    rmtree(f'{path}/imgs_1280')
    rmtree(f'{path}/converted_imgs_webp_1280')
    rmtree(f'{path}/converted_imgs_png_1280')
    rmtree(f'{path}/converted_imgs_avif_1280')
