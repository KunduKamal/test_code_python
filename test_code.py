import os
import sys
from dotenv import load_dotenv
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

#  Replace FOLDER.PATH.YOUR_FILE with the actual file path and import your test functions.
from FOLDER.PATH.YOUR_FILE import function_test_1, function_test_2

load_dotenv()

class Test_Code(unittest.TestCase):

    def test_fun_1(self):
        result = function_test_1()
        self.assertEqual(result, "expected_result")
    def test_fun_2(self):
        result = function_test_2()

        #result needs to be perfect match
        self.assertEqual(result, "expected result")

        # result needs to be specific length
        self.assertGreater(len(result), 50)

        # result needs to contain something
        self.assertIn("expected_contence", result)

if __name__ == "__main__":
    unittest.main()

