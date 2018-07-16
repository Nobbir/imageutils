import filecmp

from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
from PIL import ImageChops
from PIL import Image
from PIL import ImageStat

exif_tags = ['CompressedBitsPerPixel', 'DateTimeOriginal', 'DateTimeDigitized', 'MaxApertureValue', 'MeteringMode',
             'LightSource', 'FocalLength', 'ExifImageWidth', 'Make', 'Model', 'SubsecTimeOriginal', 'Orientation',
             'YCbCrPositioning', 'SensingMethod', 'XResolution', 'YResolution', 'ExposureTime', 'ISOSpeedRatings',
             'FNumber', 'DateTime', 'ExifImageHeight']

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
    
    



