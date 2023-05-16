# Build a simple question-answering system for domestic flights

run `python main.py` to get started

Results can be viewed in the folder view results. Note that this project is designed to answer exactly 10 given questions.
It will not work well if more question is asked.

1. Máy bay nào đến thành phố Huế luc 13:30HR ?. 
2. Máy bay nào bay từ Đà Nẵng đến TP. Hồ Chí Minh mât 1 giờ ?. 
3. Hãy cho biết mã hiệu các máy bay hạ cánh ở Huế ?. 
4. Máy bay nào xuất phát từ Tp.Hồ Chí Minh, lúc mấy giờ ?. 
5. Máy bay nào bay từ TP.Hồ Chí Minh đến Hà Nôi ?. 
6. Máy bay VN4 có xuất phát từ Đà Nẵng không ?. 
7. Thời gian máy bay VJ5 bay từ TP. Hà Nôi đến Khánh Hòa mất mấy giờ ?. 
8. Có máy bay nào xuất phát từ Hải Phòng không ?. 
9. Máy bay của hãng hàng không VietJet Air bay đến những thành phố nào ?
10. Có máy bay nào bay từ Hải Phòng đến Khánh Hòa không?

Database is hardcoded in proceduralsemantics.py. The sequence of the program is: 
1. Word Segmentation (taking keywords)
2. Shift-reduce parsing and create relation (Dependency parsing)
3. Create Logical form
4. Answer question