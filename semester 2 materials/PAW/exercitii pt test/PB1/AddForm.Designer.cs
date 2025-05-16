namespace PB1
{
    partial class AddForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            button1 = new Button();
            button2 = new Button();
            dtpBirthDate = new DateTimePicker();
            tbLastName = new TextBox();
            tbFirstName = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            errorProvider = new ErrorProvider(components);
            ((System.ComponentModel.ISupportInitialize)errorProvider).BeginInit();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Location = new Point(169, 268);
            button1.Name = "button1";
            button1.Size = new Size(149, 39);
            button1.TabIndex = 0;
            button1.Text = "OK";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Location = new Point(418, 262);
            button2.Name = "button2";
            button2.Size = new Size(167, 46);
            button2.TabIndex = 1;
            button2.Text = "Cancel";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // dtpBirthDate
            // 
            dtpBirthDate.Location = new Point(300, 177);
            dtpBirthDate.Name = "dtpBirthDate";
            dtpBirthDate.Size = new Size(265, 27);
            dtpBirthDate.TabIndex = 2;
            dtpBirthDate.Validating += dtpBirthDate_Validating;
            // 
            // tbLastName
            // 
            tbLastName.Location = new Point(300, 130);
            tbLastName.Name = "tbLastName";
            tbLastName.Size = new Size(272, 27);
            tbLastName.TabIndex = 4;
            tbLastName.Validating += tbLastName_Validating;
            // 
            // tbFirstName
            // 
            tbFirstName.Location = new Point(303, 84);
            tbFirstName.Name = "tbFirstName";
            tbFirstName.Size = new Size(267, 27);
            tbFirstName.TabIndex = 5;
            tbFirstName.Validating += tbFirstName_Validating;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(155, 91);
            label1.Name = "label1";
            label1.Size = new Size(80, 20);
            label1.TabIndex = 6;
            label1.Text = "First Name";
            label1.Click += label1_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(155, 130);
            label2.Name = "label2";
            label2.Size = new Size(79, 20);
            label2.TabIndex = 7;
            label2.Text = "Last Name";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(155, 184);
            label3.Name = "label3";
            label3.Size = new Size(76, 20);
            label3.TabIndex = 8;
            label3.Text = "Birth Date";
            // 
            // errorProvider
            // 
            errorProvider.ContainerControl = this;
            // 
            // AddForm
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(tbFirstName);
            Controls.Add(tbLastName);
            Controls.Add(dtpBirthDate);
            Controls.Add(button2);
            Controls.Add(button1);
            Name = "AddForm";
            Text = "AddForm";
            Load += AddForm_Load;
            ((System.ComponentModel.ISupportInitialize)errorProvider).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button button1;
        private Button button2;
        private DateTimePicker dtpBirthDate;
        private TextBox tbLastName;
        private TextBox tbFirstName;
        private Label label1;
        private Label label2;
        private Label label3;
        private ErrorProvider errorProvider;
    }
}