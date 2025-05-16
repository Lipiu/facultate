namespace WinFormsApp10
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
            tbValue2 = new TextBox();
            tbValue1 = new TextBox();
            backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
            tbResult = new TextBox();
            Calculate = new Button();
            label1 = new Label();
            label2 = new Label();
            SuspendLayout();
            // 
            // tbValue2
            // 
            tbValue2.Location = new Point(361, 118);
            tbValue2.Name = "tbValue2";
            tbValue2.Size = new Size(125, 27);
            tbValue2.TabIndex = 2;
            // 
            // tbValue1
            // 
            tbValue1.Location = new Point(54, 118);
            tbValue1.Name = "tbValue1";
            tbValue1.Size = new Size(125, 27);
            tbValue1.TabIndex = 3;
            // 
            // tbResult
            // 
            tbResult.Location = new Point(634, 115);
            tbResult.Name = "tbResult";
            tbResult.Size = new Size(125, 27);
            tbResult.TabIndex = 4;
            // 
            // Calculate
            // 
            Calculate.Location = new Point(521, 195);
            Calculate.Name = "Calculate";
            Calculate.Size = new Size(238, 29);
            Calculate.TabIndex = 6;
            Calculate.Text = "GHICESTE CE O SA SE INTAMPLE";
            Calculate.UseVisualStyleBackColor = true;
            Calculate.Click += btnCalculate_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(247, 123);
            label1.Name = "label1";
            label1.Size = new Size(15, 20);
            label1.TabIndex = 7;
            label1.Text = "/";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(566, 118);
            label2.Name = "label2";
            label2.Size = new Size(19, 20);
            label2.TabIndex = 8;
            label2.Text = "=";
            label2.Click += label2_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(Calculate);
            Controls.Add(tbResult);
            Controls.Add(tbValue1);
            Controls.Add(tbValue2);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private TextBox tbValue2;
        private TextBox tbValue1;
        private System.ComponentModel.BackgroundWorker backgroundWorker1;
        private TextBox tbResult;
        private Label label1;
        private Button Calculate;
        private Label label2;
    }
}
