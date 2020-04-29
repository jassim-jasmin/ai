import tabula

pdf_path = "C:\\Users\\MOHAMMED JASIM\\Documents\\mj\\project\\cdisk\\nalaxone\\p1.pdf"
df = tabula.read_pdf(pdf_path, pages="16")

print(df[0])