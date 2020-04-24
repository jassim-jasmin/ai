import csv
import pymysql as MySQLdb

db = MySQLdb.connect("192.168.15.43", "root", "softinc", "training_data")
cursor = db.cursor()
# nlp = spacy.load('en_core_web_sm')
TRAIN_DATA1 = []


sql = "SELECT data,start,end,label FROM training_data.deed_document;"

cursor.execute(sql)

data = cursor.fetchall()
filePath = "dataset\\d1_unorder.csv"
# Create the csv file

import pandas as pd

with open(filePath, 'w', newline='') as f_handle:
    writer = csv.writer(f_handle,)
    # Add the header/column names
    header = ['data', 'start', 'end', 'label']
    header = ['data', 'word', 'label']
    writer.writerow(header)
    # Iterate over `data`  and  write to the csv file
    try:
        insert_row = []
        data_value = []
        insert = []
        for row, row1, row2, lable in data:
            insert_row = []
            insert_row.append(row)
            left = int(row1)
            right = int(row2)
            insert_row.append(row[left:right])
            insert_row.append(lable)

            writer.writerow(insert_row)
        # pd.DataFrame({'data':insert_row[0], 'word':insert_row[1], 'label':insert_row[2]})
    except Exception as e:
        print('error :', e)
        print(row)
        cursor.close()
db.close()