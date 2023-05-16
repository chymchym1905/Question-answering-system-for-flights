import ast
import os

OUTPUT_DIR = "./test/output/"
dictionary = ["máy bay", "Máy bay", "thành phố", "Đà Nẵng", "1 giờ", "cho biết", "mã hiệu",
              "hạ cánh", "xuất phát", "mấy giờ", "Hà Nội", "Khánh Hòa", "Thời gian", "Vietjet Air",
              "Hải Phòng", "VietJet Air", "hàng không", "Thời gian"]
skipword = ["của", "hãng" , "hàng không", "những", "Thời gian", "các"]

class WordSegment:
    def __init__(self, input):
        self.input = input
        self.output = []


    def check(self):
        self.parse()
        self.wordsegment()
        # print(self.output)
        return self.output
        
    def parse(self):
        inp = str(self.input).split(" ")
        for i in range(len(inp)):
            inp[i] = inp[i].replace(",", "")
        self.output = inp

    def wordsegment(self):
        word_list = self.output
        result = []
        i = 0
        while i < len(word_list):
            sequence = word_list[i]
            j = i + 1
            while j < len(word_list) and ' '.join(word_list[i:j+1]) in dictionary:
                sequence = ' '.join(word_list[i:j+1])
                j += 1
            result.append(sequence)
            i = j
        result = [word for word in result if word not in skipword]
        self.output = result

class Dependency:
    noun = ["Máy bay", "máy bay", "thành phố"]
    nmodifier = "mã hiệu"
    nameflight = ["VietJet Air", "VJ5", "VN4"]
    nameloc = ["Huế", "Đà Nẵng", "TPHCM", "Hà Nội", "Hải Phòng", "Khánh Hòa"]
    verb = ["xuất phát", "cho biết", "hạ cánh", "bay"]
    time = ["13:30HR", "1 giờ", "mấy giờ"]
    querytime = "mấy giờ"
    whdet = "nào"
    toloc = "đến"
    fromloc = "từ"
    duration = "mất"
    yes = ["Có", "có"]
    no = "không"
    
    def __init__(self, input, num):
        self.root = False
        self.stack = ["root"]
        # with open(os.path.join(OUTPUT_DIR + str(num-100) + ".txt"), 'r', encoding="utf-8") as file:
        #     a = file.read()
        self.buffer = list(ast.literal_eval(input))
        self.output = []
        # print(num)

    def start(self):
        self.createrelation()
        # print(self.output)
        self.output = [d for d in self.output if not ("nsubj" in d and "bay" in d["nsubj"])]
        return self.output
    
    def rightarc_shift(self):
        self.stack += [self.buffer[0]]
        self.buffer.pop(0)

    def leftarc_reduce(self):
        self.stack.pop()

    
    def createrelation(self):
        # print(self.buffer)
        while self.buffer != []:
            if self.stack == ["root"]:
                self.rightarc_shift() #shift
            elif len(self.stack)>1:
                if self.stack[-1] in self.noun and self.buffer[0] == self.whdet: #noun + nào
                    self.output += [{"wh_det": (self.stack[-1], self.buffer[0])}]
                    self.rightarc_shift() #rightarc
                elif self.stack[-1] in self.yes and self.buffer[0] not in [self.no, "?"] : #root for yesno
                    if self.root == False:
                        self.root = True #mark setence as rooted
                        # self.output += [{"root": ("root", self.stack[-1])}]
                        self.rightarc_shift() #rightarc
                        continue
                    self.rightarc_shift()
                elif self.stack[-1] in self.noun and (self.buffer[0] in self.verb or self.buffer[0]=="đến" or self.buffer[0] in self.yes): #N + V
                    self.output += [{"nsubj": (self.buffer[0], self.stack[-1])}]
                    self.leftarc_reduce() #reduce
                elif self.buffer[0] in self.verb and self.stack[-1] == "Hãy": #hãy + verb
                    self.output += [{"command": (self.buffer[0], "Hãy")}]
                    self.leftarc_reduce() #leftarc
                elif self.stack[-1] == self.whdet: #nếu trên stack có "nào", reduce
                    self.leftarc_reduce() #reduce
                elif self.stack[-1] in self.noun and self.buffer[0] in self.nameflight: #máy bay + flight
                    self.output += [{"nmod": (self.stack[-1], self.buffer[0])}]
                    self.rightarc_shift() #rightarc
                elif self.stack[-1] in self.noun and self.buffer[0] in self.nameloc:#thành phố + city
                    self.output += [{"nameloc": (self.stack[-1], self.buffer[0])}]
                    self.rightarc_shift() #rightarc
                elif self.stack[-1] == self.nmodifier and self.buffer[0] in self.noun: #mã hiệu + máy bay
                    self.output += [{"namemod": (self.buffer[0], self.stack[-1])}]
                    self.leftarc_reduce() #leftarc
                elif (self.buffer[0] in self.verb or self.buffer[0]=="đến")  and self.stack == ["root"]:
                    if self.root == False:
                        self.root = True
                        self.output += [{"root": ("root", self.buffer[0])}]
                        self.rightarc_shift() #rightarc
                elif self.stack[-1] in self.fromloc and self.buffer[0] in self.nameloc: #từ + nameloc
                    self.output += [{"fromloc": (self.buffer[0],self.stack[-1])}]
                    self.leftarc_reduce() #leftarc
                elif self.stack[-1] in self.toloc and self.buffer[0] in self.nameloc: #đến + nameloc
                    self.output += [{"toloc": (self.buffer[0], self.stack[-1])}]
                    self.leftarc_reduce() #leftarc
                elif self.stack[-1] in self.toloc and self.buffer[0] in self.noun: #đến + noun (thành phố)
                    self.output += [{"toloc": (self.stack[-1], self.buffer[0])}]
                    self.rightarc_shift() #right arc
                elif self.stack[-1] == "ở" and self.buffer[0] in self.nameloc: #ở + nameloc
                    self.output += [{"atloc": (self.buffer[0], self.stack[-1])}]
                    self.leftarc_reduce() #leftarc
                elif (self.stack[-1] in self.verb or self.stack[-1] == "đến" ) and self.buffer[0] in self.nameloc: #verb + nameloc
                    if "fromloc" in self.output[-1]:
                        self.output += [{"namelocfrom": (self.stack[-1], self.buffer[0])}]
                        self.rightarc_shift() #rightarc
                    if "toloc" in self.output[-1]:
                        self.output += [{"namelocto": (self.stack[-1], self.buffer[0])}]
                        self.rightarc_shift() #rightarc
                    if "atloc" in self.output[-1]:
                        self.output += [{"namelocat": (self.stack[-1], self.buffer[0])}]
                        self.rightarc_shift() #rightarc
                elif self.stack[-1] == "cho biết" and self.buffer[0] == "máy bay": #special case "cho biết" + "máy bay"
                    self.output += [{"wh_det": (self.stack[-1], self.buffer[0])}]
                    self.rightarc_shift()
                elif self.stack[-1] in self.yes and self.buffer[0] == self.no: # có + không
                    self.output +=[{"y/nquery": (self.stack[-1], self.buffer[0])}] 
                    self.rightarc_shift() #rightarc
                elif self.stack[-1] in self.nameloc or self.stack[-1] in self.nameflight: #nameloc on top of the stack
                    self.leftarc_reduce() #reduce
                elif self.stack[-1] in self.verb and self.buffer[0] == self.duration: #verb + mất
                    self.output += [{"duration": (self.stack[-1], self.buffer[0])}]
                    self.rightarc_shift() #rightarc
                elif self.stack[-1] in self.verb and self.buffer[0] == "lúc": #verb + lúc
                    self.output += [{"attime": (self.stack[-1], self.buffer[0])}]
                    self.rightarc_shift() #rightarc
                elif (self.stack[-1] == self.duration or self.stack[-1] == "lúc") and self.buffer[0] in self.time: #lúc/mất + time
                    if self.time != "mấy giờ": #13:30HR, 1 giờ
                        self.output += [{"time": (self.stack[-1], self.buffer[0])}]
                        self.rightarc_shift() #rightarc
                    else: #mấy giờ
                        self.output += [{"querytime": (self.stack[-1], self.buffer[0])}]
                        self.rightarc_shift()
                elif  self.buffer[0] == "?" or self.buffer[0] in self.no: #verb + ? or không
                    # print(self.output)
                    if len(self.stack) > 2:
                        self.leftarc_reduce()
                         #reduce until there's only main verb and root
                    elif "y/nquery" in self.output[-1]:
                        break
                    elif len(self.stack) <= 2:
                        # self.output += [{"query": (self.stack[-1], self.buffer[0])}]
                        self.rightarc_shift() #rightarc
                else: self.rightarc_shift() #shift
            # print(self.stack, self.buffer)
