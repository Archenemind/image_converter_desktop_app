import os
import pillow_avif  # This module is used but pylint doesn't recognize it
from PIL import Image, UnidentifiedImageError
from create_convertion_folders import check_convertion_folders


class Folder():
    def __init__(self, path) -> None:
        self.path = path

        self.out_path_webp = f'{path}/converted_imgs_webp'
        self.out_path_png = f'{path}/converted_imgs_png'
        self.out_path_avif = f'{path}/converted_imgs_avif'

        self.path640 = f'{path}/imgs_640'
        self.out_path_webp_640 = f'{path}/converted_imgs_webp640'
        self.out_path_png_640 = f'{path}/converted_imgs_png640'
        self.out_path_avif_640 = f'{path}/converted_imgs_avif640'

        self.path1280 = f'{path}/imgs_1280'
        self.out_path_webp_1280 = f'{path}/converted_imgs_webp_1280'
        self.out_path_png_1280 = f'{path}/converted_imgs_png_1280'
        self.out_path_avif_1280 = f'{path}/converted_imgs_avif_1280'

    def create_folders(self) -> None:
        check_convertion_folders(self.path, self.out_path_avif)
        check_convertion_folders(self.path, self.out_path_avif_1280)
        check_convertion_folders(self.path, self.out_path_avif_640)

        check_convertion_folders(self.path, self.path640)
        check_convertion_folders(self.path, self.out_path_png)
        check_convertion_folders(self.path, self.out_path_png_1280)
        check_convertion_folders(self.path, self.out_path_png_640)

        check_convertion_folders(self.path, self.path1280)
        check_convertion_folders(self.path, self.out_path_webp)
        check_convertion_folders(self.path, self.out_path_webp_1280)
        check_convertion_folders(self.path, self.out_path_webp_640)

    def create_images(self):
        for filename in os.listdir(self.path):

            try:
                clean_name = os.path.splitext(filename)[0]
                img = Image.open(f"{self.path}/{filename}")
                img.save(f'{self.out_path_webp}/{clean_name}.webp')
                img.save(f'{self.out_path_png}/{clean_name}.png')
                img.save(f'{self.out_path_avif}/{clean_name}.avif')

                change_width640 = Image.open(f"{self.path}/{filename}")
                change_width640.thumbnail((640, 640))
                change_width640.save(
                    f'{self.out_path_webp_640}/{clean_name}.webp')
                change_width640.save(
                    f'{self.out_path_png_640}/{clean_name}.png')
                change_width640.save(
                    f'{self.out_path_avif_640}/{clean_name}.avif')

                if change_width640.mode in ("RGBA", "P"):
                    change_width640 = change_width640.convert("RGB")

                change_width640.save(f'{self.path640}/{clean_name}.jpg')

                change_width1280 = Image.open(f"{self.path}/{filename}")
                change_width1280.thumbnail((1280, 1280))
                change_width1280.save(
                    f'{self.out_path_webp_1280}/{clean_name}.webp')
                change_width1280.save(
                    f'{self.out_path_png_1280}/{clean_name}.png')
                change_width1280.save(
                    f'{self.out_path_avif_1280}/{clean_name}.avif')

                if change_width1280.mode in ("RGBA", "P"):
                    change_width1280 = change_width1280.convert("RGB")

                change_width1280.save(f'{self.path1280}/{clean_name}.jpg')

            except PermissionError:
                continue
            except UnidentifiedImageError:
                continue
