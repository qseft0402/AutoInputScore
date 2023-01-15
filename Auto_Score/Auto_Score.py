from ReadScoreFromExcel import RSFE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

scoreExcelPath='N:\\明新上課\\課程\\ProBuilder\\成績\\test.xlsx' #選擇的excel資料路徑
selectClassName='物件導向'   #要選擇的課程名稱(部分即可) 要和網頁上的相同

def getScoreFromExcel(stdID):
    data = RSFE(scoreExcelPath)
    return data.getScore(stdID)


account = open('account.txt', 'r').readline();
pas=open('password.txt', 'r').readline();

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
username.send_keys(account)
password.send_keys(pas)
time.sleep(5)
login.click()

time.sleep(1)
driver.get('https://teachinfo.must.edu.tw/scrinput/smtr_cos_list.asp')

for i in range(1,10):
    url='/html/body/form[2]/center[2]/b/p/table/tbody/tr/td[2]/select/option['+str(i)+']'
    classItme = driver.find_element(by=By.XPATH, value=url)
    if selectClassName in classItme.text:
        print(classItme.text)
        classItme.click()
        break


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
    score=getScoreFromExcel(tds[1].text)
    print('輸入:'+str(score))
    for td in tds:
        try:
            input = tr.find_element(By.TAG_NAME, 'input')
            input.send_keys(int(score))
        except:
            print('again')
        break

time.sleep(100000)