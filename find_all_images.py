import os
import sys
import filecmp
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

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

# an image is provided
def getExif(img):
    ret = {}
    info = img._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, value)
        ret[decoded] = value
    return ret

# image path is provided
def get_exif(img_path):
    ret = {}
    try:
        with Image.open(img_path) as iv:
            info = iv._getexif()
            for tag, value in info.items():
                decoded = TAGS.get(tag, value)
                ret[decoded] = value
            return ret
    except Exception as ex:
        print("Image {} does not have any exif".format(img_path))
        # use os.stat(image_path) to get time info
        return
        
        
def ConvertTimestampToLong(date_str):  # e.g., '2010:07:14 20:43:00'
    
    dt = date_str.split()[0]
    tm = date_str.split()[1]
    year, month, day = dt.split(":")
    year = int(year.strip())
    month = int(month.strip())
    day = int(day.strip())

    hour, minute, second = tm.split(":")
    hour = int(hour.strip())
    minute = int(minute.strip())
    second = int(second.strip())

    return second * 1 + minute * 100 + hour * 10000 + day * 1000000 + month * 100000000 + year * 10000000000

    
def ConvertTimestampToDateTime(date_str): # e.g., '2010:07:14 20:43:00'

    dt = date_str.split()[0]
    tm = date_str.split()[1]
    year, month, day = dt.split(":")
    year = int(year.strip())
    month = int(month.strip())
    day = int(day.strip())

    hour, minute, second = tm.split(":")
    hour = int(hour.strip())
    minute = int(minute.strip())
    second = int(second.strip())

    return year, month, day, hour, minute, second


def listAllImages(root):

    makes = []
    try:
        #root = r"G:\Pictures" #\house_redlands\verona drive"
        #root = r"C:\temp"
        image_count = 0
        video_count = 0
        
        for root_folder, folders, files in os.walk(root):
            
            for f in files:
                
                file_path = os.path.join(root_folder, f)   # f is file name, e.g., AM234.jpg
                       
                ext = os.path.splitext(file_path)[1].lower()
                
                if ext in [".nef", ".db", ".psd", ".modd", ".moff", ".thm", ".py", ".lnk"]:
                    continue
                
                if ext in [".avi", ".mov", ".mpeg", ".mpg", ".mp4"]:
                    #consider only images for now ------------------
                    #modifiedtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    #print("{}: {}".format(file_path, modifiedtime))    
                    continue
                
                # check whether it's an image
                try:
                    img = Image.open(file_path)
                    image_count += 1
                    
                    exif = getExif(img)

                    if exif:
                        date_time_org = ConvertTimestampToDateTime(exif['DateTimeOriginal'])
                        date_time_taken = ConvertTimestampToDateTime(exif['DateTime'])   # this is the one work FIRST
                        camera = exif['Make']
                        if camera not in makes:
                            #print(camera)
                            makes.append(camera)
                        #print("DateTaken - {} and Make - {}".format(exif['DateTime'], exif['Make']))
                    else:
                        # look for os.stat time information
                        modifiedtime = datetime.fromtimestamp(os.path.getmtime(file_path))   # returns a time string 
                        if modifiedtime:
                            image_count += 1
                            #print("Modified time: ", modifiedtime.year, modifiedtime.month, modifiedtime.day)
                        else:
                            print("{} has no timestamp")
                            
                except Exception as ex0:
                    
                    if ext in [".jpg", ".jpeg", ".png"]:
                        modifiedtime = datetime.fromtimestamp(os.path.getmtime(file_path))   # returns a DateTime object
                        #print("{}: {}".format(file_path, modifiedtime))
                    else:
                        print("NOT AN IMAGE: {}".format(file_path))
                        
                except Exception as ex:
                    print(ex.args[0])

        print(makes)
    except Exception as ex:
        print(ex.args[0])
        
        

if __name__ == '__main__':
    """
    Searching Python list of dictionaries: http://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
    user generator expression : https://www.python.org/dev/peps/pep-0289/
    >>> dicts = [
    ...     { "name": "Tom", "age": 10 },
    ...     { "name": "Mark", "age": 5 },
    ...     { "name": "Pam", "age": 7 },
    ...     { "name": "Dick", "age": 12 }
    ... ]
    
    >>> (item for item in dicts if item["name"] == "Pam").next()
    {'age': 7, 'name': 'Pam'}
    
    """

    root = r"C:\Users\farnf\OneDrive\Pictures\FromFujiCamera"
    root = r"C:\temp"
    root = r"C:\Users\farnf\Pictures\2016-07"
    root = r"D:\DCIM\101_FUJI"
    root = r"C:\Users\nobi4775\Pictures\NikonD60_2"
    root = r"C:\Users\nobi4775\Pictures"
    root = r"C:\Users\farnf\OneDrive\Pictures"
    root = r"C:\Users\farnf\Pictures"
    root = r"F:\Pictures"
    listAllImages(root)


####dir_cmp = filecmp.dircmp(root1, root2)
##
####lefts = dir_cmp.left_only
####rights = dir_cmp.right_only

