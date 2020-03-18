import cv2
import json
from PIL import Image
import numpy as np
import numpy.matlib


path = json.loads(open('pathDirectory.json','r').read())['ubuntu']

im = cv2.imread(path['testImagePath3'],0)

minLineLength = 100
maxLineGap = 50
edges = cv2.Canny(im,50,100,apertureSize = 3)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

kernel = np.ones((7,7),np.uint8)
edges = cv2.dilate(edges,kernel,iterations = 7)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(type(hierarchy),'hierarchy')
# cv2.imshow('image ', hierarchy)
cv2.imwrite(path['testEdgeImageDirectory']+'/edge2.tif',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(im.shape)

shy, shx = im.shape
xMinLimit = shx/4
xMaxLimit = shx - shx/2
print(xMinLimit, xMaxLimit)

for c in contours:
    x, y, x2, y2 = cv2.boundingRect(c)
    if y2 > 50 and y2 < 800 and x2 > 400 and x2 < 1300 :
        new_img = im[y:y + y2, x:x + x2]
        # cv2.imwrite(path['contoursLinedImage'], new_img)
        cv2.imshow('image '+str(y) + ' ' + str(y2) + ' ' + str(x) + ' ' + str(x2), new_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(new_img.shape)
        # inv = np.linalg.inv(new_img)
        # cv2.imshow('inverse', inv)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # print(inv)
# cv2.imwrite(path['edgeImagePath'], edges)

# if im is not None:
    # print(im, type(im))
    # im.shape = (2549,3321)
    # im = im.reshape(3321,2549)
    # edges = cv2.Canny(im,50,150,apertureSize = 3)
    # minLineLength = 10
    # maxLineGap = 10
    # lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    # print(lines)
    # print(test, type(test))
    # cv2.imshow('image', edges)
    # cv2.waitKey(2000)
    # cv2.destroyAllWindows()
# else:
#     print("path error")