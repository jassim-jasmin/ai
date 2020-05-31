import tabula

pdf_path = "C:\\Users\\MOHAMMED JASIM\\Documents\\mj\\project\\cdisk\\nalaxone\\p1.pdf"
pdf_path_2 = "C:\\Users\\MOHAMMED JASIM\\Documents\\mj\\project\\cdisk\\op0927\\OP0927_GWEP1446 Protocol Final V5.0 05Dec16 Clean signed.pdf"
pdf_path_3 = "C:\\Users\\MOHAMMED JASIM\\Documents\\mj\\project\\cdisk\\op0992\\OP0992.pdf"

# df = tabula.read_pdf(pdf_path, pages="16")[0]
#
# print(df.head())

df2 = tabula.read_pdf(pdf_path_2, pages="61")[0]


print(df2.columns)
print(df2.head())

# df3 = tabula.read_pdf(pdf_path_3, pages="48")[0]
#
# print(df3.head())

# print(df[['Screening', 'Admission/\rBaseline', 'Period\r1', 'Washout', 'Period\r2']])
"""
['N = 30\rsubjects'
    , 'Screening'
    , 'Admission/\rBaseline'
    , 'Period\r1',
       'Washout'
    , 'Period\r2'
    , 'Washout.1'
    , 'Period\r3'
    , 'Washout.2',
       'Period\r4'
    , 'Washout.3'
    , 'Period\r5'
    , 'Dis-\rcharge'
    , 'Follow-\rUp',
       'Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4',
       'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7']
"""