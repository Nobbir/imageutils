import cv2



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


class ImageObject():
    
    #self.file_hash = None
    #self.im_name = None
    
    def __init__(self):
        print("Yes")

x = ImageObject()

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


location = r"C:\Users\nobi4775\Pictures"
location = r'C:\Users\nobi4775\Documents\GitHub\AllImageScripts\CompareOrganizeImage1\Mobile Phones\GooglePhonePictures\Feb2013_Feb2014'

i = 0
for root, folders, files in os.walk(location):

    for file in files:
        
        try:
            f = os.path.join(root, file)
            im = Image.open(f)  # this line verifies the file is an image file.
            findWithinTimePeriods(f)
            
        except Exception as ex:
            print("{} is not an image")
            print(ex.args[0])



##
##def findWithinTimePeriods(file1):
##
##    # modified time is EARLIER
##    pacific = pytz.timezone('US/Pacific')
##
##    # range of time to look for
##    start = datetime(2014, 4, 4, 0, 1, 11) #, tzinfo=pacific)  # type = datetime.datetime
##    end = datetime(2014, 4, 24, 0, 1, 11) #, tzinfo=pacific)  # type = datetime.datetime    
##
##    modifiedtime = datetime.fromtimestamp(os.path.getmtime(file1)) #, pacific)  # type = datetime.datetime
##    if modifiedtime < start or modifiedtime > end:
##        print("Not within range!")
##        return
##
##    if modifiedtime > start and modifiedtime < end:
##        print(modifiedtime)
##        print("Got it!")
##    else:
##        print(start)
##        print(modifiedtime)
##        print(end)
##        print("out of bound")
##
##        
##x = findWithinTimePeriods(r"C:\Interests\ImagePhotoshop\pohela.jpg")
    
##file = r"C:\messages.xml"
##
##
##
### range of time to look for
##apr04 = datetime(2015, 4, 4, 0, 0, 0)  # type = datetime.datetime
##apr24 = datetime(2015, 4, 24, 0, 0, 0)  # type = datetime.datetime
##print(apr24 - apr04)
##print(apr24 > apr04)
##
####diff = apr04 - apr24 # type = datetime.timedelta
### diff - timedelta
##
##createtime = os.path.getctime(file)  # type = 'float'
##modifiedtime = os.path.getmtime(file)  # type = 'float'
##
##datetime.fromtimestamp(createtime)  # type = datetime.datetime created from float
##datetime.fromtimestamp(modifiedtime)     # type = datetime.datetime created from float
##
##
####create1 = time.ctime(os.path.getctime(file))  # type = 'str'
####print(datetime.fromtimestamp(create0))  # passing 'float' succeeds
####print(datetime.fromtimestamp(create1))  # passing 'str' causes failure
##
######d = datetime(time.ctime(os.path.getctime(file)))
######print(type(d))
####
####created = time.ctime(os.path.getctime(file))
####
####print(created > later)
####
######+t1	Returns a timedelta object with the same value. (2)
######-t1	equivalent to timedelta(-t1.days, -t1.seconds, -t1.microseconds), and to t1* -1. (1)(4)
####
####print(type(os.path.getctime(file)))  # this returns a float!!!
####print(os.path.getctime(file))  # returns float
####print(os.path.getmtime(file))  # returns float
####
##### returns: created: Wed Oct 21 14:02:30 2015
####created = time.ctime(os.path.getctime(file))
####
##### returns: last modified: Fri Mar  4 09:46:28 2016
####modified = time.ctime(os.path.getmtime(file))
####
####print(type(os.path.getmtime(file)))
####print(created > modified)
####
####print(type(datetime.now()))
####now = datetime.now()
####print(now > modified)
####
####### returns datetime.datetime object - use +, -, >, < operators on it
######print(type(parser.parse(time.ctime(os.path.getctime(file)))))
##

if __name__ == "__main__":
    pass
