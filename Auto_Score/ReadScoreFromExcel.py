import pandas as pd

class RSFE:


    def __init__(self,exlPath):
        self.df = pd.DataFrame()
        self.df = pd.read_excel(exlPath)
    def getScore(self,stdID):
        for index, row in self.df.iterrows():
            name = row['姓名']
            std_id = row['帳號']
            score = row['最終成績']
            print(std_id, stdID)
            if std_id==stdID and name!=None:
                print('return!!: '+str(score))
                return score
