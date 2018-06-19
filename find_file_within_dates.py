import cv2

#from skimage.measure import structural_similarity as ssim
from skimage import measure




# END OPENCV2
#
import filecmp
import os #.path,
import time
#from dateutil import parser
from datetime import datetime
import pytz
from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
from PIL import ImageChops
from PIL import Image
from PIL import ImageStat

'''
>>> from datetime import datetime
>>> past = datetime.now()
>>> present = datetime.now()
>>> past < present
True
>>> datetime(3000, 1, 1) < present
False
>>> present - datetime(2000, 4, 4)
datetime.timedelta(4242, 75703, 762105)
'''
"""
datetime.fromtimestamp(ts) converts "seconds since the epoch" to a naive datetime object
that represents local time. tzinfo is always None in this case.
"""

f1 = r"C:\Interests\ImagePhotoshop\pohela.jpg"

##d = datetime.fromtimestamp(os.path.getctime(f1))
##print(d.year)
##print(d.month)
##print(d.day)
##print(d.hour)
##print(d.minute)
##print(d.second)


#class ImageObject():
    
    ##self.file_hash = None
    ##self.im_name = None
    
    #def __init__(self):
        #print("Yes")

#x = ImageObject()

# timeperiod1, timeperiod2, file1
# 
def findWithinTimePeriods(file1):

    ##    # range of time to look for
    ##    start = datetime(2014, 4, 4, 0, 1, 11) #, tzinfo=pacific)  # type = datetime.datetime
    ##    end = datetime(2014, 4, 24, 0, 1, 11) #, tzinfo=pacific)  # type = datetime.datetime
    year = 2014
    month = 4
    startday = 4
    endday = 24
        
    try:
        # modified time is EARLIER
        pacific = pytz.timezone('US/Pacific')
        
        #createdtime = datetime.fromtimestamp(os.path.getctime(file1)) #, pacific)    # type = datetime.datetime
        modifiedtime = datetime.fromtimestamp(os.path.getmtime(file1)) #, pacific)  # type = datetime.datetime
    
        #print(modifiedtime)
        if modifiedtime.year < 2015 and modifiedtime.year > 2013:
            if modifiedtime.month < 4: #< 6 and modified.month > 2:
                print(os.path.split(file1)[1])
                
    except Exception as ex:
        print(ex.args[0])



from PIL import ImageChops
import math
import operator
from functools import reduce


def getImageSimilarity(img1, img2):
    bbox = ImageChops.difference(img1, img2).getbbox()
    print(bbox[2])

def getRMSdiff(img1, img2):
    
    h = ImageChops.difference(img1, img2).histogram()
    
    rms = math.sqrt(reduce(operator.add,
                           map(lambda h, i:h*(i**2), h, range(256))
                           ) / (float(img1.size[0]) * img1.size[1]))
    return rms
    
location = r"C:\Users\nobi4775\Pictures"
location = r'C:\Users\nobi4775\Documents\GitHub\AllImageScripts\CompareOrganizeImage1\Mobile Phones\GooglePhonePictures\Feb2013_Feb2014\duplidate_test'

def create_img_array():
    
    img_list = []
    
    for root, folders, files in os.walk(location):
        
        for infile in files:
            
            file_name = infile.split(".")[0]
            
            f = os.path.join(root, infile)
            try:
                im = Image.open(f)
                img_list.append((file_name, im))
            except:
                pass
            
    return img_list

img_arr_1 = create_img_array()
img_arr_2 = create_img_array()

for i, img in enumerate(img_arr_1):
    
    rms = None
    
    remainders = img_arr_1[i+1:]
    
    # now compare img with the rest of the images
    for rm in remainders:
        
        #getImageSimilarity(img, rm)
        ## compare img and rm
        #if getImageSimilarity(img, rm) is None:
            #print("Nothing .................")
        #else:
            #print("Something ............")
        rms = getRMSdiff(img[1], rm[1])
        print("{}\t:{}\t{}".format(rms, img[0], rm[0]))
    #print("{}\t{}".format(i, img))
    
#i = WORKING WORKING WORKING ....
#for root, folders, files in os.walk(location):

    #for infile in files:
        
        #size = 128, 128  # shouldn't be of same proportion????
        
        #try:
            #f = os.path.join(root, infile)
            #file, ext = os.path.splitext(infile)
            #im = Image.open(f)  # this line verifies the file is an image file.
            #gray_im = im.convert("L")
            #gray_im.thumbnail(size)
            ##gray_im.show()
            #gray_im.save(os.path.join(root, "thumbnails", file) + ".png", "JPEG")
            ##findWithinTimePeriods(f)
            
        #except Exception as ex:
            #print("{} is not an image")
            #print(ex.args[0])






if __name__ == "__main__":
    pass
