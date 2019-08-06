from fuzzywuzzy import fuzz
import os
import json
import re
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from warnings import simplefilter
import pickle
import timeit

from lcs import Substring

simplefilter(action='ignore', category=FutureWarning)

np.random.seed(0)


def replace(string):
    try:
        # string = string.replace("\n",'')
        # string = string.replace("+", '')
        # string = string.replace("-", '')
        # string = string.replace("*", '')
        # string = string.replace(",", '')
        # string = string.replace("\"", '')
        # string = string.replace(".", '')
        # string = string.replace(":", '')
        # string = string.replace("`", '')
        # string = string.replace("-", '')
        # string = string.replace("_", '')
        # string = string.replace("/", '')
        # string = string.replace("[", '')
        # string = string.replace("]", '')
        string = re.sub(r'[^a-zA-Z]*', '', string)
        string.upper()
        return string
    except Exception as e:
        print(e, " in substring")


def collectFile(directoryPath):
    try:
        print(directoryPath, 'in collectFile')
        files = []
        for r, d, f in os.walk(directoryPath):
            for file in f:
                if '.txt' in file:
                    files.append(os.path.join(r, file))
        return files
    except Exception as e:
        print(e, "in collectFile")


def getSubstringsFromFile(files, substringList):
    try:
        for file in files:
            fileData = open(file, 'r').read()
            for otherFile in files:
                if otherFile != file:
                    fileData = replace(fileData)
                    otherFileData = open(otherFile, 'r').read()
                    otherFileData = replace(otherFileData)
                    substring = Substring.getSubstring(Substring, fileData, otherFileData, 20)
                    for substrings in substring.keys():
                        substringList[substrings] = 0
                        # break
            print("break")
            break
        print("substring fetch")
        return substringList
    except Exception as e:
        print(e, "in getSubstringsFromFile")


def featureNames(firstTrainingSetPath, secondTrainingSetPath, subStringPriorityFilePath):
    mortgageFiles = collectFile(firstTrainingSetPath)
    deedFiles = collectFile(secondTrainingSetPath)
    substringList = dict()
    substringList = getSubstringsFromFile(mortgageFiles, substringList)

    substringList = getSubstringsFromFile(deedFiles, substringList)

    open(subStringPriorityFilePath, 'w').write(json.dumps(substringList))
    return substringList


def buildTrainingModel(trainingSetDirectoryPath, featureNames, targetNumber, dataDic):
    try:
        files = collectFile(trainingSetDirectoryPath)

        for eachFiles in files:
            data = []
            fp = open(eachFiles, 'r')
            fileRead = fp.read()

            for featureName in featureNames:
                data.append(fuzz.token_set_ratio(fileRead, featureName))

            if 'data' in dataDic:
                dataDic['data'].append(data)
            else:
                dataDic['data'] = []
                dataDic['data'].append(data)
            if 'target' in dataDic:
                dataDic['target'].append(targetNumber)
            else:
                dataDic['target'] = [targetNumber]
            fp.close()
        dataDic['feature_names'] = feature_names
        return dataDic

    except Exception as e:
        print(e)


def buildFullTrainingModel(trainingPathList, featureNames, targetNames):
    # try:
    trainingModel = dict()
    i = -1
    print(trainingPathList)

    for trainingPath in trainingPathList:
        i = i + 1
        trainingModel = buildTrainingModel(trainingPath, featureNames, i, trainingModel)

    trainingModel['feature_names'] = featureNames
    trainingModel['target_names'] = targetNames
    return trainingModel


# except Exception as e:
#     print(e)

def buildClassifier(trainingModelPath, classifierPath):
    trainingModel = json.loads(open(trainingModelPath, 'r').read())
    df = pd.DataFrame(trainingModel['data'], columns=trainingModel['feature_names'])
    df['target_names'] = pd.Categorical.from_codes(trainingModel['target'], trainingModel['target_names'])
    features = df.columns[:4]
    y = pd.factorize(df['target_names'])[0]
    clf = RandomForestClassifier(n_jobs=2, random_state=0)
    clf.fit(df[features], y)
    pickle.dump(clf, open(classifierPath, 'wb'))


def predict(testModel, classifierPath):
    classifier = pickle.load(open(classifierPath, 'rb'))
    df = pd.DataFrame(testModel['data'], columns=testModel['feature_names'])
    # print(testModel['target'], testModel['target_names'])  #
    df['target_names'] = pd.Categorical.from_codes(testModel['target'], testModel['target_names'])
    features = df.columns[:4]
    pre = classifier.predict(df[features])
    preds = np.array(df['target_names'])[pre]
    # print(df['target_names'])
    # print(preds, 'the prediction')
    print(classifier.predict(df[features]))

def setTestData(firstTrainingSetPath, secondTrainingSetPath, feature_names, targetNames, testModelFirstPath, testModelSecondPath):
    testModelMortgage = buildFullTrainingModel([firstTrainingSetPath], feature_names, targetNames)  #
    open(testModelFirstPath, 'w').write(json.dumps(testModelMortgage))  #

    testModelDeed = buildFullTrainingModel([secondTrainingSetPath], feature_names, targetNames)
    open(testModelSecondPath, 'w').write(json.dumps(testModelDeed))  #

def setDataModel(firstTrainingSetPath, secondTrainingSetPath, subStringPriorityFilePath, trainingModelPath,
                 classifierPath, testModelFirstPath, testModelSecondPath, feature_names):
    featureNames(firstTrainingSetPath, secondTrainingSetPath, subStringPriorityFilePath)  #
    pathList = [firstTrainingSetPath, secondTrainingSetPath]
    targetNames = ['mortgage', 'deed']
    trainingModel = buildFullTrainingModel(pathList, feature_names, targetNames)  #
    open(trainingModelPath, 'w').write(json.dumps(trainingModel))  #
    buildClassifier(trainingModelPath, classifierPath)  #

    setTestData(firstTrainingSetPath, secondTrainingSetPath, feature_names, targetNames, testModelFirstPath,
                testModelSecondPath)

start = timeit.default_timer()

firstTrainingSetPath = '/root/Documents/dev/ail/files/mortgage'
secondTrainingSetPath = '/root/Documents/dev/ail/files/deed'
subStringPriorityFilePath = '/root/Documents/mj/python/model/subStringPriority.txt'
trainingModelPath = '/root/Documents/mj/python/model/trainingModel.txt'
classifierPath = '/root/Documents/mj/python/model/classifier.sav'
testModelFirstPath = '/root/Documents/mj/python/model/testModelMortgage.txt'
testModelSecondPath = '/root/Documents/mj/python/model/testModelDeed.txt'

# feature_names = json.loads(open(subStringPriorityFilePath, 'r').read())

# setDataModel(firstTrainingSetPath, secondTrainingSetPath, subStringPriorityFilePath, trainingModelPath,
# classifierPath, testModelFirstPath, testModelSecondPath, feature_names)

print('mortgage')
testModel = json.loads(open(testModelFirstPath,'r').read())
predict(testModel,classifierPath)

print('deed')
testModel = json.loads(open(testModelSecondPath,'r').read())
predict(testModel,classifierPath)

stop = timeit.default_timer()
print('Time: ', stop - start)
