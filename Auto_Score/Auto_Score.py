from ReadScoreFromExcel import RSFE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class Auto_Score:


    def __init__(self,account,password,selectClassName,excelPath,excelColIDName,excelColScoreName,waitTime):
        self.account = account
        self.pas = password
        self.scoreExcelPath = excelPath  # 選擇的excel資料路徑
        self.selectClassName = selectClassName  # 要選擇的課程名稱(部分即可) 要和網頁上的相同
        self.excelColIDName=excelColIDName #要讀取的成績欄位名稱
        self.excelColScoreName=excelColScoreName
        self.waitTime=waitTime
        self.Run()

    def getScoreFromExcel(self,stdID):
        data = RSFE(self.scoreExcelPath,self.excelColIDName,self.excelColScoreName)
        return data.getScore(stdID)

    def Run(self):
        # account = open('account.txt', 'r').readline();
        # pas=open('password.txt', 'r').readline();

        driver = webdriver.Chrome()
        driver.get('https://teachinfo.must.edu.tw/')


        username = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.NAME, "EMPNO"))
        )

        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "PASSWD"))
        )





        login = driver.find_element(by=By.CLASS_NAME, value="genform")
        username.clear()
        password.clear()
        username.send_keys(self.account)
        password.send_keys(self.pas)
        time.sleep(int(self.waitTime)) #怕輸入驗證碼太慢所以等待
        login.click()

        time.sleep(1)
        driver.get('https://teachinfo.must.edu.tw/scrinput/smtr_cos_list.asp')
        # driver.get('https://teachinfo.must.edu.tw/LoginGo.asp')

        for i in range(1,10): #期末成績
            url='/html/body/form[2]/center[2]/b/p/table/tbody/tr/td[2]/select/option['+str(i)+']'
            classItme = driver.find_element(by=By.XPATH, value=url)
            if self.selectClassName in classItme.text:
                print(classItme.text)
                classItme.click()
                break

        # for i in range(1,10): #期中成績
        #     url='/html/body/form[2]/center[2]/b/table/tbody/tr/td[2]/select/option['+str(i)+']'
        #     classItme = driver.find_element(by=By.XPATH, value=url)
        #     if self.selectClassName in classItme.text:
        #         print(classItme.text)
        #         classItme.click()
        #         break


        input_select_Button = driver.find_element(by=By.XPATH,value='/html/body/form[2]/center[2]/b/p/table/tbody/tr/td[3]/input') #輸入/查詢成績
        input_select_Button.click()
        main_table = driver.find_element(By.TAG_NAME,'table')

        print(main_table.text)


        trs = main_table.find_elements(By.TAG_NAME,'tr')
        print(len(trs))



        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME, 'td')
            print(tds[1].text)
            print(tds[2].text)
            if tds[1].text=='學號':
                continue
            score=self.getScoreFromExcel(tds[1].text)
            print('輸入:'+str(score))
            for td in tds:
                try:
                    input = tr.find_element(By.TAG_NAME, 'input')
                    input.send_keys(int(score))
                except:
                    print('again')
                break
        time.sleep(1800)



#sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]
#'','視窗程式設計','D:\\111_2.xlsx','帳號','最終成績'
account, password='',''
if len(sys.argv)-1 ==5:
    className,excelPath,excelColNameStdID,excelColNameScore,waitTime=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]
elif len(sys.argv)-1 ==6:
    className, excelPath, excelColNameStdID, excelColNameScore, waitTime, account = sys.argv[1], sys.argv[2], \
                                                                                           sys.argv[3], sys.argv[4], \
                                                                                           sys.argv[5], sys.argv[6]

elif len(sys.argv)-1 ==7:
    className, excelPath, excelColNameStdID, excelColNameScore, waitTime, account, password = sys.argv[1], sys.argv[2], \
                                                                                           sys.argv[3], sys.argv[4], \
                                                                                           sys.argv[5], sys.argv[6], \
                                                                                           sys.argv[7]

auto=Auto_Score(account,password,className,excelPath,excelColNameStdID,excelColNameScore,waitTime)
