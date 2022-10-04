import os
from PIL import Image
import pillow_avif

def check_existence_of_convertion_folders(path, convertion_path):
    for filename in os.listdir(path):
        it_exists = os.path.exists(convertion_path)
    
        if not it_exists:
            os.makedirs(convertion_path)


#path = input()
#path2 = f'{path}/shu'

#for filename in os.listdir(path):
#    it_exists = os.path.exists(path2)
    
#    if not it_exists:
#        os.makedirs(path2)

    
        
        