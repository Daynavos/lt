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
    
    def test_findTop(self):
        sample_data = """Course,Student Number,Mark,Comment
ELEN3020,160001,72,OK
ELEN3020,167381,90,Check
ELEN3020,143211,83,-
ELEN3020,17171,48,Redo
ELEN3020,191919,73,-"""
        
        dummy_file = StringIO(sample_data)
        num_col = 1
        mark_col = 2
        best_ind, best = getbest.findTop(dummy_file, num_col, mark_col)

        self.assertEqual(best_ind, "167381")
        self.assertEqual(best, 90)
    
if __name__ == '__main__':
    unittest.main()