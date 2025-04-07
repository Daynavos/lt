import unittest
import getbest
from io import StringIO

class TestGetBest(unittest.TestCase):
    
    def setUp(self):
        self.sample_data = """Course,Student Number,Mark,Comment
ELEN3020,160001,72,OK
ELEN3020,167381,90,Check
ELEN3020,143211,83,-
ELEN3020,17171,48,Redo
ELEN3020,191919,73,-"""
        self.dummy_file = StringIO(self.sample_data)
        self.num_col = 1
        self.mark_col = 2
    
    def tearDown(self):
        self.dummy_file.close()

    def test_getCols(self):
        
        num_col, mark_col = getbest.getCols(self.dummy_file)
        self.assertEqual(num_col,1)
        self.assertEqual(mark_col,2)
    
    def test_findTop(self):

        best_ind, best = getbest.findTop(self.dummy_file, self.num_col, self.mark_col)

        self.assertEqual(best_ind, "167381")
        self.assertEqual(best, 90)
    
if __name__ == '__main__':
    unittest.main()