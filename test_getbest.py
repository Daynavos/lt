import unittest
import getbest
from io import StringIO

class TestGetBest(unittest.TestCase):
    
    def test_getCols(self):
        sample_data = "Course,Student Number,Mark,Comment\n"
        dummy_file = StringIO(sample_data)
        num_col, mark_col = getbest.getCols(dummy_file)
        self.assertEqual(num_col,1)
        self.assertEqual(mark_col,2)
    
    
if __name__ == '__main__':
    unittest.main()