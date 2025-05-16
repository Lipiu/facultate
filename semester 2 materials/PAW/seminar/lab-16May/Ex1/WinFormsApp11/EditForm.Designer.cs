namespace WinFormsApp11
{
    partial class EditForm
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
            tbFirstName = new TextBox();
            tbLastName = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            dtpBirthDate = new DateTimePicker();
            btnOk = new Button();
            btnCancel = new Button();
            SuspendLayout();
            // 
            // tbFirstName
            // 
            tbFirstName.Location = new Point(323, 60);
            tbFirstName.Name = "tbFirstName";
            tbFirstName.Size = new Size(125, 27);
            tbFirstName.TabIndex = 0;
            // 
            // tbLastName
            // 
            tbLastName.Location = new Point(323, 137);
            tbLastName.Name = "tbLastName";
            tbLastName.Size = new Size(125, 27);
            tbLastName.TabIndex = 1;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(203, 63);
            label1.Name = "label1";
            label1.Size = new Size(74, 20);
            label1.TabIndex = 2;
            label1.Text = "firstName";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(205, 140);
            label2.Name = "label2";
            label2.Size = new Size(72, 20);
            label2.TabIndex = 3;
            label2.Text = "lastName";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(205, 211);
            label3.Name = "label3";
            label3.Size = new Size(72, 20);
            label3.TabIndex = 4;
            label3.Text = "BirthDate";
            // 
            // dtpBirthDate
            // 
            dtpBirthDate.Location = new Point(323, 211);
            dtpBirthDate.Name = "dtpBirthDate";
            dtpBirthDate.Size = new Size(250, 27);
            dtpBirthDate.TabIndex = 5;
            // 
            // btnOk
            // 
            btnOk.DialogResult = DialogResult.OK;
            btnOk.Location = new Point(374, 309);
            btnOk.Name = "btnOk";
            btnOk.Size = new Size(94, 29);
            btnOk.TabIndex = 6;
            btnOk.Text = "OK";
            btnOk.UseVisualStyleBackColor = true;
            btnOk.Click += btnOk_Click;
            // 
            // btnCancel
            // 
            btnCancel.DialogResult = DialogResult.Cancel;
            btnCancel.Location = new Point(586, 309);
            btnCancel.Name = "btnCancel";
            btnCancel.Size = new Size(94, 29);
            btnCancel.TabIndex = 7;
            btnCancel.Text = "Cancel";
            btnCancel.UseVisualStyleBackColor = true;
            // 
            // EditForm
            // 
            AcceptButton = btnOk;
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            CancelButton = btnCancel;
            ClientSize = new Size(800, 450);
            Controls.Add(btnCancel);
            Controls.Add(btnOk);
            Controls.Add(dtpBirthDate);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(tbLastName);
            Controls.Add(tbFirstName);
            Name = "EditForm";
            ShowInTaskbar = false;
            StartPosition = FormStartPosition.CenterParent;
            Text = "Form2";
            Load += EditForm_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox tbFirstName;
        private TextBox tbLastName;
        private Label label1;
        private Label label2;
        private Label label3;
        private DateTimePicker dtpBirthDate;
        private Button btnOk;
        private Button btnCancel;
    }
}