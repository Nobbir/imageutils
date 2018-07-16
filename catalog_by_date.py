import filecmp
import os #.path,
import time
from dateutil import parser
from datetime import datetime
import pytz
from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
from PIL import ImageChops
from PIL import Image
from PIL import ImageStat

# parseDateTime method moved to image_utitlities
from image_utilities import *

"""
datetime.fromtimestamp(time_stamp)  -- example return: datetime.datetime(2016, 8, 3, 9, 56, 52, 43531)
os.path.getmtime() and getctime returns a double (timestamp) which can be converted to a datetime object as

exif date time is returned as a string: '2016:08:01 22:12:20' - this is converted to a datetime object with custom code?
"""
# check these 3 time stamps - 
# if the key1 is not in exif then check key2 and so on
# 1: ('DateTimeOriginal', '2016:08:01 22:12:20')
# 2: ('DateTimeDigitized', '2016:08:01 22:12:20')
# 3: ('DateTime', '2016:08:03 09:56:52')

###dt1 = datetime(2016, 1, 19, 9, 12, 45)
###dt2 = datetime(2015, 1, 19, 9, 15, 33)
###dt3 = datetime(2016, 12, 16, 9, 0, 1)
###dt4 = datetime(2010, 7, 6, 22, 12, 19)

###x = sorted([dt1, dt2, dt3, dt4])


    
####################
location = r"C:\Users\nobi4775\Pictures"
f = open("picture_catalog.txt", "w")

all_pics = []
i = 0
for root, folders, files in os.walk(location):
    
    for file1 in files:
        
        try:
            file_path = os.path.join(root, file1)
            im = Image.open(file_path)
 
            # fromtimestamp method requres a 'float' as input
            # os.path.getmtime returns a float - also, getctime returns a float
            modifiedtime = datetime.fromtimestamp(os.path.getmtime(file_path)) 
            
            y, m, d = modifiedtime.year, modifiedtime.month, modifiedtime.day
            
            all_pics.append(file_path)
            f.writelines(file_path + "\n")
            i += 1
            
        except Exception as ex:
            pass

f.write("\n" + str(i) + "\n")
f.close()

path = r"C:\Users\nobi4775\Pictures"
f = 'me_savar_abedin_home2.jpg'


def myLambda(f_name):
    full_path = os.path.join(path, f_name)
    x = os.stat(full_path).st_mtime
    return x
y = myLambda('me_savar_abedin_home2.jpg')

def myLambda2(file_full_path):
    x = os.stat(file_full_path).st_mtime

    
#mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
#pics0 = sorted(os.listdir(path), key=mtime)
#pics = list(pics0)
#pics = list(sorted(os.listdir(path), key=mtime))

###path = r"C:\Users\nobi4775\Pictures"
##mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
#mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
mtime = lambda full_path: os.stat(full_path).st_mtime

pics_chrono = sorted(all_pics, key=mtime)

for pic in pics_chrono:
    print(pic)
