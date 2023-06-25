using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Management.Automation;
using System.Management.Automation.Runspaces;
using System.Threading;

namespace Auto_Score_GUI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
            if (!tb_Password.Text.Equals("") && tb_Account.Text.Equals(""))
            {
                MessageBox.Show("若輸入密碼一定要輸入帳號");
                return;
            }
            if (tb_ClassName.Text.Equals(""))
            {
                MessageBox.Show("課程名稱一定要輸入");
                return;
            }
            if (tb_ExcelPath.Text.Equals(""))
            {
                MessageBox.Show("Excel路徑一定要輸入");
                return;
            }
            if (tb_ExcelStdID.Text.Equals(""))
            {
                MessageBox.Show("Excel學號欄位名稱一定要輸入");
                return;
            }
            if (tb_ExcelScore.Text.Equals(""))
            {
                MessageBox.Show("Excel最終成績欄位名稱一定要輸入");
                return;
            }
            if (tb_WaitTime.Text.Equals(""))
            {
                MessageBox.Show("驗證碼等待秒數一定要輸入");
                return;
            }
           

            string excelColNameStdID = tb_ExcelStdID.Text;
            string excelColNameScore = tb_ExcelScore.Text;
            string waitTime = tb_WaitTime.Text;

            Thread t1 = new Thread(CallPython);
            t1.Start();
           
        }

        private void CallPython()
        {
            string account = tb_Account.Text;
            string passw = tb_Password.Text;
            string className = tb_ClassName.Text;
            string excelPath = tb_ExcelPath.Text;
            string excelColNameStdID = tb_ExcelStdID.Text;
            string excelColNameScore = tb_ExcelScore.Text;
            string waitTime = tb_WaitTime.Text;



            Console.WriteLine("python Auto_Score.py");
            using (PowerShell powershell = PowerShell.Create())
            {
                string script = "python Auto_Score.py "
                    + className + " " + excelPath + " " + excelColNameStdID + " " + excelColNameScore + " " + waitTime + " " + account + " " + passw;
                powershell.AddScript(script);
                powershell.Invoke(); //執行powershell指令

            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            OpenFileDialog dialog = new OpenFileDialog();
            dialog.Title = "Select file";
            dialog.InitialDirectory = ".\\";
            dialog.Filter = "xlsx files (*.xlsx)|*.xlsx|xls files (*.*)|*.xls |csv files (*.csv)|*.csv";
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                tb_ExcelPath.Text= dialog.FileName;
            }
        }
    }
}
