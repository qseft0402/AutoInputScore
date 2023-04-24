from ReadScoreFromExcel import RSFE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Auto_Score:


    def __init__(self,account,password,selectClassName,excelPath,excelColIDName,excelColScoreName):
        self.account = account
        self.pas = password
        self.scoreExcelPath = excelPath  # 選擇的excel資料路徑
        self.selectClassName = selectClassName  # 要選擇的課程名稱(部分即可) 要和網頁上的相同
        self.excelColIDName=excelColIDName #要讀取的成績欄位名稱
        self.excelColScoreName=excelColScoreName
        self.Run()

    def getScoreFromExcel(self,stdID):
        data = RSFE(self.scoreExcelPath)
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
        time.sleep(5)
        login.click()

        time.sleep(1)
        driver.get('https://teachinfo.must.edu.tw/scrinput/smtr_cos_list.asp')
        # driver.get('https://teachinfo.must.edu.tw/LoginGo.asp')

        # for i in range(1,10): #期末成績
        #     url='/html/body/form[2]/center[2]/b/p/table/tbody/tr/td[2]/select/option['+str(i)+']'
        #     classItme = driver.find_element(by=By.XPATH, value=url)
        #     if self.selectClassName in classItme.text:
        #         print(classItme.text)
        #         classItme.click()
        #         break

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
