from matplotlib import pyplot
from pandas import read_csv
path = r"C:\Users\MOHAMMED JASIM\Documents\mj\COVID-19-master\who_covid_19_situation_reports\who_covid_19_sit_rep_time_series\who_covid_19_sit_rep_time_series.csv"
names = ['Province/States', 'Country/Region', 'WHO region','1/21/2020', '3/4/2020']
data = read_csv(path    )
data.plot(kind = 'box', subplots = True, sharex = False,sharey = False)
pyplot.show()