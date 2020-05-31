import re
import os

class GetFromShare:
    def getDirectoryElements(self, pathToDirectoyr):
        try:
            files = os.listdir(pathToDirectoyr)

            return files
        except Exception as e:
            print('erron in getDrectoryElements in DirectoryHandling', e)
            return False

    def getDirectoryElementBykey(self, pathToDirecotory, searchKey):
        try:
            allElements = self.getDirectoryElements(pathToDirecotory)

            if allElements:
                allElementsArray = []
                for eachElements in allElements:
                    if re.search(searchKey, eachElements):
                        allElementsArray.append(eachElements)
            else:
                return False

            return allElementsArray
        except Exception as e:
            print('error in getDirectoryElementByKey', e)
            return False

    def getTextFileFromDiffDirectory(self, mainDirectoryPath,osDirectorySeperator):
        try:
            allFolder =  self.getDirectoryElements(mainDirectoryPath)
            allTextFilePath = []

            for eachFolder in allFolder:
                insideEachFolder = mainDirectoryPath+osDirectorySeperator+eachFolder
                textFiles = self.getDirectoryElementBykey(insideEachFolder, 'txt')
                if textFiles:
                    for eachTextFile in textFiles:
                        allTextFilePath.append(insideEachFolder+osDirectorySeperator+eachTextFile)
                else:
                    return False

            return allTextFilePath
        except Exception as e:
            print('error in getTextFileFromDiffDirectory in DirectoryHandling', e)
            return False