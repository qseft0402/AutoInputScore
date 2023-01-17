import pandas as pd

class RSFE:


    def __init__(self,exlPath,excelColName):
        self.df = pd.DataFrame()
        self.df = pd.read_excel(exlPath)
        self.excelColName=excelColName

    def getScore(self,stdID):
        for index, row in self.df.iterrows():
            name = row['姓名']
            std_id = row['帳號'] #帳號、學號
            score = row[self.excelColName] #最終成績
            print(std_id, stdID)
            if std_id==stdID and name!=None:
                print('return!!: '+str(score))
                return score
