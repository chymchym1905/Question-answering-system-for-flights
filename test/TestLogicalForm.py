import os
import unittest
from TestUtils import TestLogicForm


OUTPUT_DIR = "./test/output/"
class TestLogicalForm(unittest.TestCase):
    def test0(self):
        with open(os.path.join(OUTPUT_DIR + str(200) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "['WH-FLIGHT', 'DEST', {'ARRIVE': 'HUE'}, {'ATTIME': '13:30HR'}]"
        self.assertTrue(TestLogicForm.test(input, expect, 300))
    def test1(self):
        with open(os.path.join(OUTPUT_DIR + str(201) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "['WH-FLIGHT', {'SOURCE': 'DN'}, {'ARRIVE': 'HCM'}, {'DURATION': '1:00 HR'}]"
        self.assertTrue(TestLogicForm.test(input, expect, 301))
    def test2(self):
        with open(os.path.join(OUTPUT_DIR + str(202) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "['WH-FLIGHT', 'DEST', {'ARRIVE': 'HUE'}]"
        self.assertTrue(TestLogicForm.test(input, expect, 302))
    def test3(self):
        with open(os.path.join(OUTPUT_DIR + str(203) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "['WH-FLIGHT', 'DEP', {'SOURCE': 'HCM'}, {'ATTIME': '?'}]"
        self.assertTrue(TestLogicForm.test(input, expect, 303))
    def test4(self):
        with open(os.path.join(OUTPUT_DIR + str(204) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "['WH-FLIGHT', {'SOURCE': 'HCM'}, {'ARRIVE': 'HN'}]"
        self.assertTrue(TestLogicForm.test(input, expect, 304))
    def test5(self):
        with open(os.path.join(OUTPUT_DIR + str(205) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'FLIGHT': 'VN4'}, {'SOURCE': 'DN'}, 'ASSERTTRUE']"
        self.assertTrue(TestLogicForm.test(input, expect, 305))
    def test6(self):
        with open(os.path.join(OUTPUT_DIR + str(206) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'FLIGHT': 'VJ5'}, {'SOURCE': 'HN'}, {'ARRIVE': 'KH'}, {'DURATION': '?'}]"
        self.assertTrue(TestLogicForm.test(input, expect, 306))
    def test7(self):
        with open(os.path.join(OUTPUT_DIR + str(207) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'FLIGHT': 'VJ'}, 'WH-CITY', 'DEST']"
        self.assertTrue(TestLogicForm.test(input, expect, 307))
    def test8(self):
        with open(os.path.join(OUTPUT_DIR + str(208) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "['WH-FLIGHT', 'DEP', {'SOURCE': 'HP'}, 'ASSERTTRUE']"
        self.assertTrue(TestLogicForm.test(input, expect, 308))
    def test9(self):
        with open(os.path.join(OUTPUT_DIR + str(209) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "['WH-FLIGHT', {'SOURCE': 'HP'}, {'ARRIVE': 'KH'}, 'ASSERTTRUE']"
        self.assertTrue(TestLogicForm.test(input, expect, 309))