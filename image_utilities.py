import filecmp

from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
from PIL import ImageChops
from PIL import Image
from PIL import ImageStat


# image path is provided
def get_exif(img_path):
    
    ret = {}
    try:
        iv = Image.open(img_path)
        info = iv._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, value)
            ret[decoded] = value
        return ret

    except Exception as ex:
        print("{} does not have any exif".format(img_path))
        # use os.stat(image_path) to get time info
        return
    
    
exif_tags = ['CompressedBitsPerPixel', 'DateTimeOriginal', 'DateTimeDigitized', 'MaxApertureValue', 'MeteringMode',
             'LightSource', 'FocalLength', 'ExifImageWidth', 'Make', 'Model', 'SubsecTimeOriginal', 'Orientation',
             'YCbCrPositioning', 'SensingMethod', 'XResolution', 'YResolution', 'ExposureTime', 'ISOSpeedRatings',
             'FNumber', 'DateTime', 'ExifImageHeight']

logfile = open("image_without_exif.txt", "w")

for root, subfolder, files in os.walk(r'C:\Users\nobi4775\Pictures'):
        
    for f in files:
        
        file_name = os.path.join(root, f)
    
        if not os.path.splitext(f)[1].lower() in ['.jpeg', '.jpg', '.png']:
            continue
        #if not os.path.splitext(file_name)[1].lower() in ['.jpeg', '.jpg', '.png']:
            #continue
        
        try:
            d = None
            if os.path.splitext(file_name)[1].lower() in ['.jpeg', '.jpg', '.png']:
                d = get_exif(file_name)
            if d:
                if 'nikon' in d['Make'].lower():# == 'nikon': 
                    pass #print("{},{},{}\n".format(file_name, d['Make'], d['DateTimeOriginal']))
            else:
                # there is no exif for this file
                #print(file_name)
                logfile.write("{}\n".format(file_name))
            
        except Exception as ex:
            pass
    

    
logfile.close()
