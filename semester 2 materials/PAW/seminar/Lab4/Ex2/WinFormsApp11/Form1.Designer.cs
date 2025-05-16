namespace WinFormsApp11
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
            components = new System.ComponentModel.Container();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            tbLastName = new TextBox();
            tbFirstName = new TextBox();
            tbSSN = new TextBox();
            errorProvider = new ErrorProvider(components);
            checkBox1 = new CheckBox();
            checkBox2 = new CheckBox();
            dateTimePicker1 = new DateTimePicker();
            button1 = new Button();
            backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
            ((System.ComponentModel.ISupportInitialize)errorProvider).BeginInit();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(28, 36);
            label1.Name = "label1";
            label1.Size = new Size(75, 20);
            label1.TabIndex = 0;
            label1.Text = "LastName";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(28, 92);
            label2.Name = "label2";
            label2.Size = new Size(80, 20);
            label2.TabIndex = 1;
            label2.Text = "First Name";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(27, 148);
            label3.Name = "label3";
            label3.Size = new Size(76, 20);
            label3.TabIndex = 2;
            label3.Text = "Birth Date";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(481, 117);
            label4.Name = "label4";
            label4.Size = new Size(36, 20);
            label4.TabIndex = 3;
            label4.Text = "SSN";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(481, 65);
            label5.Name = "label5";
            label5.Size = new Size(57, 20);
            label5.TabIndex = 4;
            label5.Text = "Gender";
            // 
            // tbLastName
            // 
            tbLastName.Location = new Point(158, 42);
            tbLastName.Name = "tbLastName";
            tbLastName.Size = new Size(125, 27);
            tbLastName.TabIndex = 5;
            tbLastName.TextChanged += tbLastName_TextChanged;
            tbLastName.Validating += tbLastName_Validating;
            // 
            // tbFirstName
            // 
            tbFirstName.Location = new Point(158, 92);
            tbFirstName.Name = "tbFirstName";
            tbFirstName.Size = new Size(125, 27);
            tbFirstName.TabIndex = 6;
            tbFirstName.TextChanged += tbFirstName_TextChanged;
            tbFirstName.Validating += tbFirstName_Validating;
            // 
            // tbSSN
            // 
            tbSSN.Location = new Point(547, 114);
            tbSSN.Name = "tbSSN";
            tbSSN.Size = new Size(125, 27);
            tbSSN.TabIndex = 7;
            // 
            // errorProvider
            // 
            errorProvider.ContainerControl = this;
            // 
            // checkBox1
            // 
            checkBox1.AutoSize = true;
            checkBox1.Location = new Point(550, 62);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(64, 24);
            checkBox1.TabIndex = 8;
            checkBox1.Text = "Male";
            checkBox1.UseVisualStyleBackColor = true;
            // 
            // checkBox2
            // 
            checkBox2.AutoSize = true;
            checkBox2.Location = new Point(615, 64);
            checkBox2.Name = "checkBox2";
            checkBox2.Size = new Size(79, 24);
            checkBox2.TabIndex = 9;
            checkBox2.Text = "Female";
            checkBox2.UseVisualStyleBackColor = true;
            // 
            // dateTimePicker1
            // 
            dateTimePicker1.Location = new Point(149, 157);
            dateTimePicker1.Name = "dateTimePicker1";
            dateTimePicker1.Size = new Size(250, 27);
            dateTimePicker1.TabIndex = 10;
            // 
            // button1
            // 
            button1.Location = new Point(484, 193);
            button1.Name = "button1";
            button1.Size = new Size(233, 29);
            button1.TabIndex = 11;
            button1.Text = "Adauga  (づ￣ 3￣)づ";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            AutoValidate = AutoValidate.EnableAllowFocusChange;
            ClientSize = new Size(800, 450);
            Controls.Add(button1);
            Controls.Add(dateTimePicker1);
            Controls.Add(checkBox2);
            Controls.Add(checkBox1);
            Controls.Add(tbSSN);
            Controls.Add(tbFirstName);
            Controls.Add(tbLastName);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Name = "Form1";
            Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)errorProvider).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private TextBox tbLastName;
        private TextBox tbFirstName;
        private TextBox tbSSN;
        private ErrorProvider errorProvider;
        private DateTimePicker dateTimePicker1;
        private CheckBox checkBox2;
        private CheckBox checkBox1;
        private Button button1;
        private System.ComponentModel.BackgroundWorker backgroundWorker1;
    }
}
