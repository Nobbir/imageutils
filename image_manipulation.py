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
    try:
        with Image.open(image_path) as image:
            im2 = image.copy()
            #im2.convert("L").save("grayscale2.jpg")
            width, height = im2.size
            small = im2.resize((width/100, height/100))
            small.save("small.jpg")
            
    except Exception as ex:
        print(ex.args[0])
        
        
def ImageResizeCentered(image_path):
    try:
        with Image.open(image_path) as image:
            im2 = image.copy()
            width, height = im2.size
            im3 = im2.convert("L") #.save("grayscale2.jpg")
            
            im3.thumbnail((256, 256))
            im3.save("thumbnail_gray2.jpg", 'JPEG')
            
            #centerx = width / 2
            #centery = height / 2
            
            #diff = 256
            #ulx = centerx - diff
            #uly = centery - diff
            #lrx = centerx + diff
            #lry = centery + diff
            
            ## pass an extent x0, y0, x1, y1 to Image.crop method
            #centered = im3.crop((ulx, uly, lrx, lry))
            #centered.save("centered2.jpg")
            
    except Exception as ex:
        print(ex.args[0])
        
    
def ResizeExperiments(image_path, size=(128, 128)):
    try:       
        file_path, file_name = os.path.split(image_path)
        filename, ext = os.path.splitext(file_name)
        thumbnail_name = filename + "_{}".format(size[0]) + ext        

        with Image.open(image_path) as image:
            image.thumbnail(size)
            image.save(thumbnail_name, 'JPEG')
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
    #ResizeExperiments(image_path, (100, 100))
    #saveImageAsGrayscale(image_path)
    ImageResizeCentered(image_path)
