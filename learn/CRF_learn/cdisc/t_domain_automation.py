from learn.CRF_learn.prediction_dir.prediction_main import crf_prediction
from learn.CRF_learn.cdisc.ta_domain.arm import generate_arm
from learn.CRF_learn.cdisc.tv_domain.table_data_grabbing import predict_variables

pdf_path_selector = {
    ""
    "nalaxone": "C:\\Users\\MOHAMMED JASIM\\Documents\\mj\\project\\cdisk\\nalaxone\\p1.pdf",
    "op0992": "C:\\Users\\MOHAMMED JASIM\\Documents\\mj\\project\\cdisk\\op0992\\OP0992.pdf",
    "op0927": "C:\\Users\\MOHAMMED JASIM\\Documents\\mj\\project\\cdisk\\op0927\\OP0927_GWEP1446 Protocol Final V5.0 05Dec16 Clean signed.pdf",
    "nalaxone_table_page": "16",
    "op0992_table_page": "48",
    "op0927_table_page": "61",
    "nalaxone_text": "dataset\\nalaxone.txt"
}

def get_protocol_data(protocol_name, text=False):
    if text:
        pdf_path = pdf_path_selector[protocol_name+"_text"]
    else:
        pdf_path = pdf_path_selector[protocol_name]

    fp = open(pdf_path, "r", encoding="utf8")
    data = fp.read()
    fp.close()

    return data

def get_prediction_result(model_name, data):
    data = data.replace('\n', ' ')
    prediction_data, final_result = crf_prediction(model_name, data)

    return final_result

def model_selector(option=None):
    model_name = "nalaxone"

    return model_name

def ta_domain(protocol_data, protocol_name):
    if protocol_name == "nalaxone":
        armcd = 'A-B-C-D-E'

    else:
        armcd = 'A'

    model_name = model_selector('test')
    prdiction_data = get_prediction_result(model_name, protocol_data)
    variables = generate_arm(prdiction_data, armcd)

    if "arm" in variables:
        print("finnal result:", variables["arm"])

    else:
        print("not found")

def tv_domain(protocol_name):
    data = predict_variables(pdf_path_selector[protocol_name], pdf_path_selector[f"{protocol_name}_table_page"])

    return data

def main(protocol_name):
    ta_values = None
    tv_values = None

    data = get_protocol_data(protocol_name, text=True)
    # ta_values = ta_domain(data, protocol_name)
    tv_values = tv_domain(protocol_name)

    # print(variables)

    final_data = {}

    if ta_values:
        final_data["ta_variables"] = ta_values

    elif tv_values:
        final_data["tv_variables"] = tv_values

    print(final_data)

    final_data

main(model_selector())
