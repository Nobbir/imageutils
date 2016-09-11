import os
import filecmp

#You need to call os.path.realpath on __file__, 
#so that when __file__ is a filename without the path you still get the dir path
root_drive = os.path.dirname(os.path.realpath(__file__))

root1 = r'C:\MyPython\CompareOrganizeImage1'
root2 = r'C:\MyPython\CompareOrganizeImage2'

print(root_drive)
                    
dir_cmp = filecmp.dircmp(root1, root2)

lefts = dir_cmp.left_only
rights = dir_cmp.right_only

print('done')
