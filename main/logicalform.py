import ast
import os

OUTPUT_DIR = "./test/output/"

class LogicalForm:
    def __init__(self, input):
        self.output = []
        self.input = list(ast.literal_eval(input))
        self.nmod = ()
        self.whdet = ()
        self.nsubj = ()
        self.fromloc = ()
        self.toloc = ()
        self.atloc = ()
        self.namelocfrom = ()
        self.namelocto = ()
        self.namelocat = ()
        self.nameloc =()
        self.duration = ()
        self.time = ()
        self.attime = ()
        self.ynquery = ()
        

    def start(self):
        self.components()
        self.createLogicalform(self.check_non_empty_variables()) 
        return self.output
    
    def components(self):
        # print(self.input)
        for dict in self.input:
            for key in dict.keys():
                value = dict[key]
                # print(type(value))
                if key == 'wh_det': self.whdet = value
                elif key == 'nmod': self.nmod =value
                elif key == 'nsubj': self.nsubj = value
                elif key == 'fromloc': self.fromloc =  value
                elif key == 'toloc': self.toloc = value
                elif key == 'atloc': self.atloc = value
                elif key == 'namelocfrom': self.namelocfrom = value
                elif key == 'namelocto': self.namelocto = value
                elif key == 'namelocat': self.namelocat = value
                elif key == 'duration': self.duration = value
                elif key == 'time': self.time = value
                elif key == 'attime': self.attime = value
                elif key == "y/nquery": self.ynquery = value
                elif key == 'nameloc': self.nameloc =  value
    
    def check_non_empty_variables(self):
        non_empty_variables = []
        for attr_name, attr_value in self.__dict__.items():
            if isinstance(attr_value, tuple) and attr_value != ():
                non_empty_variables.append(attr_name)
        return non_empty_variables
    
    def createLogicalform(self, relations):
        # print(relations)
        for relation in relations:
            if relation == 'whdet':
                value = self.whdet
                if value[0] in  ["Máy bay", "máy bay"]: self.output += ["WH-FLIGHT"]
                elif value[0] == "thành phố": self.output += ["WH-CITY"]
                elif value[0] == "cho biết" and value[1] == "máy bay": self.output += ["WH-FLIGHT"]
            elif relation == 'nmod':
                value = self.nmod
                if value[0] in ["Máy bay", "máy bay"]:
                    if value[1] == "VietJet Air": self.output += [{"FLIGHT":"VJ"}]
                    else: self.output += [{"FLIGHT": str(value[1])}]
            elif relation == 'nsubj':
                value = self.nsubj
                # print(value)
                if value[0] in ["đến", "hạ cánh"]: self.output +=["DEST"]
                elif value[0] == "xuất phát": self.output +=["DEP"]
            elif relation == 'fromloc':
                value = self.fromloc
                if value[0] == "Đà Nẵng": self.output += [{"SOURCE": "DN"}]
                elif value[0] == "TPHCM": self.output += [{"SOURCE": "HCM"}]
                elif value[0] == "Hà Nội": self.output += [{"SOURCE": "HN"}]
                elif value[0] == "Hải Phòng": self.output += [{"SOURCE": "HP"}]
            elif relation == 'toloc':
                value = self.toloc
                if value[0] == "TPHCM": self.output += [{"ARRIVE": "HCM"}]       
                elif value[0] == "Hà Nội": self.output += [{"ARRIVE": "HN"}]
                elif value[0] == "Khánh Hòa": self.output += [{"ARRIVE": "KH"}]
                elif value[0] == "đến": 
                    if not "DEST" in self.output: self.output += ["DEST"] 
            elif relation == 'nameloc':
                value = self.nameloc
                if 'toloc' in relations: self.output += [{'ARRIVE': 'HUE'}]
            elif relation == 'namelocat':
                self.output += [{"ARRIVE": "HUE"}]
            elif relation == 'time':
                value = self.time
                if value[0] == 'mất':
                    if value[1] == 'mấy giờ':
                        self.output += [{"DURATION": "?"}]
                    elif value[1] == '1 giờ':
                        self.output += [{"DURATION": "1:00 HR"}]
                elif value[0] == 'lúc':
                    if value[1] == 'mấy giờ':
                        self.output += [{"ATTIME": "?"}]
                    else: self.output += [{"ATTIME": value[1]}]
            elif relation == "ynquery": 
                self.output += ["ASSERTTRUE"]