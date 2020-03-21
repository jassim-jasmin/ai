from matplotlib import pyplot
from pandas import read_csv
import pandas as pd
path = r"C:\Users\MOHAMMED JASIM\Documents\mj\COVID-19-master\who_covid_19_situation_reports\who_covid_19_sit_rep_time_series\who_covid_19_sit_rep_time_series.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path)
data.hist()
pyplot.show()