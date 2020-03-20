from difflib import SequenceMatcher

class Substring:
    def longestSubstring(self,str1, str2,stringLength, dicData):
        # initialize SequenceMatcher object with
        # input string
        seqMatch = SequenceMatcher(None, str1, str2)

        # find match of longest sub-string
        # output will be like Match(a=0, b=0, size=5)
        match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))

        # print longest substring
        if (match.size > stringLength):
            matchString = str1[match.a: match.a + match.size]
            if matchString in dicData.keys():
                dicData[matchString] = dicData[matchString] + 1
                # print("other: ",dicData[matchString],str1)
            else:
                dicData[matchString] = 1
                # print("first ", dicData[matchString],str1)
            return True,dicData
        else:
            # print("end")
            return None,dicData

    def longestSubs(self,str1, str2,stringLength, dicData):
        # initialize SequenceMatcher object with
        # input string
        seqMatch = SequenceMatcher(None, str1, str2)

        # find match of longest sub-string
        # output will be like Match(a=0, b=0, size=5)
        match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))

        # print longest substring
        if (match.size > stringLength):
            matchString = str1[match.a: match.a + match.size]
            if matchString in dicData.keys():
                dicData[matchString] = dicData[matchString] + 1
                # print("other: ",dicData[matchString],str1)
            else:
                dicData[matchString] = 1
                # print("first ", dicData[matchString],str1)
            return True,dicData
        else:
            # print("end")
            return None,dicData

    def getSubstring(self,str1, str2, stringLength):
        stringList = dict()
        while self.longestSubs(self,str1, str2, stringLength,stringList):
            substringCondition, substringData = self.longestSubs(self,str1, str2, stringLength,stringList)
            if substringCondition:
                for substring, values in substringData.items():
                    str1 = str1.replace(substring, '')
                    stringList[substring] = values
            else:
                return stringList
        return stringList
    # j = getSubstring('hello my name is jassim jasmin from edava', 'my father name is jasmin from edava',3)

    # print(j)


    def substrinRank(self, string1, string2,stringLimit,dicData):
        # dicData = dict()
        while True:
            condition,data = self.longestSubstring(self,string1, string2,stringLimit,dicData)
            if condition:
                for item in data:
                    string1 = string1.replace(item,'',stringLimit)
            else:
                break
            # print(dicData)
            # break
        return dicData

# string1 = 'hello my name is jassim jasmin from edava jasmin'
# string2 = 'my father name is jasmin from edava'
# print(substrinRank(string1, string2,3))


# Driver program


# def lcs(X, Y):
#     # find the length of the strings
#     m = len(X)
#     n = len(Y)
#
#     # declaring the array for storing the dp values
#     L = [[None] * (n + 1) for i in range(m + 1)]
#
#     """Following steps build L[m + 1][n + 1] in bottom up fashion
#     Note: L[i][j] contains length of LCS of X[0..i-1]
#     and Y[0..j-1]"""
#     for i in range(m + 1):
#         for j in range(n + 1):
#             if i == 0 or j == 0:
#                 L[i][j] = 0
#             elif X[i - 1] == Y[j - 1]:
#                 L[i][j] = L[i - 1][j - 1] + 1
#             else:
#                 L[i][j] = max(L[i - 1][j], L[i][j - 1])
#
#                 # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
#     print(m,n)
#     return L[m][n]
#     # end of function lcs
#
# X = "jassim"
# Y = "jmin"
# print("Length of LCS is ", lcs(X, Y))