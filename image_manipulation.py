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

#def SaveImageAsThumnail(image, size=(128, 128)):
def SaveImageAsThumnail(image_path, size=(128, 128)):

    try:       
        file_path, file_name = os.path.split(image_path)
        filename, ext = os.path.splitext(file_name)
        thumbnail_name = filename + "_mini" + ext        

        with Image.open(image_path) as image:
            image.thumbnail(size, Image.ANTIALIAS)
            image.save(thumbnail_name, 'JPEG')
    except Exception as ex:
        print(ex.args[0])

def ImageEnhancerExample1(image):
    
    enhancer = ImageEnhance.Contrast(image)
    enhancer = ImageEnhance.Color(image)
    im = enhancer.enhance(0.5)
    #enhancer.save("L")   # save() called in a wrong way

def saveImageAsGrayscale(image_path):
    
    try:
        with Image.open(image_path) as image:
            im = image.convert("L")
            im.save("grayscale_im.jpg", "JPEG")
    except Exception as ex:
        print(ex.args[0])
        return None
        
        
def ImageChops():
    
    try:
        d = ImageChops.difference(im1, im2)
        if d.getbbox() is None:
            print("No difference")
        else:
            d.save(r'C:\temp\thumbdiff.jpg', 'JPEG')
        
    except Exception as ex:
        print(ex.args[0])

def ImageResize(image_path):

    image_path = "rubyct.JPG"
    
    try:
        with Image.open(image_path) as image:
            im2 = image.copy()
            #im2.convert("L").save("grayscale2.jpg")
            width, height = im2.size
            small = im2.resize((width/100, height/100))
            small.save("small.jpg")
            
    except Exception as ex:
        print(ex.args[0])
    
#############################################################
## timeit.timeit example
#print(timeit.timeit(stmt=a, number=100000))
#print(timeit.timeit(stmt=b, number=100000))
#def test():
    #"""Stupid test function"""
    #L = []
    #for i in range(100):
        #L.append(i)

#if __name__ == '__main__':
    #import timeit
    #print(timeit.timeit("test()", setup="from __main__ import test"))
#############################################################
    
if __name__ == '__main__':

    image_path = os.path.join(os.getcwd(), "rubyct.JPG")

    #SaveImageAsThumnail(image_path)
    
    #saveImageAsGrayscale(image_path)
    ImageResize(image_path)
