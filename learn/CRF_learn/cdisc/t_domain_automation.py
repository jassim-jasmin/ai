# from learn.CRF_learn.prediction_dir.prediction_main import crf_prediction
from learn.CRF_learn.prediction_dir.prediction_main import crf_prediction
from learn.CRF_learn.cdisc.ta_domain.arm import generate_arm

def get_protocol_data():
    # fp = open("learn\ocr\\data\\convert_data.txt", "r")
    # fp = open("C:\\Users\MOHAMMED JASIM\\PycharmProjects\\ai\\dataset\\p92.txt", "r", encoding="utf8")
    fp = open("C:\\Users\\MOHAMMED JASIM\\PycharmProjects\\ai\\dataset\\p27.txt", "r", encoding="utf8")
    data = fp.read()
    fp.close()

    return data

def get_prediction_result(model_name, data):
    data = data.replace('\n', ' ')
    prediction_data, final_result = crf_prediction(model_name, data)

    return final_result

def main(model_name):
    armcd = 'A-B-C-D-E'
    armcd = 'A'
    data = get_protocol_data()
    prdiction_data = get_prediction_result(model_name, data)
    variables = generate_arm(prdiction_data, armcd)

    return variables

# main()