import unittest 
from unittest.mock import patch
from io import StringIO

from number import number
class TestNumber(unittest.TestCase):

    @patch('sys.stdin', StringIO('5'))
    def test_number(self):
        #Run the function
        results = number()
        #Check values
        self.assertIs(results, int(5))

    @patch('sys.stdin', StringIO('22'))
    def test_optional_range_success(self):
        #Run the function
        results = number([22,100])
        #Check values
        self.assertIs(results, int(22))

    @patch('sys.stdin', StringIO('300'))
    def test_optional_range_failure(self):
        #Run the function
        results = number([5,295])
        #Check values
        self.assertIs(results, None)

    


    


    
if __name__ == '__main__':
    unittest.main()