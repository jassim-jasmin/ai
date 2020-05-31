import spacy
import joblib
import re
# from etl_ai_prediction.features import features
from etl_ai_prediction.features import features
# from textblob import TextBlob
# from textblob.taggers import NLTKTagger
# from difflib import SequenceMatcher
import string
import csv
import os
from fuzzywuzzy import process

featureObj = features()
nlp = spacy.load('en_core_web_sm')

class Api_crf_predication_ETL:
    def __init__(self):
        self.tagged = []
        self.tagged_single_line = []
        self.finallist = []
        self.unwanted_elements = []
        self.finallist_single_line = []
        self.lender = './etl_ai_prediction/models/GENERAL/LENDER.pkl'
        self.borrower = './etl_ai_prediction/models/GENERAL/BORROWER.pkl'
        self.crf_seller = None
        self.crf_buyer = None
        self.crf_lender = None
        self.crf_borrower = None
        self.county = None
        self.state = None
        self.model_path = './etl_ai_prediction/models/'
        self.filtered_deed_types_path = './etl_ai_prediction/filtered_deed_types.csv'
        self.similarStringConfidence = 89

    def assignDeedMortgageVariable(self, key, county=None, state=None):
        """
        :var seller,buyer,crf_seller,crf_borrower is model for prediction
        :param key:
        :param county:
        :param state:
        :return: False is success of this function else returns a json with error log
        """
        try:
            path = f'{self.model_path}/{state}/{county}'

            if key == 'deed':
                if not os.path.exists(path):
                    # dir_check = 'NOT FOUND'
                    return 'MODEL NOT FOUND'

                """
                # made it as empty, it will restrict use of general model
                dir_check = ''
                if dir_check:
                    # General prediction models
                    seller = './models/GENERAL/SELLER.pkl'
                    buyer = './models/GENERAL/BUYER.pkl'
                else:
                """
                # County based prediction models
                seller = f'{self.model_path}/{state}/{county}/SELLER.pkl'
                buyer = f'{self.model_path}/{state}/{county}/BUYER.pkl'

                # loading models
                self.crf_seller = joblib.load(seller)
                self.crf_buyer = joblib.load(buyer)
            elif key == 'mortgage':
                self.crf_lender = joblib.load(self.lender)
                self.crf_borrower = joblib.load(self.borrower)

            return False
        except Exception as e:
            print('error in assignDeedMortgageVariable', e)
            return 'INVALID INPUT'

    def removeSimilarStringFromArray(self, stringList) -> list:
        """
        For removing similar string from array and only retain the lengthiest one
        :var index: index of array
        :param stringList: List of string
        :return: List contains unique string
        """
        stringArrayLimit = len(stringList)
        index = 0
        while (stringArrayLimit > 0):
            if len(stringList)>index:
                # Finding string match ratio for searchString in stringSet
                stringSetMatchRatio = process.extract(stringList[index], stringList)

                #getting element match confidence above similarStringConfidence
                similarString = [ele[0] for ele in stringSetMatchRatio if ele[1]>self.similarStringConfidence]

                # Removing longest string from a list
                longestString = max(similarString, key=lambda s: (len(s), s))

                #removing longest string from similar list
                similarString.remove(longestString)

                lengthBeforeUpdation = len(stringList)

                #removing similar string from string set
                stringList = [ele for ele in stringList if ele not in similarString]

                lengthAfeterUpdation = len(stringList)

                if longestString not in stringList:
                    stringList.append(longestString)

                if lengthAfeterUpdation < lengthBeforeUpdation:
                    # for checking next element when the current element is removed
                    index -= 1
            else:
                break

            index += 1

        return stringList


    def clean(self, json) -> dict:
        """
        For removing similar words from each json array string
        :param json:
        :return: json result with removed similar strings
        """
        result = []
        for text in json:
            text_list = json[text]
            text_list_final = text_list
            text_list_final = self.removeSimilarStringFromArray(text_list_final)

            for txt in text_list_final:
                txt = txt.strip()
                # t = txt
                # nltk_tagger = NLTKTagger()
                # blob = TextBlob(t, pos_tagger=nltk_tagger)
                # noun_arr = blob.noun_phrases
                # print(noun_arr)
                # if noun_arr:
                # if txt not in result:
                result.append(txt)
        result = {text: result}
        # print(result)
        return result

    def loadGetIndexDeedType(self, test_text) -> list:
        """
        Loading DEED types for removing data above header
        :param test_text:
        :return:
        """
        index_count = []
        try:
            with open(self.filtered_deed_types_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                deed_types = [row["type"] for row in csv_reader]
            for data in deed_types:
                if data in test_text:
                    b = test_text.index(data)
                    index_count.append(b)
        except Exception as e:
            print('error in loadGetIndexDeedType', e)

        return index_count

    def deedPortionSelector(self, test_text) -> str:
        """
        Text start with grantee only need to process, removes characters for processing
        :param test_text: data
        :return: single lined text with only contains the regular expression
        """
        # Line removal
        test_text_single_line = re.sub(r'(\n)+', ' ', test_text)
        # symbol removal
        test_text_single_line = test_text_single_line.lower()

        if self.state == 'TX':
            test_text_single_line = re.sub(r'grantee(\()?(s?)(\))?(\s)?:', ', does hereby convey to buyer',
                                           test_text_single_line)
        test_text_single_line = re.sub(r'grantee(s?)(\s)?:', ', does hereby convey to', test_text_single_line)
        test_text_single_line = test_text_single_line.replace('.', ' ').replace(':', ' ').replace('[', ' ').replace(
            ']', ' ').replace('_', ' ').replace('"', ' ').replace('\'', '').replace('|', '')
        test_text_single_line = re.sub(r'(\s){2,}', ' ', test_text_single_line)

        return test_text_single_line

    def prediction(self, test_single_line, tagged_single_line, model, prediction_type) -> dict:
        """
        General prediction function for both deed and mortgage
        :param test_single_line: text data
        :param tagged_single_line: text data
        :param model: trainded model for deed or mortgage based on entity name
        :param prediction_type: DEED/MORTGAGE
        :return: dictionary of entity list with prediction values
        """
        predicted = model.predict(test_single_line)
        entityList = featureObj.extractEntities(predicted[0], tagged_single_line)

        if entityList:
            try:
                entityList = self.clean(entityList)
            except Exception as e:
                print(f'issue with clean {prediction_type} ---> ', e)
        else:
             entityList = {prediction_type: ''}

        return entityList

    def getSingleLineText(self, parced_single_line, tagged_single_line):
        """

        :param parced_single_line:
        :param tagged_single_line:
        :return:
        """
        finallist_single_line = []

        for i in range(len(parced_single_line)):
            tagged_single_line.append((str(parced_single_line[i]), parced_single_line[i].tag_))

        finallist_single_line.append(tagged_single_line)
        test_single_line = [featureObj.sent2features(s) for s in finallist_single_line]

        return test_single_line

    def getParsed(self, test_text, test_text_single_line):
        """
        NLP process
        :param test_text: text data
        :param test_text_single_line: single line text data
        :return: original NLP processed, processed text NLP processed
        """
        parsed = nlp(test_text)
        parced_single_line = nlp(test_text_single_line)

        return parsed, parced_single_line

    def deedPrediction(self, data):
        """
        For predicting seller buyer
        :param data: text document
        :return: json if successfull prediction else returns error with tyepe string
        """
        tagged_single_line = []
        test_text = data.lower()
        test_text = re.sub(f'[^{re.escape(string.printable)}]', '', test_text)

        if (test_text):
            index_count = self.loadGetIndexDeedType(data)

            if (index_count):
                # Trimming the string before first deed type encounter
                if (len(test_text[min(index_count):]) > 100):
                    test_text = test_text[min(index_count):]

            test_text_single_line = self.deedPortionSelector(test_text)
            parsed, parced_single_line = self.getParsed(test_text, test_text_single_line)

            # for i in range(len(parsed)):
            #     tagged.append((str(parsed[i]), parsed[i].tag_))
            #
            # finallist.append(tagged)
            # test = [featureObj.sent2features(s) for s in finallist]

            #########################single line text##########################
            test_single_line = self.getSingleLineText(parced_single_line, tagged_single_line)

            ##########################SELLER###################################
            seller_entityList = self.prediction(test_single_line, tagged_single_line, self.crf_seller, 'SELLER')

            ##########################BUYER####################################
            buyer_entityList = self.prediction(test_single_line, tagged_single_line, self.crf_buyer, 'BUYER')

            ###################################################################
            entityList = {**seller_entityList, **buyer_entityList}
            if (entityList):
                return entityList
            else:
                return 'NOT AVAILABLE'
        else:
            return 'NO TEXT FOUND'

    def mortgagePrediction(self, test_text):
        """
        For predicting lender borrower
        :param test_text: text data
        :return: json if successfull prediction else returns error with tyepe string
        """
        tagged_single_line = []
        test_text = re.sub(f'[^{re.escape(string.printable)}]', '', test_text)
        test_text = test_text.replace('_', ' ').replace('"', ' ')
        test_text_single_line = re.sub(r'(\n)+', ' ', test_text)
        test_text_single_line = re.sub(r'(\s){2,}', ' ', test_text_single_line)

        if (test_text):
            parsed, parced_single_line = self.getParsed(test_text, test_text_single_line)

            # for i in range(len(parsed)):
            #     tagged.append((str(parsed[i]), parsed[i].tag_))
            #
            # finallist.append(tagged)
            # test = [featureObj.sent2features(s) for s in finallist]

            #########################single line text##########################
            test_single_line = self.getSingleLineText(parced_single_line, tagged_single_line)

            ##########################LENDER###################################
            lender_entityList = self.prediction(test_single_line, tagged_single_line, self.crf_lender, 'LENDER')

            ##########################BORROWER#################################
            borrower_rv_entityList = self.prediction(test_single_line, tagged_single_line, self.crf_borrower, 'BORROWER')

            ###################################################################
            entityList = {**lender_entityList, **borrower_rv_entityList}

            if (entityList):
                return entityList
            else:
                return 'NOT AVAILABLE'
        else:
            return 'NO TEXT FOUND'

    def etlPredictionMain(self, key, data):
        """
        Pass the data value to deed or mortgage prediction function based on key value
        :param key: deed/mortgage
        :param data: text data
        :return: prediction result
        """
        if (key == 'deed'):
            return self.deedPrediction(data)

        elif (key == 'mortgage'):
            return self.mortgagePrediction(data)
        else:
            return 'INVALID INPUT'
