import os
import sys
import collections
import filecmp
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

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

def ValidateImageName(image_name):
    if "?" in image_name:
        return False
    else:
        return True


# image path is provided
def get_exif(img_path):
    ret = {}
    try:
        with Image.open(img_path) as iv:
            info = iv._getexif()
            if not info: 
                print("Cannot read exif info of: {}".format(img_path))
            else:
                for tag, value in info.items():
                    decoded = TAGS.get(tag, value)
                    ret[decoded] = value
        return ret, iv
    
    except Exception as ex:
        print("Image {} does not have any exif".format(img_path))
        return  None, None # None

def listAllImages(root):

    image_count = 0
    video_count = 0
    cameras = []
    exif_count = 0
    non_exif_count = 0
    modified_count = 0
    images_dict = {}    # image path key, datetime value
    
    for root_folder, folders, files in os.walk(root):
        
        for f in files:
            
            if not ValidateImageName(f):   #f = lambda s: True if not "?" in s else False
                print("Name {} is not valid".format(f))
                continue
            
            file_path = os.path.join(root_folder, f)   # f is file name, e.g., AM234.jpg
            ext = os.path.splitext(file_path)[1].lower()

            if ext in [".nef", ".db", ".psd", ".modd", ".moff", ".thm", ".py", ".lnk"] or ext in [".avi", ".mov", ".mpeg", ".mpg", ".mp4"]:
                #consider only images for now - videos later   
                continue
            
            # check whether it's an image
            try:
                
                exif, im = get_exif(file_path)

                if exif:

                    camera = camera_dict[exif['Make']]    
                    #camera_model = camera_dict[exif['Model']]  # e.g., Nikon D60
                    # u'Apple', u'EASTMAN KODAK COMPANY', u'NIKON CORPORATION', u'Nokia', u'PENTAX', u'SONY', u'Panasonic', u'Canon', u'LGE'
                    if not camera in cameras:
                        cameras.append(camera)

                    # ExifImageWidth, ExifImageHeight  
                    date_time_org = datetime.strptime(exif['DateTimeOriginal'], "%Y:%m:%d %H:%M:%S")
                    date_time_taken = datetime.strptime(exif['DateTime'], "%Y:%m:%d %H:%M:%S")
                    #print("Exif {}".format(type(date_time_taken)))
                    #images_dict[file_path] = date_time_taken
                    if not images_dict.keys():
                        images_dict[modifiedtime] = [file_path]                    
                    if date_time_taken in images_dict.keys:
                        images_dict[date_time_taken].append(file_path)
                    else:
                        images_dict[date_time_taken] = [file_path]                    
                    exif_count += 1
                        
            except Exception as ex:
                
                if ext in [".jpg", ".jpeg", ".png"]:  # these are images without Exif info
                    non_exif_count += 1
                    modifiedtime = datetime.fromtimestamp(os.path.getmtime(file_path))   # returns a DateTime object
                    #print("NOT exif {}".format((type(modifiedtime))))
                    #images_dict[file_path] = modifiedtime
                    if modifiedtime in images_dict.keys():
                        images_dict[modifiedtime].append(file_path)
                    else:
                        images_dict[modifiedtime] = [file_path]
                else:
                    print("NOT AN IMAGE: {}".format(file_path))
                    #print(ex.args[0])

    #x = sorted(images_dict.values()) #(images_dict.items())
    #c = collections.Counter(x)
    #mc = c.most_common()
    #for m in mc:
        #if m[1] > 1:
            #print(m[1])
        
    # New way dictionary - datetime as key of the dict
    #for item in images_dict.items():   # prints both key and vals
    f = open(os.path.join(os.getcwd(), "dups.txt"), "w")
    dups = 0
    for k, vals in images_dict.items():
        #print(vals)
        if len(vals) > 1:   # 2, 3, 4, 5 ...
            dups += len(vals) - 1
            for i, val in enumerate(vals):
                if i == 0: continue
                try:
                    im = Image.open(val)
                    fname = os.path.basename(val)
                    name1 = fname.split(".")[0]
                    ext = fname.split(".")[1]
                    new_fname = name1 + "_{}.".format(i) + ext
                    #im.save(r"C:\temp\imagetest\{}_{}.{}".format(name1, i, ext), "JPEG")
                    #print(os.path.join(r"C:\temp\imagetest", new_fname))
                    f.write(val + "\n")
                    im.save(os.path.join(r"C:\temp\imagetest", new_fname))
                except:
                    pass
    f.close()
    
    #print("************************************************************")
    #ordered_dict = collections.OrderedDict(sorted(images_dict.items()))
    #for k, v in ordered_dict.items():
        #print("{} : {}".format(k, v))


        
    """
    >>> x
    [5, 2, 1, 2, 9, 7, 2, 5, 8, 6, 3, 5]
    >>> v = collections.Counter(x)
    >>> v
    Counter({2: 3, 5: 3, 1: 1, 3: 1, 6: 1, 7: 1, 8: 1, 9: 1})
    """  
##    for k, v in images_dict.items():
##        print("{} : {}".format(k, v))
##    print(cameras)
##    print(exif_count)
##    print(non_exif_count)
##    print(modified_count)
                    
    
    
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

    onedrive_fuji = r"C:\Users\farnf\OneDrive\Pictures\FromFujiCamera"
    root = r"C:\temp"
    twok_07 = r"C:\Users\farnf\Pictures\2016-06"
    root = r"D:\DCIM\101_FUJI"
    root = r"C:\Users\nobi4775\Pictures\NikonD60_2"
    root = r"C:\Users\nobi4775\Pictures"
    root = r"C:\Users\farnf\Pictures"
    root = r"C:\Users\nobi4775\Pictures\NikonD60_2"
    
    #listAllImages(r"C:\Users\farnf\Pictures\2016-06")

    img = Image.open(x)
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    
    for k, v in exif.items():
        print(k, v)
        
    onedrive_fuji = r"C:\Users\farnf\OneDrive\Pictures\FromFujiCamera"
    root = r"C:\Users\nobi4775\Pictures\NikonD60_2"
    root = r"C:\Users\nobi4775\Pictures\MinecraftCake"
    
    listAllImages(root)
    print("one")

