import tabula
import pandas as pd

from learn.CRF_learn.cdisc.tv_domain.nalaxone.generate_variables import find_variables

def convert_table_to_datafram(pdf_path, page_number):
    try:
        df = tabula.read_pdf(pdf_path, pages=page_number)[0]

        return df

    except Exception as e:
        print("error in convert_table_to_dataframe", e)

        return pd.DataFrame

def nalaxone_specific(data):
    step_1 = data[0]
    nalaxone_flag = True
    final_data = {}

    for each_element in step_1:
        if 'nan' == each_element:
            nalaxone_flag = False
            break

    if nalaxone_flag:
        print("nalaxone specific stage 1 match")
        final_data = find_variables(step_1)

    return final_data

def generate_variables(data):
    """
    specific rules need to add here
    """
    final_result_array = []
    matrix = data.values

    final_result_array.append({"nalaxone": nalaxone_specific(matrix)})


    return final_result_array

def predict_variables(pdf_path, page_number):
    """
    tv values contains 0 means there is a chance like error, need to verify that.
    """
    print("tv domain", pdf_path, page_number)
    df = convert_table_to_datafram(pdf_path, page_number)
    final_result = generate_variables(df) # :todo: check for multiple key, then need to sortout, here written only for nalaxone

    return {"tv": final_result}
