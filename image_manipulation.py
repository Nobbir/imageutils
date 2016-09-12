import os
import sys
import filecmp
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from PIL import ImageEnhance


exif_keys = ['LightSource', 'YResolution', 'ResolutionUnit', 'FlashPixVersion',
             'Make', 'Flash', 'SceneCaptureType', 'DateTime', 'MeteringMode',
             'XResolution', 'Contrast', 'Saturation', 'MakerNote', 'ExposureProgram',
             'FocalLengthIn35mmFilm', 'ColorSpace', 'ExifImageWidth',
             'ExposureBiasValue', 'DateTimeOriginal', 'UserComment',
             'SceneType', 'Software', 'SubjectDistanceRange', 'WhiteBalance',
             'CompressedBitsPerPixel', 'DateTimeDigitized', 'SensingMethod',
             'FNumber', 'CustomRendered', 'FocalLength', 'SubsecTimeOriginal',
             'ExposureMode', 'ComponentsConfiguration', 'ExifOffset',
             'ExifImageHeight', 'SubsecTimeDigitized', 'ISOSpeedRatings',
             'Model', 'Orientation', 'ExposureTime', 'FileSource', 'SubsecTime',
             'MaxApertureValue', 'ExifInteroperabilityOffset', 'CFAPattern',
             'Sharpness', 'GainControl', 'YCbCrPositioning', 'DigitalZoomRatio',
             'ExifVersion']


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
        print("Image {} does not have any exif".format(img_path))
        # use os.stat(image_path) to get time info
        return
        

        

if __name__ == '__main__':

    sample_image = os.path.join(os.getcwd(), "rubyct.JPG")
    
    try:
        image = Image.open(sample_image)
        enhancer = ImageEnhance.Contrast(image)
        enhancer = ImageEnhance.Color(image)
        im = enhancer.enhance(0.5)
        im.show()
    except:
        print("Not an image")