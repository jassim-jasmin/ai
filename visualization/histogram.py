from matplotlib import pyplot
from pandas import read_csv

def histogram(path):
    path1 = r"C:\Users\MOHAMMED JASIM\Documents\mj\COVID-19-master\who_covid_19_situation_reports\who_covid_19_sit_rep_time_series\who_covid_19_sit_rep_time_series.csv"
    data = read_csv(path)
    data.hist()
    pyplot.show()