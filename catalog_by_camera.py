import filecmp

from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
from PIL import ImageChops
from PIL import Image
from PIL import ImageStat
import imageutils

exif_tags = ['CompressedBitsPerPixel', 'DateTimeOriginal', 'DateTimeDigitized', 'MaxApertureValue', 'MeteringMode',
             'LightSource', 'FocalLength', 'ExifImageWidth', 'Make', 'Model', 'SubsecTimeOriginal', 'Orientation',
             'YCbCrPositioning', 'SensingMethod', 'XResolution', 'YResolution', 'ExposureTime', 'ISOSpeedRatings',
             'FNumber', 'DateTime', 'ExifImageHeight']

logfile = open("catalog_Nikon.csv", "wb")

for root, subfolder, files in os.walk(r'F:\Pictures'):
        
    for f in files:
        
        file_name = os.path.join(root, f)
    
        if os.path.splitext(file_name)[1] not in ['.JPEG', '.JPG', '.jpeg', '.jpg', '.png', '.PNG']:
            continue
        
        try:
            #im = Image.open(file_name)
            d = imageutils.get_exif(file_name)
            #print(file_name)
            if 'nikon' in d['Make'].lower():# == 'nikon': 
                logfile.write("{},{},{}\n".format(file_name, d['Make'], d['DateTimeOriginal']))
            
        except Exception as ex:
            pass



#logfile.write("\n\nTotal number of photos: {}\n".format(i))
logfile.close()
    

    
