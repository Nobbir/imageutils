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
        
        
def listAllImages(root):
    
    try:
        #root = r"G:\Pictures" #\house_redlands\verona drive"
        #root = r"C:\temp"
        image_count = 0
        video_count = 0
        
        for root_folder, folders, files in os.walk(root):
            
            for f in files:
                
                file_path = os.path.join(root_folder, f)
                       
                ext = os.path.splitext(file_path)[1].lower()
                
                if ext in [".nef", ".db"]:
                    continue
                
                if ext in [".avi", ".mov", ".mpeg", ".mpg", ".mp4"]:
                    modifiedtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    print("{}: {}".format(file_path, modifiedtime))                    
                
                # check whether it's an image
                try:
                    img = Image.open(file_path)
                    image_count += 1
                    
                    exif = getExif(img)

                    if exif:
                        #print("Date time original - {} : {}".format(f, exif['DateTimeOriginal']))
                        #print("Date Taken - {} : {}".format(f, exif['DateTime']))  # WRONG WRONG
                        print("DateTaken - {} and Make - {}".format(exif['DateTime'], exif['Make']))
                    else:
                        # look for os.stat time information
                        modifiedtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                        if modifiedtime:
                            image_count += 1
                            print("Modified time: ", modifiedtime.year, modifiedtime.month, modifiedtime.day)
                        else:
                            print("{} has no timestamp")
                            
                except Exception as ex0:
                    
                    if ext in [".jpg", ".jpeg", ".png"]:
                        modifiedtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                        print("{}: {}".format(file_path, modifiedtime))
                    else:
                        print("NOT AN IMAGE: {}".format(file_path))
                        
                except Exception as ex:
                    print(ex.args[0])


    except Exception as ex:
        print(ex.args[0])
        
        

if __name__ == '__main__':

    root = r"C:\Users\farnf\OneDrive\Pictures\FromFujiCamera"
    root = r"C:\temp"
    root = r"C:\Users\farnf\Pictures\2016-07"
    root = r"D:\DCIM\101_FUJI"
    root = r"C:\Users\nobi4775\Pictures\NikonD60_2"
    
    listAllImages(root)


####dir_cmp = filecmp.dircmp(root1, root2)
##
####lefts = dir_cmp.left_only
####rights = dir_cmp.right_only

