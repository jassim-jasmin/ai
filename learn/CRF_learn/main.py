# # from learn.ocr.tesseract_test import
# from learn.CRF_learn.prediction_dir.prediction_main import crf_prediction
# from learn.CRF_learn.entitty_mapping import arm_attribute
#
# # from learn.CRF_learn.learn_1 import text
#
# def protocol(prdiction):
#     arm_attribute(prdiction)
#
#
# # fp = open("learn\ocr\\data\\convert_data.txt", "r")
# # fp = open("C:\\Users\MOHAMMED JASIM\\PycharmProjects\\ai\\dataset\\p92.txt", "r", encoding="utf8")
# fp = open("C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\\dataset\\p27.txt", "r", encoding="utf8")
#
# data = fp.read()
# fp.close()
#
# data = data.replace('\n', ' ')
#
# model_name = "cdisk_2"
#
# crf_seller, final_result = crf_prediction(model_name, data)
#
# # for a, b in final_result.items():
# #     print(a, b)
# # print(final_result)
#
# protocol(final_result)

from learn.CRF_learn.cdisc.t_domain_automation import main
model_name = "cdisk_2"
main(model_name)