import os
import filecmp

root = os.getcwd()

base_files = []

def compareImages(test_files):
    
    for file1 in base_files:
        for file2 in test_files:
            if filecmp.cmp(file1, file2, 0):
                print(file1)
                break
i = 0
for dirs, folders, files in os.walk(root):
    #print(dirs)
    if folder in dirs.split(os.sep):
        test_files = [os.path.join(dirs, f) for f in files]
        if i == 0:
            base_files = test_files[:]
        else: # i > 0
            compareImages(test_files)
        i += 1

