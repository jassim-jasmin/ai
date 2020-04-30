import json
import os
# from pyspark.ml import Pipeline
from sparknlp.base import *
from sparknlp.annotator import *
import sparknlp
import mysql.connector
spark = sparknlp.start()


def get_ann_pipeline():
    document_assembler = DocumentAssembler() \
        .setInputCol("text") \
        .setOutputCol('document')

    sentence = SentenceDetector() \
        .setInputCols(['document']) \
        .setOutputCol('sentence') \
        .setCustomBounds(['\n'])

    tokenizer = Tokenizer() \
        .setInputCols(["sentence"]) \
        .setOutputCol("token")

    pos = PerceptronModel.pretrained() \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("pos")

    embeddings = WordEmbeddingsModel.pretrained() \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("embeddings")

    ner_model = NerDLModel.pretrained() \
        .setInputCols(["sentence", "token", "embeddings"]) \
        .setOutputCol("ner")

    ner_converter = NerConverter() \
        .setInputCols(["sentence", "token", "ner"]) \
        .setOutputCol("ner_chunk")

    ner_pipeline = Pipeline(
        stages=[
            document_assembler,
            sentence,
            tokenizer,
            pos,
            embeddings,
            ner_model,
            ner_converter
        ]
    )

    empty_data = spark.createDataFrame([[""]]).toDF("text")

    ner_pipelineFit = ner_pipeline.fit(empty_data)

    ner_lp_pipeline = LightPipeline(ner_pipelineFit)

    print("Spark NLP NER lightpipeline is created")

    return ner_lp_pipeline


def demo():
    conll_pipeline = get_ann_pipeline()

    parsed = conll_pipeline.annotate("Peter Parker is a nice guy and lives in New York.")
    conll_lines = ''

    for token, pos, ner in zip(parsed['token'], parsed['pos'], parsed['ner']):
        print('token', token, 'ner::', ner)
        ner = 'J-Label'

        conll_lines += "{} {} {} {}\n".format(token, pos, pos, ner)

    print(conll_lines)


def constructCoNLL(text, lpos, rpos, tag):

    tag_data = text[lpos:rpos].split(' ')
    print(tag_data)

    conll_pipeline = get_ann_pipeline()

    parsed = conll_pipeline.annotate(text)
    conll_lines = ''

    for token, pos, ner in zip(parsed['token'], parsed['pos'], parsed['ner']):
        if token in tag_data:
            ner = tag
        else:
            ner = 'O'

        conll_lines += "{} {} {} {}\n".format(token, pos, pos, ner)

    # print(conll_lines)

    return conll_lines

def collectCoNLLData(array, text, lpos, rpos, tag):
    array.append(constructCoNLL(text, lpos, rpos, tag))

def saveToFile(array, fileName):
    fp = open(fileName, 'w')
    for data in array:
        fp.write(data)
        fp.write('\n')

    fp.close()

def getDataFromMysql(selector, table):
    sql = f"SELECT data,start,end,label FROM training_data.{table} where label ='{selector}' limit 5;"
    mydb = mysql.connector.connect(host="192.168.15.43", user="root", password="softinc", database="training_data")

    cursor = mydb.cursor()
    cursor.execute(sql)

    data = []

    for eachRow in cursor:
        data.append({'data': eachRow[0], 'lpos': eachRow[1], 'rpos': eachRow[2], 'tag': eachRow[3]})

    return data

array = []
# text = "Peter Parker is a nice guy and lives in New York."
# collectCoNLLData(array, text, 6, 12, 'I-PER')
# saveToFile(array, 'test.conll')
# print(array)
ar = []

seller = getDataFromMysql('SELLER', 'deed_document')
buyer = getDataFromMysql('BUYER', 'deed_document')

ar = seller
ar.extend(buyer)

for eachRecord in seller:
    collectCoNLLData(array, eachRecord['data'], int(eachRecord['lpos']), int(eachRecord['rpos']), eachRecord['tag'])

for eachRecord in buyer:
    collectCoNLLData(array, eachRecord['data'], int(eachRecord['lpos']), int(eachRecord['rpos']), eachRecord['tag'])

saveToFile(array, 'trainall.conll')