import filecmp

from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
from PIL import ImageChops
from PIL import Image
from PIL import ImageStat
import hashlib


# http://blog.iconfinder.com/detecting-duplicate-images-using-python/
pic1 = r"C:\Users\nobi4775\Pictures\GooglePhonePicturesDhaka\IMG_20130331_005901.jpg"
pic2 = r"C:\Users\nobi4775\Pictures\GooglePhonePicturesDhaka\IMG_20130331_005906.jpg"
pic3 = r"C:\Users\nobi4775\Pictures\GooglePhonePicturesDhaka\IMG_20130331_005901.jpg"
pic4 = r"C:\Users\nobi4775\Pictures\GooglePhonePicturesDhaka\IMG_20130331_005901Copy.jpg"   # 5-6 pixel is different

###
## hash table - Image cataloging ....
### 

# original image's hash value
image_file = open(pic1).read()
hash1 = hashlib.md5(image_file).hexdigest()

# modified image's hash value
image_file_modified = open(pic2).read()
hash2 = hashlib.md5(image_file_modified).hexdigest()

image_file = open(pic3).read()
hash3 = hashlib.md5(image_file).hexdigest()

image_file = open(pic4).read()
hash4 = hashlib.md5(image_file).hexdigest()

print(hash1 == hash4)
print(hash1)
print(hash3)