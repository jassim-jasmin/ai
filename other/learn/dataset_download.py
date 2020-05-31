import tensorflow as tf

dataset = tf.keras.utils.get_file(
      fname="who_covid_19_sit_rep_time_series.csv",
      origin="https://github.com/CSSEGISandData/COVID-19/blob/master/who_covid_19_situation_reports/who_covid_19_sit_rep_time_series/who_covid_19_sit_rep_time_series.csv",
      extract=False, cache_dir="dataset")

print(dataset)