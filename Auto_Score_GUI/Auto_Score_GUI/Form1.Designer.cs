namespace Auto_Score_GUI
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.panel1 = new System.Windows.Forms.Panel();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.tb_WaitTime = new System.Windows.Forms.TextBox();
            this.tb_ExcelScore = new System.Windows.Forms.TextBox();
            this.tb_ExcelStdID = new System.Windows.Forms.TextBox();
            this.tb_ExcelPath = new System.Windows.Forms.TextBox();
            this.tb_ClassName = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.tb_Password = new System.Windows.Forms.TextBox();
            this.tb_Account = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.label10);
            this.panel1.Controls.Add(this.button2);
            this.panel1.Controls.Add(this.button1);
            this.panel1.Controls.Add(this.tb_WaitTime);
            this.panel1.Controls.Add(this.tb_ExcelScore);
            this.panel1.Controls.Add(this.tb_ExcelStdID);
            this.panel1.Controls.Add(this.tb_ExcelPath);
            this.panel1.Controls.Add(this.tb_ClassName);
            this.panel1.Controls.Add(this.label9);
            this.panel1.Controls.Add(this.label8);
            this.panel1.Controls.Add(this.label7);
            this.panel1.Controls.Add(this.label6);
            this.panel1.Controls.Add(this.label5);
            this.panel1.Controls.Add(this.label4);
            this.panel1.Controls.Add(this.tb_Password);
            this.panel1.Controls.Add(this.tb_Account);
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.label1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(446, 450);
            this.panel1.TabIndex = 2;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(376, 136);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(67, 22);
            this.button2.TabIndex = 17;
            this.button2.Text = "搜尋路徑";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(23, 267);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(151, 57);
            this.button1.TabIndex = 16;
            this.button1.Text = "執行";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // tb_WaitTime
            // 
            this.tb_WaitTime.Location = new System.Drawing.Point(188, 227);
            this.tb_WaitTime.Name = "tb_WaitTime";
            this.tb_WaitTime.Size = new System.Drawing.Size(40, 22);
            this.tb_WaitTime.TabIndex = 15;
            this.tb_WaitTime.Text = "5";
            // 
            // tb_ExcelScore
            // 
            this.tb_ExcelScore.Location = new System.Drawing.Point(153, 199);
            this.tb_ExcelScore.Name = "tb_ExcelScore";
            this.tb_ExcelScore.Size = new System.Drawing.Size(204, 22);
            this.tb_ExcelScore.TabIndex = 14;
            this.tb_ExcelScore.Text = "最終成績";
            // 
            // tb_ExcelStdID
            // 
            this.tb_ExcelStdID.Location = new System.Drawing.Point(153, 165);
            this.tb_ExcelStdID.Name = "tb_ExcelStdID";
            this.tb_ExcelStdID.Size = new System.Drawing.Size(204, 22);
            this.tb_ExcelStdID.TabIndex = 13;
            this.tb_ExcelStdID.Text = "帳號";
            // 
            // tb_ExcelPath
            // 
            this.tb_ExcelPath.Location = new System.Drawing.Point(92, 137);
            this.tb_ExcelPath.Name = "tb_ExcelPath";
            this.tb_ExcelPath.Size = new System.Drawing.Size(278, 22);
            this.tb_ExcelPath.TabIndex = 12;
            // 
            // tb_ClassName
            // 
            this.tb_ClassName.Location = new System.Drawing.Point(92, 109);
            this.tb_ClassName.Name = "tb_ClassName";
            this.tb_ClassName.Size = new System.Drawing.Size(204, 22);
            this.tb_ClassName.TabIndex = 11;
            this.tb_ClassName.Text = "基礎程式設計";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(21, 230);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(161, 24);
            this.label9.TabIndex = 10;
            this.label9.Text = "登入網頁輸入驗證碼等待秒數\r\n只能輸入正整數";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(21, 202);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(130, 12);
            this.label8.TabIndex = 9;
            this.label8.Text = "Exce最終l成績欄位名稱:";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(21, 172);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(106, 12);
            this.label7.TabIndex = 8;
            this.label7.Text = "Excel學號欄位名稱:";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(21, 144);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(58, 12);
            this.label6.TabIndex = 7;
            this.label6.Text = "Excel路徑:";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(21, 119);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(56, 12);
            this.label5.TabIndex = 6;
            this.label5.Text = "課程名稱:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 98);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(345, 12);
            this.label4.TabIndex = 5;
            this.label4.Text = "---------------------------------------------------------------------------------" +
    "----";
            // 
            // tb_Password
            // 
            this.tb_Password.Location = new System.Drawing.Point(92, 73);
            this.tb_Password.Name = "tb_Password";
            this.tb_Password.PasswordChar = '*';
            this.tb_Password.Size = new System.Drawing.Size(204, 22);
            this.tb_Password.TabIndex = 4;
            // 
            // tb_Account
            // 
            this.tb_Account.Location = new System.Drawing.Point(92, 47);
            this.tb_Account.Name = "tb_Account";
            this.tb_Account.Size = new System.Drawing.Size(204, 22);
            this.tb_Account.TabIndex = 3;
            this.tb_Account.Text = "B03775";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(21, 76);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(68, 12);
            this.label3.TabIndex = 2;
            this.label3.Text = "教職員密碼:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(21, 53);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(68, 12);
            this.label2.TabIndex = 1;
            this.label2.Text = "教職員帳號:";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(21, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(317, 36);
            this.label1.TabIndex = 0;
            this.label1.Text = "作為登入使用，可以不寫，若要自動輸入帳號密碼才需輸入\r\n輸入密碼一定要輸入帳號\r\n可輸入帳帳號，不輸入密碼";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(12, 429);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(133, 12);
            this.label10.TabIndex = 18;
            this.label10.Text = "Made by AWen 2023/6/25 ";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.panel1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox tb_WaitTime;
        private System.Windows.Forms.TextBox tb_ExcelScore;
        private System.Windows.Forms.TextBox tb_ExcelStdID;
        private System.Windows.Forms.TextBox tb_ExcelPath;
        private System.Windows.Forms.TextBox tb_ClassName;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox tb_Password;
        private System.Windows.Forms.TextBox tb_Account;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label label10;
    }
}

