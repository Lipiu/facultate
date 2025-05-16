namespace model1
{
    partial class Form2
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
            btnAddWaiter = new Button();
            textBoxName = new TextBox();
            textBoxAge = new TextBox();
            textBoxID = new TextBox();
            errorProvider1 = new ErrorProvider(components);
            textBox1 = new TextBox();
            textBox2 = new TextBox();
            textBox3 = new TextBox();
            ((System.ComponentModel.ISupportInitialize)errorProvider1).BeginInit();
            SuspendLayout();
            // 
            // btnAddWaiter
            // 
            btnAddWaiter.Location = new Point(190, 268);
            btnAddWaiter.Name = "btnAddWaiter";
            btnAddWaiter.Size = new Size(94, 29);
            btnAddWaiter.TabIndex = 1;
            btnAddWaiter.Text = "Add waiter";
            btnAddWaiter.UseVisualStyleBackColor = true;
            btnAddWaiter.Click += btnAddWaiter_Click;
            // 
            // textBoxName
            // 
            textBoxName.Location = new Point(190, 87);
            textBoxName.Name = "textBoxName";
            textBoxName.Size = new Size(125, 27);
            textBoxName.TabIndex = 2;
            // 
            // textBoxAge
            // 
            textBoxAge.Location = new Point(190, 145);
            textBoxAge.Name = "textBoxAge";
            textBoxAge.Size = new Size(125, 27);
            textBoxAge.TabIndex = 3;
            // 
            // textBoxID
            // 
            textBoxID.Location = new Point(190, 197);
            textBoxID.Name = "textBoxID";
            textBoxID.Size = new Size(125, 27);
            textBoxID.TabIndex = 4;
            // 
            // errorProvider1
            // 
            errorProvider1.ContainerControl = this;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(133, 87);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(51, 27);
            textBox1.TabIndex = 5;
            textBox1.Text = "Name";
            // 
            // textBox2
            // 
            textBox2.Location = new Point(133, 197);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(51, 27);
            textBox2.TabIndex = 6;
            textBox2.Text = "ID";
            // 
            // textBox3
            // 
            textBox3.Location = new Point(133, 145);
            textBox3.Name = "textBox3";
            textBox3.Size = new Size(51, 27);
            textBox3.TabIndex = 7;
            textBox3.Text = "Age";
            textBox3.TextChanged += textBox3_TextChanged;
            // 
            // Form2
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(textBox3);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            Controls.Add(textBoxID);
            Controls.Add(textBoxAge);
            Controls.Add(textBoxName);
            Controls.Add(btnAddWaiter);
            Name = "Form2";
            Text = "Form2";
            Load += Form2_Load;
            ((System.ComponentModel.ISupportInitialize)errorProvider1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private Button btnAddWaiter;
        private TextBox textBoxName;
        private TextBox textBoxAge;
        private TextBox textBoxID;
        private ErrorProvider errorProvider1;
        private TextBox textBox3;
        private TextBox textBox2;
        private TextBox textBox1;
    }
}