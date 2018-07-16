import os
import filecmp

root1 = r'F:\MyPython\CompareOrganizeImage'
root2 = r'C:\MyPython\CompareOrganizeImage'

"""
#You need to call os.path.realpath on __file__, 
#so that when __file__ is a filename without the path you still get the dir path
"""

root_drive = os.path.dirname(os.path.realpath(__file__))

# this is very simple approach
dir_cmp = filecmp.dircmp(root1, root2)

lefts = dir_cmp.left_only
rights = dir_cmp.right_only

for dirs1, folders1, files1 in os.walk(root1):
    
    for dirs2, folders2, files2 in os.walk(root2):
        
        for file1 in files1:
            
            f1 = os.path.join(root1, file1)
            if not os.path.exists(f1): continue
            
            for file2 in files2:
                
                f2 = os.path.join(root2, file2)
                if not os.path.exists(f2): continue
                
                if file1 == file2:  # files have same name

                    # ignore *.db files
                    if file1 == 'Thumbs.db' and file2 == 'Thumbs.db': 
                        continue
                    else:   
                        flag = filecmp.cmp(f1, f2)
                        if not flag:
                            print("{}\n{}".format(f1, f2))
                else:
                    pass

print('done')
