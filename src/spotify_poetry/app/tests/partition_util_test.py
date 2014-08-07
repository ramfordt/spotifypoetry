'''
Created on Aug 5, 2014

@author: ramsysafadi
'''
import unittest

from spotify_poetry.utils.partition_util import integer_partition, string_partition


class TestPartitonFunctions(unittest.TestCase):

    def test_integer_partition(self):
        # Normal case
        test = 4
        expected = ["(4,)","(1, 3)","(2, 2)","(3, 1)","(1, 1, 2)","(1, 2, 1)","(2, 1, 1)","(1, 1, 1, 1)"]
        print 'Integer Partition - Normal Case : ' + str(test)
        result = integer_partition(test)
        print result
        self.compare_integer_partition(result, expected)

        # Extreme case: 1
        test = 1
        expected = ["(1,)"]
        print 'Integer Partition Test - Extreme Case 1 : ' + str(test)
        result = integer_partition(test)
        print result
        self.compare_integer_partition(result, expected)
        
        #TODO: Add Extreme Case 0
        #TODO: Add Expected failures

    def test_string_partition(self):
        # Normal case
        test = "I am the walrus"
        expected = [
                "['I am the walrus']",
                "['I', 'am the walrus']",
                "['I am', 'the walrus']",
                "['I am the', 'walrus']",
                "['I', 'am', 'the walrus']",
                "['I', 'am the', 'walrus']",
                "['I am', 'the', 'walrus']",
                "['I', 'am', 'the', 'walrus']"]
        print 'String Partition Test - Normal : ' + test
        result = string_partition(test)
        print result['tuples']
        self.compare_string_partition(result['tuples'], expected)

        # Extreme case: 1 word
        test = "Hello"
        expected = ["['Hello']"]
        print 'String Partition Test - Extreme Case 1 word : ' + test
        result = string_partition(test)
        print result['tuples']
        self.compare_string_partition(result['tuples'], expected)

        #TODO: Add Extreme Case 0
        #TODO: Add Expected failures


    def compare_integer_partition(self, result, expected):
        self.assertEqual(len(expected), len(result))
        for combination in result:
            self.assertTrue(str(combination) in expected, str(combination) + " is not in the results")

    def compare_string_partition(self, result, expected):
        self.assertEqual(len(expected), len(result))
        for combination in result:
            self.assertTrue(str(combination) in expected, str(combination) + " is not in the results")
            

if __name__ == '__main__':
    unittest.main()