import tkinter as tk
from tkinter.constants import CENTER #加到第一行

from easygui import easygui

from Auto_Score import  Auto_Score
from tkinter import filedialog

root = tk.Tk()
root.title('GUI')
root.geometry('680x400')
root.resizable(True, True)

name_var=tk.StringVar()
passw_var=tk.StringVar()
className_var=tk.StringVar()
excelPath_var=tk.StringVar()
excelColNameStdID_var=tk.StringVar()
excelColNameScore_var=tk.StringVar()
sleep_var=tk.StringVar()

def btn_input_getFileName():
    # file_path = easygui.fileopenbox()
    file_path=filedialog.askopenfile(mode='r')
    print(file_path)
    excelPath_var.set(file_path.name)





remark_label = tk.Label(root, text='作為登入使用，可以不寫，若要自動輸入密碼才需輸入', font=('calibre', 10, 'bold'))
account_label = tk.Label(root, text='Username:', font=('calibre', 10, 'bold'))
account_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

passw_label = tk.Label(root, text='Password:', font=('calibre', 10, 'bold'))
passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

zone_label = tk.Label(root, text='--------------------------------------------------------------------------------------------------------', font=('calibre', 10, 'bold'))

remark_label.grid(row=0,column=0,columnspan=3)
account_label.grid(row=1,column=0)
account_entry.grid(row=1,column=1)
passw_label.grid(row=2,column=0)
passw_entry.grid(row=2,column=1)
zone_label.grid(row=3,column=0,columnspan=3)

className_label = tk.Label(root, text='課程名稱:', font=('calibre', 10, 'bold'))
className_entry = tk.Entry(root, textvariable=className_var, font=('calibre', 10, 'normal'))

excelPath_label = tk.Label(root, text='excel路徑:', font=('calibre', 10, 'bold'))
excelPath_entry = tk.Entry(root, textvariable=excelPath_var, font=('calibre', 10, 'normal'))
excelPath_entry.config(width='40')
getFileName_button = tk.Button(root, text='尋找檔案',command=btn_input_getFileName)

excelColNameStdID_var.set('帳號')
excelColNameStdID_label = tk.Label(root, text='excel 學號欄位名稱:', font=('calibre', 10, 'bold'))
excelColNameStdID_entry = tk.Entry(root, textvariable=excelColNameStdID_var, font=('calibre', 10, 'normal'))

excelColNameScore_var.set('學號')
excelColNameScore_label = tk.Label(root, text='excel 成績欄位名稱:', font=('calibre', 10, 'bold'),wraplength=150)
excelColNameScore_entry = tk.Entry(root, textvariable=excelColNameScore_var, font=('calibre', 10, 'normal'))

sleep_var='10'
sleep_label = tk.Label(root, text='登入網頁等待秒數 只能輸入正整數:', font=('calibre', 10, 'bold'),wraplength=150)
sleep_entry = tk.Entry(root, textvariable=sleep_var, font=('calibre', 10, 'normal'))


className_label.grid(row=4,column=0)
className_entry.grid(row=4,column=1)
excelPath_label.grid(row=5,column=0)
excelPath_entry.grid(row=5,column=1,columnspan=2)
getFileName_button.grid(row=5,column=3)
excelColNameStdID_label.grid(row=6,column=0)
excelColNameStdID_entry.grid(row=6,column=1)
excelColNameScore_label.grid(row=7,column=0)
excelColNameScore_entry.grid(row=7,column=1)
sleep_label.grid(row=8,column=0)
sleep_entry.grid(row=8,column=1)

global account,passw,className,excelPath,excelColNameStdID,excelColNameScore
account=account_entry.get()
passw = passw_entry.get()
className = className_entry.get()
excelPath = excelPath_entry.get()
excelColNameStdID = excelColNameStdID_entry.get()
excelColNameScore =excelColNameScore_entry.get()





def Go():
    auto=Auto_Score(account,passw,className,excelPath,excelColNameStdID,excelColNameScore)


mybutton = tk.Button(root, text='執行',command=Go)
mybutton.config(width='20',height='2')
mybutton.grid(row=9,column=0,columnspan=1,rowspan=2)




root.mainloop()