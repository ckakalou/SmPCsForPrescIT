# Created by Christine Kakalou on 4/1/2023
# Project: SmPCs for PrescIT
#

# Python program to check whether
# the directory empty or not


import os

# path of the directory
path = r"Data\SmPCs\EMA_ExtractedFiles"

emptyDirCount = 0
nonEmptyDirCount = 0

for dirpath, dirnames, files in os.walk(path):
    if files:
        nonEmptyDirCount += 1
        print("Directory {0} has files in it".format(dirpath))
        print("Files are : {0}".format(files))
    else:
        emptyDirCount += 1
        print("Directory {0} is empty".format(dirpath))

print(emptyDirCount)
print(nonEmptyDirCount)