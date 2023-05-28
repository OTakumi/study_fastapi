import unittest
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src import calc 

class TestStringMethods(unittest.TestCase):
    def test_add_num(self):
        """
        add_numの単体テスト
        """
        self.assertEqual(8, calc.add_num(3, 4))


#    def test_is_positive(self):
#        """
#        is_positiveの単体テスト
#        """
#        self.assertTrue(calc.is_positive(3))

