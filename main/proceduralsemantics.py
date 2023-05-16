import ast

flights = {
    'VN1': {'ATIME': 'HUE 11:00HR', 'DTIME': 'HCM 10:00HR', 'RUN-TIME': 'HCM HUE 1:00 HR'},
    'VN2': {'ATIME': 'HCM 16:30HR', 'DTIME': 'DN 15:30HR', 'RUN-TIME': 'DN HCM 1:00 HR'},
    'VN3': {'ATIME': 'HN 6:30HR', 'DTIME': 'HCM 4:30HR', 'RUN-TIME': 'HCM HP 2:00 HR'},
    'VN4': {'ATIME': 'DN 11:30HR', 'DTIME': 'HN 9:30HR', 'RUN-TIME': 'HN DN 2:00 HR'},
    'VN5': {'ATIME': 'KH 17:45HR', 'DTIME': 'HCM 17:00HR', 'RUN-TIME': 'HCM KH 0:45 HR'},
    'VJ1': {'ATIME': 'HUE 13:30HR', 'DTIME': 'HN 12:30HR', 'RUN-TIME': 'HN HUE 1:00 HR'},
    'VJ2': {'ATIME': 'HN 11:00HR', 'DTIME': 'DN 9:30HR', 'RUN-TIME': 'DN HN 1:30 HR'},
    'VJ3': {'ATIME': 'HP 11:45HR', 'DTIME': 'HCM 9:45HR', 'RUN-TIME': 'HCM HP 2:00 HR'},
    'VJ4': {'ATIME': 'DN 9:30HR', 'DTIME': 'HCM 8:30HR', 'RUN-TIME': 'HCM DN 1:00 HR'},
    'VJ5': {'ATIME': 'KH 10:45HR', 'DTIME': 'HN 9:00HR', 'RUN-TIME': 'HN KH 0:45 HR'}
}

class ProceduralSemantics:
    def __init__(self, input, num) -> None:
        self.input = list(ast.literal_eval(input))
        self.output = []
        self.question = {
            'WH': False,
            'YN': False,
            'DEPFLIGHT': False,
            'DESTFLIGHT': False,
            'FLIGHT' : '',
            'DEP': '',
            'DEST': '',
            'RUNTIME': '',
            'DTIME': '',
            'ATIME': '',
        }
        # print(num)

    def start(self):
        self.DetermineQuestion()
        self.answer()
        # print(self.output)
        return self.output
    
    def encodeCity(self, city):
        if city == "Huế": return 'HUE'
        elif city == 'TPHCM': return 'HCM'
        elif city == 'Khánh Hoà': return 'KH'
        elif city == 'Hà Nội': return 'HN'
        elif city == 'Đà Nẵng': return 'DN'
        elif city == 'Hải Phòng': return 'HP'


    def DetermineQuestion(self):
        for x in self.input:
            if x == "WH-FLIGHT":
                self.question['WH'] = True
                self.question['FLIGHT'] = '?'
            elif x == "WH-CITY":
                self.question['WH'] = True
                self.question['CITY'] = '?'
            elif x == "DEP": self.question["DEPFLIGHT"] = True
            elif x == 'DEST': self.question["DESTFLIGHT"] = True
            elif x == 'ASSERTTRUE': self.question['YN'] = True
            elif isinstance(x, dict):
                if 'DURATION' in x :
                    if x['DURATION'] == '?':
                        self.question['WH'] = True
                        self.question['RUNTIME'] = '?'
                    else: self.question['RUNTIME'] = x['DURATION']
                if 'ATTIME' in x:
                    if x['ATTIME'] == '?':
                        self.question['WH'] = True
                        if self.question['DESTFLIGHT'] == True: self.question['ATIME'] = '?'
                        elif self.question['DEPFLIGHT'] == True: self.question['DTIME'] = '?'
                    else:
                        if self.question['DESTFLIGHT'] == True: self.question['ATIME'] = x['ATTIME']
                        elif self.question['DEPFLIGHT'] == True: self.question['DTIME'] = x['ATTIME']
                if 'SOURCE' in x:
                    self.question['DEP'] = x['SOURCE']
                if 'ARRIVE' in x:
                    self.question['DEST'] = x['ARRIVE']
                if 'FLIGHT' in x:
                    # print(x['FLIGHT'])
                    self.question['FLIGHT'] = x['FLIGHT']
                
    def answer(self):
        target = []
        # print(self.question)
        for x in self.question:
            if self.question[x] == '?': target += [x]
        if len(target) == 1:
            for x in target:
                if x == 'FLIGHT':
                    for flight, info in flights.items():
                        if self.question['DESTFLIGHT'] == True:
                            if self.question ['DEST'] != '' and self.question['ATIME'] != '':
                                if self.question['DEST'] in info['ATIME'] and self.question['ATIME'] in info['ATIME']: self.output +=[flight]     
                            elif self.question['DEST'] != '':
                                if self.question['DEST'] in info['ATIME']: self.output += [flight] 
                        elif self.question['DEPFLIGHT'] == True:
                            if self.question ['DEP'] != '' and self.question['DTIME'] != '':
                                if self.question['DEP'] in info['DTIME'] and self.question['DTIME'] in info['DTIME']: self.output +=[flight]
                            elif self.question['DEP'] != '':
                                if self.question['DEP'] in info['DTIME']: self.output += [flight]
                        elif self.question['DEP'] != '' and self.question['DEST']!= '':                            
                            if self.question['DEP'] == info['RUN-TIME'].split()[0] and self.question['DEST'] == info['RUN-TIME'].split()[1]:
                                # print(info['RUN-TIME'])
                                if self.question['RUNTIME'] != '' and self.question['RUNTIME'] in info['RUN-TIME']:
                                    self.output += [flight]
                                elif self.question['RUNTIME'] == '': self.output+=[flight]
                elif x =='RUNTIME':
                    for flight, info in flights.items():
                        # print(info['RUN-TIME'])
                        if flight == self.question['FLIGHT'] and self.question['DEP'] in info['RUN-TIME'].split()[0] and self.question['DEST'] in info['RUN-TIME'].split()[1]:
                            self.output += [info['RUN-TIME'].split()[-2]]
                elif x == 'CITY':
                    for flight, info in flights.items():
                        if self.question['DESTFLIGHT'] == True and self.question['FLIGHT'] in flight:
                            self.output += [info['ATIME'].split()[0]]
        elif 'FLIGHT' in target and 'DTIME' in target:
            self.output = {}
            for flight, info in flights.items():
                if self.question['DEPFLIGHT'] == True:
                    if self.question['DEP'] == info['DTIME'].split()[0]:
                        self.output[flight] = info['DTIME'].split()[1]

        if self.question['YN'] == True and self.output == []:
            self.output = False
        elif self.question['YN'] == True and self.output != []:
            self.output = True
        elif self.question['YN'] == False and self.output == []:
            self.output = None
        
        if isinstance(self.output, list):
            if len(self.output) == 1: self.output = self.output[0]

