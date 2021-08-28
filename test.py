import cv2
import os
for (root, dirs, files) in os.walk('imgs', topdown=True):
    print(root)
    print(dirs)
    print(files)
    for fileName in files:
        img = cv2.imread(root+"/"+fileName)
        cv2.imshow("myPic", img)
        cv2.waitKey(0)
