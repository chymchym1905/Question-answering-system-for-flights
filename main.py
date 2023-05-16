import time
import unittest
import sys

for path in ['./test/']:
    sys.path.append(path)

def main():
    from TestWordSeg import TestWordSeg
    getAndTest(TestWordSeg)
    from TestDepend import TestDepend
    getAndTest(TestDepend)
    from TestLogicalForm import TestLogicalForm
    getAndTest(TestLogicalForm)
    from TestProcSemantic import TestProcSem
    getAndTest(TestProcSem)
    from t import run
    run()

def getAndTest(cls):
    suite = unittest.makeSuite(cls)
    test(suite)


def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())

if __name__ == "__main__":
    main()