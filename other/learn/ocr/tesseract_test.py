import pytesseract
import cv2
from os import sep
from pdf2image import convert_from_path

# from learn.ocr.opencv_test.opencv_test import t, get_cv_image, crop_confidence

tesseract_path = "C:\\Program Files\\Tesseract-OCR\\tesseract"
pytesseract.pytesseract.tesseract_cmd = tesseract_path

image_path = "C:\\Users\\MOHAMMED JASIM\\Documents\\mj\\dataset\\805893.tif"

def pdf_to_text(file_path):
    try:
        pdf = convert_from_path(file_path)
        data = ''

        for each_page in pdf:
            data += pytesseract.image_to_string(each_page)
        return data
    except Exception as e:
        print("\nexception", e)


def test():
    print("Begin ocr conversion")

    tif = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    data = pytesseract.image_to_string(tif)
    data_block = pytesseract.image_to_data(tif)

    fp = open(f"data{sep}ocr.txt", "w")
    fp2 = open(f"data{sep}ocr_box.csv", "w")

    fp.write(data)
    fp2.write(data_block)

    fp2.close()
    fp.close()
    print(data)


# def test1():
#     print("begin")
#     image = get_cv_image(image_path)
#     # data_block = pytesseract.image_to_data(t)
#
#     width = 158
#     height = 21
#     left = 536
#     top = 59
#     # 536	158	59	21	96
#     # 1271	144	73	55	0	Boe8
#     left = 1271
#     width = 144
#     top = 73
#     height = 55
#
#     crop_image = crop_confidence(image, left-1,  top+1, width-1, height)
#     cv2.imshow('crop pic', crop_image)
#     cv2.waitKey()
#     data_block = pytesseract.image_to_data(crop_image)
#     print(data_block)

pdf_path = "C:\\Users\\MOHAMMED JASIM\\Documents\mj\\dataset\\p1.pdf"
# pdf_to_text_path = "data\\convert_data.txt"

# pdf_path = "C:\\Users\\MOHAMMED JASIM\\\Documents\\mj\\project\cdisk\\op0992\\OP0992.pdf"
pdf_to_text_path = "data/op0222.txt"

data = pdf_to_text(pdf_path)

if data:
    fp = open(pdf_to_text_path, "w")

    fp.write(data)
    fp.close()
    print(data)
