import os


def check_convertion_folders(path, convertion_path) -> None:
    """Creates the folders in which the converted images will output 
    if they don't exist, otherwise it doesn't create them"""
    for file in os.listdir(path):
        it_exists = os.path.exists(convertion_path)

        if not it_exists:
            os.makedirs(convertion_path)
