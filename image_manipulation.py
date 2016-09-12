import os
import sys
import filecmp
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from PIL import ImageEnhance


def image_difference(im1, im2):
    out = abs(image1, image2)  # returns an image ...
    return out

print("stop")

def saveImageAsGrayscale(image):
    image.save("L")
        
#try:
    ##filename, ext = os.path.splitext(imfile1)
    ##new_file = filename + "_mini" + '.JPEG'
    ##size = (128, 128)
    #im1= Image.open(imfile1)
    ##im1.thumbnail(size, Image.ANTIALIAS)
    ##im.save(new_file, 'JPEG')
    
    ##filename, ext = os.path.splitext(imfile2)
    ##new_file = filename + "_mini" + '.JPEG'
    #im2= Image.open(imfile2)
    ##im2.thumbnail(size, Image.ANTIALIAS)

    ##d = ImageChops.difference(im1, im2)
    ##if d.getbbox() is None:
        ##print("No difference")
    ##else:
        ##d.save(r'C:\temp\thumbdiff.jpg', 'JPEG')

    #print(timeit.timeit(stmt=a, number=100000))
    #print(timeit.timeit(stmt=b, number=100000))
    
#except Exception as ex:
    #print(ex.args[0])
    
if __name__ == '__main__':

    sample_image = os.path.join(os.getcwd(), "rubyct.JPG")
    
    try:
        image = Image.open(sample_image)
        enhancer = ImageEnhance.Contrast(image)
        enhancer = ImageEnhance.Color(image)
        im = enhancer.enhance(0.5)
        enhancer.save("L")
    except:
        print("Not an image")