import os
import time
import sys
import filecmp
import numpy as np
from skimage.io import imread
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import hashlib


def get_hash(in_path):
    
    image = Image.open(in_path)
    md5_hash = hashlib.md5(image.tobytes()).hexdigest()

    return md5_hash


if __name__ == '__main__':
    
    root = r"C:\Users\nobi4775\Pictures\MinecraftCake"
    root = r"C:\Users\nobi4775\Pictures"
    
    unique_files = set()
    hash_list = []
    t1 = time.time()
    
    try:
        not_dups = []
        for root_folder, folders, files in os.walk(root):
            
            for f in files:
                
                file_path = os.path.join(root_folder, f)
                ext = os.path.splitext(file_path)[1].lower()
                
                if ext in [".jpg", ".jpeg", ".png", ".gif"]:
                
                    try: 
                        hash_val = get_hash(file_path)
                        if not hash_val in hash_list:
                            hash_list.append(hash_val)
                        else:
                            not_dups.append(file_path)
                            
                        unique_files.add(hash_val)
                            
                    except Exception as ex:
                        #print(ex.args[0])
                        continue
                    
        total_time = time.time() - t1
        print("Time taken = {}".format(total_time))
    
    except Exception as ex:
        print(ex.args[0])