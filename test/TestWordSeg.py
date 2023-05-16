import unittest
from TestUtils import TestWordSegment

class TestWordSeg(unittest.TestCase):
    def test0(self):
        input = "Máy bay nào đến thành phố Huế lúc 13:30HR ?"
        expect = "['Máy bay', 'nào', 'đến', 'thành phố', 'Huế', 'lúc', '13:30HR', '?']"
        self.assertTrue(TestWordSegment.test(input, expect, 100))
    def test1(self):
        input = "Máy bay nào bay từ Đà Nẵng đến TPHCM mất 1 giờ ?"
        expect = "['Máy bay', 'nào', 'bay', 'từ', 'Đà Nẵng', 'đến', 'TPHCM', 'mất', '1 giờ', '?']"
        self.assertTrue(TestWordSegment.test(input, expect, 101))
    def test2(self):
        input = "Hãy cho biết mã hiệu các máy bay hạ cánh ở Huế ?"
        expect = "['Hãy', 'cho biết', 'mã hiệu', 'máy bay', 'hạ cánh', 'ở', 'Huế', '?']"
        self.assertTrue(TestWordSegment.test(input, expect, 102))
    def test3(self):
        input = "Máy bay nào xuất phát từ TPHCM, lúc mấy giờ ?"
        expect = "['Máy bay', 'nào', 'xuất phát', 'từ', 'TPHCM', 'lúc', 'mấy giờ', '?']"
        self.assertTrue(TestWordSegment.test(input, expect, 103))
    def test4(self):
        input = "Máy bay nào bay từ TPHCM đến Hà Nội ?"
        expect = "['Máy bay', 'nào', 'bay', 'từ', 'TPHCM', 'đến', 'Hà Nội', '?']"
        self.assertTrue(TestWordSegment.test(input, expect, 104))
    def test5(self):
        input = "Máy bay VN4 có xuất phát từ Đà Nẵng không ?"
        expect = "['Máy bay', 'VN4', 'có', 'xuất phát', 'từ', 'Đà Nẵng', 'không', '?']"
        self.assertTrue(TestWordSegment.test(input, expect, 105))
    def test6(self):
        input = "Thời gian máy bay VJ5 bay từ Hà Nội đến Khánh Hòa mất mấy giờ ?"
        expect = "['máy bay', 'VJ5', 'bay', 'từ', 'Hà Nội', 'đến', 'Khánh Hòa', 'mất', 'mấy giờ', '?']"
        self.assertTrue(TestWordSegment.test(input, expect, 106))
    def test7(self):
        input = "Máy bay của hãng hàng không VietJet Air bay đến những thành phố nào ?"
        expect = "['Máy bay', 'VietJet Air', 'bay', 'đến', 'thành phố', 'nào', '?']"
        self.assertTrue(TestWordSegment.test(input, expect, 107))
    def test8(self):
        input = "Có máy bay nào xuất phát từ Hải Phòng không ?"
        expect = "['Có', 'máy bay', 'nào', 'xuất phát', 'từ', 'Hải Phòng', 'không', '?']"
        self.assertTrue(TestWordSegment.test(input, expect, 108))
    def test9(self):
        input = "Có máy bay nào bay từ Hải Phòng đến Khánh Hòa không ?"
        expect = "['Có', 'máy bay', 'nào', 'bay', 'từ', 'Hải Phòng', 'đến', 'Khánh Hòa', 'không', '?']"
        self.assertTrue(TestWordSegment.test(input, expect, 109))
