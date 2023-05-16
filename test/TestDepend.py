import os
import unittest
from TestUtils import TestDependency


OUTOUT_DIR = "./test/output/"
class TestDepend(unittest.TestCase):
    def test0(self):
        with open(os.path.join(OUTOUT_DIR + str(100) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'wh_det': ('Máy bay', 'nào')}, {'nsubj': ('đến', 'Máy bay')}, {'toloc': ('đến', 'thành phố')}, {'nameloc': ('thành phố', 'Huế')}, {'time': ('lúc', '13:30HR')}]"
        self.assertTrue(TestDependency.test(input, expect, 200))
    def test1(self):
        with open(os.path.join(OUTOUT_DIR + str(101) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'wh_det': ('Máy bay', 'nào')}, {'fromloc': ('Đà Nẵng', 'từ')}, {'namelocfrom': ('bay', 'Đà Nẵng')}, {'toloc': ('TPHCM', 'đến')}, {'namelocto': ('bay', 'TPHCM')}, {'duration': ('bay', 'mất')}, {'time': ('mất', '1 giờ')}]"
        self.assertTrue(TestDependency.test(input, expect, 201))
    def test2(self):
        with open(os.path.join(OUTOUT_DIR + str(102) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'command': ('cho biết', 'Hãy')}, {'namemod': ('máy bay', 'mã hiệu')}, {'wh_det': ('cho biết', 'máy bay')}, {'nsubj': ('hạ cánh', 'máy bay')}, {'atloc': ('Huế', 'ở')}, {'namelocat': ('hạ cánh', 'Huế')}]"
        self.assertTrue(TestDependency.test(input, expect, 202))
    def test3(self):
        with open(os.path.join(OUTOUT_DIR + str(103) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'wh_det': ('Máy bay', 'nào')}, {'nsubj': ('xuất phát', 'Máy bay')}, {'fromloc': ('TPHCM', 'từ')}, {'namelocfrom': ('xuất phát', 'TPHCM')}, {'attime': ('xuất phát', 'lúc')}, {'time': ('lúc', 'mấy giờ')}]"
        self.assertTrue(TestDependency.test(input, expect, 203))
    def test4(self):
        with open(os.path.join(OUTOUT_DIR + str(104) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'wh_det': ('Máy bay', 'nào')}, {'fromloc': ('TPHCM', 'từ')}, {'namelocfrom': ('bay', 'TPHCM')}, {'toloc': ('Hà Nội', 'đến')}, {'namelocto': ('bay', 'Hà Nội')}]"
        self.assertTrue(TestDependency.test(input, expect, 204))
    def test5(self):
        with open(os.path.join(OUTOUT_DIR + str(105) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'nmod': ('Máy bay', 'VN4')}, {'nsubj': ('có', 'Máy bay')}, {'fromloc': ('Đà Nẵng', 'từ')}, {'namelocfrom': ('xuất phát', 'Đà Nẵng')}, {'y/nquery': ('có', 'không')}]"
        self.assertTrue(TestDependency.test(input, expect, 205))
    def test6(self):
        with open(os.path.join(OUTOUT_DIR + str(106) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'nmod': ('máy bay', 'VJ5')}, {'fromloc': ('Hà Nội', 'từ')}, {'namelocfrom': ('bay', 'Hà Nội')}, {'toloc': ('Khánh Hòa', 'đến')}, {'namelocto': ('bay', 'Khánh Hòa')}, {'duration': ('bay', 'mất')}, {'time': ('mất', 'mấy giờ')}]"
        self.assertTrue(TestDependency.test(input, expect, 206))
    def test7(self):
        with open(os.path.join(OUTOUT_DIR + str(107) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'nmod': ('Máy bay', 'VietJet Air')}, {'toloc': ('đến', 'thành phố')}, {'wh_det': ('thành phố', 'nào')}]"
        self.assertTrue(TestDependency.test(input, expect, 207))
    def test8(self):
        with open(os.path.join(OUTOUT_DIR + str(108) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'wh_det': ('máy bay', 'nào')}, {'nsubj': ('xuất phát', 'máy bay')}, {'fromloc': ('Hải Phòng', 'từ')}, {'namelocfrom': ('xuất phát', 'Hải Phòng')}, {'y/nquery': ('Có', 'không')}]"
        self.assertTrue(TestDependency.test(input, expect, 208))
    def test9(self):
        with open(os.path.join(OUTOUT_DIR + str(109) + ".txt"), 'r', encoding="utf-8") as file:
            input = file.read()
        expect = "[{'wh_det': ('máy bay', 'nào')}, {'fromloc': ('Hải Phòng', 'từ')}, {'namelocfrom': ('bay', 'Hải Phòng')}, {'toloc': ('Khánh Hòa', 'đến')}, {'namelocto': ('bay', 'Khánh Hòa')}, {'y/nquery': ('Có', 'không')}]"
        self.assertTrue(TestDependency.test(input, expect, 209))