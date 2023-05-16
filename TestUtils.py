from dependency import WordSegment, Dependency
import os

from logicalform import LogicalForm

from proceduralsemantics import ProceduralSemantics


TEST_DIR = "./test/input/"
EXPECT_DIR = "./test/expect/"
OUTPUT_DIR = "./test/output/"
class TestUtil:
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w", encoding="utf-8")
        file.write(inputStr)
        file.close()
        return inputStr
    
    def makeExpect(inputStr, num):
        filename = EXPECT_DIR + str(num) + ".txt"
        file = open(filename, "w", encoding="utf-8")
        file.write(inputStr)
        file.close()

class TestWordSegment:
    def test(input, expect, num):
        inputstring = TestUtil.makeSource(input, num)
        TestUtil.makeExpect(expect,num)
        TestWordSegment.writesolution(OUTPUT_DIR, inputstring, num)
        dest = open(OUTPUT_DIR + str(num) + ".txt", "r", encoding="utf-8")
        line = dest.read()
        return line == expect
    
    def writesolution(soldir, inputstring, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w", encoding="utf-8")
        res = WordSegment(inputstring)
        result=res.check()
        dest.write(str(result))
        dest.close()

class TestDependency:
    def test(input, expect, num):
        inputstring = TestUtil.makeSource(input, num)
        TestUtil.makeExpect(expect,num)
        TestDependency.writesolution(OUTPUT_DIR, inputstring, num)
        dest = open(OUTPUT_DIR + str(num) + ".txt", "r", encoding="utf-8")
        line = dest.read()
        return line == expect
    def writesolution(soldir, inputstring, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w", encoding="utf-8")
        res = Dependency(inputstring, num)
        result=res.start()
        dest.write(str(result))
        dest.close()

class TestLogicForm:
    def test(input, expect, num):
        inputstring = TestUtil.makeSource(input, num)
        TestUtil.makeExpect(expect,num)
        TestLogicForm.writesolution(OUTPUT_DIR, inputstring, num)
        dest = open(OUTPUT_DIR + str(num) + ".txt", "r", encoding="utf-8")
        line = dest.read()
        return line == expect
    def writesolution(soldir, inputstring, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w", encoding="utf-8")
        res = LogicalForm(inputstring)
        result=res.start()
        dest.write(str(result))
        dest.close()

class TestProceduralSem:
    def test(input, expect, num):
        inputstring = TestUtil.makeSource(input, num)
        TestUtil.makeExpect(expect,num)
        TestProceduralSem.writesolution(OUTPUT_DIR, inputstring, num)
        dest = open(OUTPUT_DIR + str(num) + ".txt", "r", encoding="utf-8")
        line = dest.read()
        return line == expect
    def writesolution(soldir, inputstring, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w", encoding="utf-8")
        res = ProceduralSemantics(inputstring, num)
        result=res.start()
        dest.write(str(result))
        dest.close()