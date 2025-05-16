namespace MouseEvents
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            tbValue1 = new TextBox();
            tbValue2 = new TextBox();
            tbResult = new TextBox();
            label1 = new Label();
            label2 = new Label();
            button1 = new Button();
            SuspendLayout();
            // 
            // tbValue1
            // 
            tbValue1.BackColor = Color.Blue;
            tbValue1.ForeColor = Color.Yellow;
            tbValue1.Location = new Point(154, 121);
            tbValue1.Name = "tbValue1";
            tbValue1.Size = new Size(47, 27);
            tbValue1.TabIndex = 0;
            tbValue1.TextChanged += tbNumericTextBox_TextChanged;
            tbValue1.KeyPress += tbNumericTextBox_KeyPress;
            // 
            // tbValue2
            // 
            tbValue2.BackColor = Color.Yellow;
            tbValue2.ForeColor = Color.Red;
            tbValue2.Location = new Point(242, 121);
            tbValue2.Name = "tbValue2";
            tbValue2.Size = new Size(47, 27);
            tbValue2.TabIndex = 1;
            tbValue2.TextChanged += textBox1_TextChanged;
            tbValue2.KeyPress += textBox1_KeyPress;
            // 
            // tbResult
            // 
            tbResult.BackColor = Color.Red;
            tbResult.ForeColor = Color.Blue;
            tbResult.Location = new Point(320, 121);
            tbResult.Name = "tbResult";
            tbResult.Size = new Size(47, 27);
            tbResult.TabIndex = 2;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(207, 124);
            label1.Name = "label1";
            label1.Size = new Size(19, 20);
            label1.TabIndex = 3;
            label1.Text = "+";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(295, 124);
            label2.Name = "label2";
            label2.Size = new Size(19, 20);
            label2.TabIndex = 4;
            label2.Text = "=";
            // 
            // button1
            // 
            button1.BackColor = Color.Fuchsia;
            button1.ForeColor = SystemColors.ButtonFace;
            button1.Location = new Point(471, 121);
            button1.Name = "button1";
            button1.Size = new Size(189, 29);
            button1.TabIndex = 5;
            button1.Text = "CALCULEAZA(≧▽≦q)";
            button1.UseVisualStyleBackColor = false;
            button1.Click += button1_Click;
            button1.Enter += button1_Enter;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(button1);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(tbResult);
            Controls.Add(tbValue2);
            Controls.Add(tbValue1);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox tbValue1;
        private TextBox tbValue2;
        private TextBox tbResult;
        private Label label1;
        private Label label2;
        private Button button1;
    }
}
