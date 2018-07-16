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

exif_keys = ['LightSource', 'YResolution', 'ResolutionUnit', 'FlashPixVersion',
             'Make', 'Flash', 'SceneCaptureType', 'DateTime', 'MeteringMode',
             'XResolution', 'Contrast', 'Saturation', 'MakerNote', 'ExposureProgram',
             'ColorSpace', 'ExifImageWidth', 'FocalLengthIn35mmFilm',
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

# simplified names of Cameras
camera_dict = {u'Apple': 'iPhone', u'EASTMAN KODAK COMPANY': 'Kodak', u'NIKON CORPORATION': 'Nikon', 
               u'Canon': 'Canon', u'SONY': 'Sony', u'Nokia': 'Other', u'LGE': 'Other', 
               u'PENTAX': 'Other', u'Panasonic': 'Other'}


def compareImages(test_files):
    """
    i = 0
    for dirs, folders, files in os.walk(root):
        #print(dirs)
        if folder in dirs.split(os.sep):
            test_files = [os.path.join(dirs, f) for f in files]
            if i == 0:
                base_files = test_files[:]
            else: # i > 0
                compareImages(test_files)
            i += 1
    """
    for file1 in base_files:
        for file2 in test_files:
            if filecmp.cmp(file1, file2, 0):
                print(file1)
                break

            
# input '2016:08:01 22:12:20'
# output: a tuple of 6 numbers
def parseDateTime(dt_string):
    
    if not dt_string: return
    
    _date = dt_string.split()[0]
    _time = dt_string.split()[1]
    
    d = _date.split(":")
    t = _time.split(":")
    
    year = int(d[0].strip())
    month = int(d[1].strip())
    day = int(d[2].strip())
    hour = int(t[0].strip())
    minute = int(t[1].strip())
    second = int(t[2].strip())
    
    return [year, month, day, hour, minute, second]


# image path is provided
def get_exif(img_path):
    """
    pic = r"C:\Users\nobi4775\Pictures\amelia_fokla_IMG_2381.JPG"
    pic2 = r"C:\Users\nobi4775\Pictures\Eid2015_Fab_Me_Am.jpg"    #r'C:\Users\nobi4775\Pictures\me_savar_abedin_home2'
    exif1 = getExif(pic)
    exif2 = getExif(pic2)

    if exif1 and 'DateTimeOriginal' in exif1.keys():
        date1 = parseDateTime(exif1['DateTimeOriginal'])
    else:
        date1 = None
        
    if exif2 and 'DateTimeOriginal' in exif2.keys():
        date2 = parseDateTime(exif2['DateTimeOriginal'])
    else:
        date2 = None
        
    if date1 and date2:
        print(testListEquality(date1, date2))
    """
    ret = {}
    try:
        with Image.open(img_path) as iv:
            #iv = Image.open(img_path)
            info = iv._getexif()
            if not info: "Handle the situation ??????"
            for tag, value in info.items():
                decoded = TAGS.get(tag, value)
                ret[decoded] = value
            return ret, iv

    except Exception as ex:
        print("{} does not have any exif".format(img_path))
        # use os.stat(image_path) to get time info
        print(ex.args[0])
        return
    
    



