from unittest import TestCase
# from etl_ai_prediction.Api_crf_predication_ETL import Api_crf_predication_ETL
# from etl_ai_prediction.Api_crf_predication_ETL import Api_crf_predication_ETL
from etl_api.etl_ai_prediction.Api_crf_predication_ETL import Api_crf_predication_ETL

class TestApi_crf_predication_ETL(TestCase):
    def setUp(self) -> None:
        self.obj = Api_crf_predication_ETL()


    def tearDown(self) -> None:
        pass

    def test_test(self):
        pass

    def test_assign_deed_mortgage_variable(self):
        self.assertFalse(self.obj.assignDeedMortgageVariable('deed', 'LOSANGELES', 'CA'), 'the assign function has error')

    def test_case_remove_similar_string(self):
        return [
            {
                'input':  ['aaab', 'ab', 'aaaaab', 'xx', 'xa', 'ax'],
                'output': ['aaaaab', 'xx', 'xa', 'ax'],
                'issue': 'removing similar string from array has issue'
            },
            {
               'input':  ['aaab', 'd', 'ab', 'aaaaab', 'xx', 'j', 'dd', 'jj', 'xa', 'ax'],
                'output': ['aaaaab', 'xx', 'dd', 'jj', 'xa', 'ax'],
                'issue': 'second string came with different value need to consider'
            },
            {
                'input': ['aaab', 'aaab'],
                'output': ['aaab'],
                'issue': 'duplicate long string come means retain one'
            },
            {
                'input': ['aaab'],
                'output': ['aaab'],
                'issue': 'single string should not removed'
            },
            {
                'input': ["NATL AR MOR'I'GAGE LLC D", 'NATIONSTAR MORTGAGE LLC D/2', 'NATIONSTAR MORTGAGE LLC D / B / A MR', 'other mortgage loan servicing obligations', 'KATIONSTAR MORTGAGE LLC D / B / A MR'],
                'output':["NATL AR MOR'I'GAGE LLC D", 'NATIONSTAR MORTGAGE LLC D / B / A MR', 'other mortgage loan servicing obligations'],
                'issue':'similar_string_confidence test'
            }
        ]

    def test_remove_similar_string(self):
        testCase = self.test_case_remove_similar_string()
        for eachCase in testCase:
            value = self.obj.removeSimilarStringFromArray(eachCase['input'])
            self.assertEqual(eachCase['output'], value, eachCase['issue'])

    def test_case_clean(self):
        return [
            {
                'input': {'test':['aaaaab', 'xx', 'dd', 'jj', 'xa', 'ax']},
                'output': {'test': ['aaaaab', 'xx', 'dd', 'jj', 'xa', 'ax']},
                'issue': 'no similar issue'
            },
            {
                'input': {'test': ['aaab', 'd', 'ab', 'aaaaab', 'xx', 'j', 'dd', 'jj', 'xa', 'ax']},
                'output': {'test': ['aaaaab', 'xx', 'dd', 'jj', 'xa', 'ax']},
                'issue': 'remove duplicate issue'
            },
            {
                'input': {'test': ['aaab']},
                'output': {'test': ['aaab']},
                'issue': 'single value removed'
            },
            {
                'input': {'test': ['aaab', 'aaab']},
                'output': {'test': ['aaab']},
                'issue': 'if duplicate long string, one should be removed'
            }
        ]
    def test_clean(self):
        testCase = self.test_case_clean()
        for  eachCase in testCase:
            value = self.obj.clean(eachCase['input'])
            self.assertEqual(eachCase['output'], value, eachCase['issue'])
