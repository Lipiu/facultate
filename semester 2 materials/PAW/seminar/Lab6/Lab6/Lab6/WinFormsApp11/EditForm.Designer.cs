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
            dtpBirthDate = new DateTimePicker();
            labelLastName = new Label();
            labelFirstName = new Label();
            tbBirthDate = new Label();
            buttonOk = new Button();
            buttonCancel = new Button();
            SuspendLayout();
            // 
            // tbFirstName
            // 
            tbFirstName.BackColor = Color.DarkOrchid;
            tbFirstName.ForeColor = SystemColors.Window;
            tbFirstName.Location = new Point(122, 132);
            tbFirstName.Name = "tbFirstName";
            tbFirstName.Size = new Size(125, 27);
            tbFirstName.TabIndex = 6;
            // 
            // tbLastName
            // 
            tbLastName.BackColor = Color.DarkOrchid;
            tbLastName.ForeColor = SystemColors.Window;
            tbLastName.Location = new Point(122, 61);
            tbLastName.Name = "tbLastName";
            tbLastName.Size = new Size(125, 27);
            tbLastName.TabIndex = 7;
            // 
            // dtpBirthDate
            // 
            dtpBirthDate.CalendarMonthBackground = Color.DarkOrchid;
            dtpBirthDate.CalendarTitleBackColor = Color.DarkOrchid;
            dtpBirthDate.CalendarTitleForeColor = Color.DarkOrchid;
            dtpBirthDate.CalendarTrailingForeColor = Color.DarkOrchid;
            dtpBirthDate.Location = new Point(122, 232);
            dtpBirthDate.Name = "dtpBirthDate";
            dtpBirthDate.Size = new Size(250, 27);
            dtpBirthDate.TabIndex = 8;
            // 
            // labelLastName
            // 
            labelLastName.AutoSize = true;
            labelLastName.Location = new Point(12, 59);
            labelLastName.Name = "labelLastName";
            labelLastName.Size = new Size(75, 20);
            labelLastName.TabIndex = 9;
            labelLastName.Text = "LastName";
            // 
            // labelFirstName
            // 
            labelFirstName.AutoSize = true;
            labelFirstName.Location = new Point(12, 132);
            labelFirstName.Name = "labelFirstName";
            labelFirstName.Size = new Size(80, 20);
            labelFirstName.TabIndex = 10;
            labelFirstName.Text = "First Name";
            labelFirstName.Click += labelFirstName_Click;
            // 
            // tbBirthDate
            // 
            tbBirthDate.AutoSize = true;
            tbBirthDate.Location = new Point(12, 232);
            tbBirthDate.Name = "tbBirthDate";
            tbBirthDate.Size = new Size(76, 20);
            tbBirthDate.TabIndex = 11;
            tbBirthDate.Text = "Birth Date";
            // 
            // buttonOk
            // 
            buttonOk.BackColor = Color.OrangeRed;
            buttonOk.DialogResult = DialogResult.OK;
            buttonOk.ForeColor = SystemColors.ControlLightLight;
            buttonOk.Location = new Point(122, 308);
            buttonOk.Name = "buttonOk";
            buttonOk.Size = new Size(94, 29);
            buttonOk.TabIndex = 12;
            buttonOk.Text = "Ok(⊙_⊙)？";
            buttonOk.UseVisualStyleBackColor = false;
            buttonOk.Click += button1_Click;
            // 
            // buttonCancel
            // 
            buttonCancel.BackColor = Color.LightPink;
            buttonCancel.DialogResult = DialogResult.Cancel;
            buttonCancel.ForeColor = SystemColors.WindowText;
            buttonCancel.Location = new Point(264, 308);
            buttonCancel.Name = "buttonCancel";
            buttonCancel.Size = new Size(108, 29);
            buttonCancel.TabIndex = 13;
            buttonCancel.Text = "Cancel(╯︿╰)";
            buttonCancel.UseVisualStyleBackColor = false;
            // 
            // EditForm
            // 
            AcceptButton = buttonOk;
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            CancelButton = buttonCancel;
            ClientSize = new Size(800, 450);
            Controls.Add(buttonCancel);
            Controls.Add(buttonOk);
            Controls.Add(tbBirthDate);
            Controls.Add(labelFirstName);
            Controls.Add(labelLastName);
            Controls.Add(dtpBirthDate);
            Controls.Add(tbLastName);
            Controls.Add(tbFirstName);
            Name = "EditForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "Form2";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox tbFirstName;
        private TextBox tbLastName;
        private DateTimePicker dtpBirthDate;
        private Label labelLastName;
        private Label labelFirstName;
        private Label tbBirthDate;
        private Button buttonOk;
        private Button buttonCancel;
    }
}