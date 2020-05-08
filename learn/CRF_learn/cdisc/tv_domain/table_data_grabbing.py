import tabula
import pandas as pd

def convert_table_to_datafram(pdf_path, page_number):
    try:
        df = tabula.read_pdf(pdf_path, pages=page_number)[0]

        return df

    except Exception as e:
        print("error in convert_table_to_dataframe", e)

        return pd.DataFrame

def table_dataframe_reformatting(dataframe):
    columns = dataframe.columns
    print(columns)

def match_headers(data_frame):
    pass

def predict_variables(pdf_path, page_number):
    print("tv domain", pdf_path, page_number)
    dataframe = convert_table_to_datafram(pdf_path, page_number)
    table_dataframe_reformatting(dataframe)
