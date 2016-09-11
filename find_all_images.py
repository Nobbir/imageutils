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
        root = r"C:\temp"
        image_count = 0
        video_count = 0
        
        for root_folder, folders, files in os.walk(root):
            
            for f in files:
                
                file_path = os.path.join(root_folder, f)
                #print(file_path)
##                if len(f.split(".")) == 2:
##                    if f.split(".")[1].lower() in ["avi", "mov", "mpeg", "mpg"]:
##                        video_count += 1
##                        #print(file_path)
                
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
                    ext = os.path.splitext(file_path)[1].lower()
                    if ext in [".jpg", ".jpeg", ".png"]:
                        modifiedtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                        print("{}: {}".format(file_path, modifiedtime))
                    else:
                        print("NOT AN IMAGE: {}".format(file_path))
                        
                except Exception as ex:
                    print(ex.args[0])
                       
        #print("{} : is total number of images.".format(image_count))
        #print("{} : is total number of videos.".format(video_count))  

    except Exception as ex:
        print(ex.args[0])
        
        

if __name__ == '__main__':

    root = r"C:\Users\farnf\OneDrive\Pictures\FromFujiCamera"
    root = r"C:\temp"
    root = r"C:\Users\farnf\Pictures\2016-07"
    root = r"D:\DCIM\101_FUJI"
    listAllImages(root)
    #try:
        #root = r"G:\Pictures" #\house_redlands\verona drive"
        #image_count = 0
        
        #for root_folder, folders, files in os.walk(root):
            
            #for f in files:
                
                #file_path = os.path.join(root_folder, f)
                #exif = get_exif(file_path)
                
                #if exif:
                    #print(exif['DateTimeOriginal'])
                    #image_count += 1
                #else:
                    #modifiedtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    #if modifiedtime:
                        #image_count += 1
                        #print("Modified time: ", modifiedtime.year, modifiedtime.month, modifiedtime.day)
                    #else:
                        #print("{} has no timestamp")                
                
        #print("{} : is total number of images.")
            

    #except Exception as ex:
        #print(ex.args[0])
    
##root1 = r'C:\MyPython\CompareOrganizeImage1'
##root2 = r'C:\MyPython\CompareOrganizeImage2'
##
##import os
##
##def fileExists(f1, f2):
##    if os.path.exists(f1):
##        print(f1)
##    if os.path.exists(f2):
##        print(f2)
##    
##dict1 = {}
##for dirs1, folders1, files1 in os.walk(root1):
##    for file1 in files1:
##        if not file1 in dict1.keys():
##            dict1[file1] = os.path.join(root1, file1)
##    
##dict2 = {}
##for dirs2, folders2, files2 in os.walk(root2):
##    for file2 in files2:
##        if not file2 in dict2.keys():
##            dict2[file2] = os.path.join(root2, file2)
##            
##exts = [".jpg", ".jpeg", ".png"]
##for file1, f1 in dict1.items():
##    
##    if file1 in dict2.keys():
##        comp = filecmp.cmp(f1, dict2[file1])
##        #if os.path.splitext(f1)[1].lower() in exts:
##            ##print(f1)
##            ##print(dict2[file1])
##            #del dict2[file1]
##        if comp:
##            print(file1)
##            print(dict2[file1])
##    else:
##        print("UNMATCHED: {}".format(file1))
##        #print(file2)
##            
##        #for file1 in files1:
##            
##            #f1 = os.path.join(root1, file1)
##            #if not os.path.exists(f1): continue
##            
##            #for file2 in files2:
##                
##                #f2 = os.path.join(root2, file2)
##                #if not os.path.exists(f2): continue
##                
##                #if file1 == file2:  # files have same name
##                    
##                    #if file1 == 'Thumbs.db' and file2 == 'Thumbs.db': 
##                        #continue
##                    #else:   
##                        #flag = filecmp.cmp(f1, f2)
##                        #if not flag:
##                            #print("{}\n{}".format(f1, f2))
##                #else:
##                    #pass
##                    
####dir_cmp = filecmp.dircmp(root1, root2)
##
####lefts = dir_cmp.left_only
####rights = dir_cmp.right_only
##
###print('done')
