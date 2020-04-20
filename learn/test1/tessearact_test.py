import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
tif = cv2.imread("C:\\Users\\MOHAMMED JASIM\\Documents\\mj\\dataset\\805893.tif", cv2.IMREAD_UNCHANGED)

data = pytesseract.image_to_string(tif)
data_block = pytesseract.image_to_data(tif)

fp = open("ocr.txt", "w")
fp2 = open("ocr_box.csv", "w")

fp.write(data)
fp2.write(data_block)

fp2.close()
fp.close()
print(data)