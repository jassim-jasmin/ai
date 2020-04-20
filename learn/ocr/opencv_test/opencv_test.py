import os
import cv2
import numpy as np

def convert(im, main_path, result_path, state, county):
    im = cv2.imread(result_path, 0)
    edges = cv2.Canny(im, 50, 150, apertureSize=3)
    minLineLength = 100
    maxLineGap = 10

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    print(type(lines))
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(edges, (x1, y1), (x2, y2), (0), 5)

    kernel = np.ones((7, 7), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=7)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    idx = 0
    if not os.path.exists(main_path + "/crop"):
        os.makedirs(main_path + "/crop")
    if not os.path.exists(main_path + "/stamp"):
        os.makedirs(main_path + "/stamp")
    path, dirs, files = next(os.walk(main_path + "/crop"))
    file_count = len(files)

    for c in contours:
        if state == 'ID' and county == 'ADA':
            x, y, x2, y2 = cv2.boundingRect(c)
            if (y2 > 150 and y2 < 800) and (x2 > 400 and x2 < 1300):
                idx += 1
                idxc = idx + file_count
                new_img = im[y:y + y2, x:x + x2]
                cv2.imwrite(main_path + "/crop/" + str(idxc) + '.tif', new_img)
        else:
            x, y, x2, y2 = cv2.boundingRect(c)
            if (y2 > 200 and y2 < 1000) and (x2 > 400 and x2 < 1300):
                idx += 1
                idxc = idx + file_count
                new_img = im[y:y + y2, x:x + x2]
                cv2.imwrite(main_path + "/crop/" + str(idxc) + '.tif', new_img)

def get_canny_edges(image):
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)

    for line in lines:
        for x1, y1, x2, y2 in line:
            # print(x1, y1, x2, y2)

            cv2.line(edges, (x1, y1), (x2, y2), (0), 5)

    kernel = np.ones((7, 7), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=7)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        # print("countours", contours)
        x, y, x2, y2 = cv2.boundingRect(c)

        if y2>100:
            print("counto", x, y, x2, y2)
            # print("range", y:y)
            # [1657:1657 + 486, 76:76 + 1455]
            new_img = image[y:y + y2, x:x + x2]

            cv2.imshow(f'{x}, {y}, {x2}, {y2}', new_img)
            cv2.waitKey()

    cv2.imshow('test', edges)
    cv2.waitKey()

# def crop_confidence(image, left, height, word_num, top_width):
#     crop_image = image[left:left+height, word_num:word_num+top_width]
#
#     return crop_image

# def crop_confidence(image, wdth, height, left, top):
def crop_confidence(image, left,  top, width, height):
    crop_image = image[width:width + height, left:left + top]

    return crop_image

def get_cv_image(image_path):
    return cv2.imread(image_path)

image_path = "C:\\Users\\MOHAMMED JASIM\\Documents\\mj\\dataset\\805893.tif"

tif = cv2.imread(image_path)

# get_canny_edges(tif)

# [1657:1657 + 486, 76:76 + 1455]
# 536	158	59	21
t = tif[536:1000:, 158:500]
t = tif[158:158+21:, 536:536+59]
# cv2.imshow('test_', t)
# cv2.waitKey()