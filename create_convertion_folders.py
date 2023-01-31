import os
from PIL import Image

def check_existence_of_convertion_folders(path, convertion_path):
        
    for filename in os.listdir(path):
        it_exists = os.path.exists(convertion_path)
    
        if not it_exists:
            os.makedirs(convertion_path)