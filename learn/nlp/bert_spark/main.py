import os
os.environ["JAVA_HOME"] = "C:\\Program Files\\Java\\jdk1.8.0_141"
os.environ["PATH"] = os.environ["JAVA_HOME"] + os.environ["PATH"]

from pyspark.sql import SparkSession
from pyspark.ml import Pipeline

import sparknlp
from sparknlp.annotator import *
from sparknlp.common import *
from sparknlp.base import *

spark = sparknlp.start()
# spark = sparknlp.start(gpu=True)

# print("Spark NLP version: ", sparknlp.version())
# print("Apache Spark version: ", spark.version)