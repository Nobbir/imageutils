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
    #image_name = "rubyct.JPG"
    file_path, file_name = os.path.split(image_path)
    filename, ext = os.path.splitext(file_name)
    thumbnail_name = file_name + "_mini" + ext
    #size = (128, 128)
    try:
        im1= Image.open(image_path)
        im1.thumbnail(size, Image.ANTIALIAS)
        im1.save(thumbnail_name, 'JPEG')
    except Exception as ex:
        print(ex.args[0])

def ImageEnhancerExample1(image):
    
    enhancer = ImageEnhance.Contrast(image)
    enhancer = ImageEnhance.Color(image)
    im = enhancer.enhance(0.5)
    enhancer.save("L")

def saveImageAsGrayscale(image):
    image.save("L")
        
    try:
    
        d = ImageChops.difference(im1, im2)
        if d.getbbox() is None:
            print("No difference")
        else:
            d.save(r'C:\temp\thumbdiff.jpg', 'JPEG')
    
        #print(timeit.timeit(stmt=a, number=100000))
        #print(timeit.timeit(stmt=b, number=100000))
        
    except Exception as ex:
        print(ex.args[0])
    
if __name__ == '__main__':

    image_path = os.path.join(os.getcwd(), "rubyct.JPG")

    #try:
        #with Image.open(image_path) as im:
            #print("{}, {}, {}, {}".format(image_path, im.format, im.size, im.mode))
    #except:
        #print("...................")

    ##im1= Image.open(image_path)
    ##im1.thumbnail(size, Image.ANTIALIAS)
    ##im1.save(thumbnail_name, 'JPEG')
    try:
        with Image.open(image_path) as image:
            #print(image.info())
            #image_copy = image.copy()
            image.thumbnail((10, 15), Image.ANTIALIAS)
            image.save("thumbnail1.jpg", "JPEG")
    except:
        print("Not an image")