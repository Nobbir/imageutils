import os
import filecmp

from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
import csv
from PIL import ImageChops
from PIL import Image
from PIL import ImageStat

#You need to call os.path.realpath on __file__, 
#so that when __file__ is a filename without the path you still get the dir path
root_drive = os.path.dirname(os.path.realpath(__file__))

print(__file__)
root1 = r'C:\MyPython\CompareOrganizeImage1'
root2 = r'C:\MyPython\CompareOrganizeImage2'

print(root_drive)


#import os

#def fileExists(f1, f2):
    #if os.path.exists(f1):
        #print(f1)
    #if os.path.exists(f2):
        #print(f2)
    
#dict1 = {}
#for dirs1, folders1, files1 in os.walk(root1):
    #for file1 in files1:
        #if not file1 in dict1.keys():
            #dict1[file1] = os.path.join(root1, file1)
    
#dict2 = {}
#for dirs2, folders2, files2 in os.walk(root2):
    #for file2 in files2:
        #if not file2 in dict2.keys():
            #dict2[file2] = os.path.join(root2, file2)
            
#exts = [".jpg", ".jpeg", ".png"]
#for file1, f1 in dict1.items():
    
    #if file1 in dict2.keys():
        #comp = filecmp.cmp(f1, dict2[file1])
        ##if os.path.splitext(f1)[1].lower() in exts:
            ###print(f1)
            ###print(dict2[file1])
            ##del dict2[file1]
        #if comp:
            #print(file1)
            #print(dict2[file1])
    #else:
        #print("UNMATCHED: {}".format(file1))
        ##print(file2)
            
        ##for file1 in files1:
            
            ##f1 = os.path.join(root1, file1)
            ##if not os.path.exists(f1): continue
            
            ##for file2 in files2:
                
                ##f2 = os.path.join(root2, file2)
                ##if not os.path.exists(f2): continue
                
                ##if file1 == file2:  # files have same name
                    
                    ##if file1 == 'Thumbs.db' and file2 == 'Thumbs.db': 
                        ##continue
                    ##else:   
                        ##flag = filecmp.cmp(f1, f2)
                        ##if not flag:
                            ##print("{}\n{}".format(f1, f2))
                ##else:
                    ##pass
                    
dir_cmp = filecmp.dircmp(root1, root2)

lefts = dir_cmp.left_only
rights = dir_cmp.right_only

print('done')
