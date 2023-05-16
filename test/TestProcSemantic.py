import os
import unittest
from TestUtils import TestProceduralSem


OUTPUT_DIR = "./test/output/"
class TestProcSem(unittest.TestCase):
    def test0(self):
        with open(os.path.join(OUTPUT_DIR + str(300) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "VJ1"
        self.assertTrue(TestProceduralSem.test(input, expect, 400))
    def test1(self):
        with open(os.path.join(OUTPUT_DIR + str(301) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "VN2"
        self.assertTrue(TestProceduralSem.test(input, expect, 401))
    def test2(self):
        with open(os.path.join(OUTPUT_DIR + str(302) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "['VN1', 'VJ1']"
        self.assertTrue(TestProceduralSem.test(input, expect, 402))
    def test3(self):
        with open(os.path.join(OUTPUT_DIR + str(303) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "{'VN1': '10:00HR', 'VN3': '4:30HR', 'VN5': '17:00HR', 'VJ3': '9:45HR', 'VJ4': '8:30HR'}"
        self.assertTrue(TestProceduralSem.test(input, expect, 403))
    def test4(self):
        with open(os.path.join(OUTPUT_DIR + str(304) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "None"
        self.assertTrue(TestProceduralSem.test(input, expect, 404))
    def test5(self):
        with open(os.path.join(OUTPUT_DIR + str(305) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "False"
        self.assertTrue(TestProceduralSem.test(input, expect, 405))
    def test6(self):
        with open(os.path.join(OUTPUT_DIR + str(306) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "0:45"
        self.assertTrue(TestProceduralSem.test(input, expect, 406))
    def test7(self):
        with open(os.path.join(OUTPUT_DIR + str(307) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "['HUE', 'HN', 'HP', 'DN', 'KH']"
        self.assertTrue(TestProceduralSem.test(input, expect, 407))
    def test8(self):
        with open(os.path.join(OUTPUT_DIR + str(308) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "False"
        self.assertTrue(TestProceduralSem.test(input, expect, 408))
    def test9(self):
        with open(os.path.join(OUTPUT_DIR + str(309) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "False"
        self.assertTrue(TestProceduralSem.test(input, expect, 409))