import os


def check_convertion_folders(path, convertion_path):

    for filename in os.listdir(path):
        it_exists = os.path.exists(convertion_path)

        if not it_exists:
            os.makedirs(convertion_path)
