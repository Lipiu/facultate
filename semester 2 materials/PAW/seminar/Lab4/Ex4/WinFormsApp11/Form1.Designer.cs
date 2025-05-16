namespace WinFormsApp11
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;


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
            ListViewGroup listViewGroup1 = new ListViewGroup("ListViewGroup", HorizontalAlignment.Left);
            ListViewItem listViewItem1 = new ListViewItem("");
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            tbLastName = new TextBox();
            tbFirstName = new TextBox();
            errorProvider = new ErrorProvider(components);
            dtpBirthDate = new DateTimePicker();
            button1 = new Button();
            lvParticipants = new ListView();
            LastName = new ColumnHeader();
            FirstName = new ColumnHeader();
            BirthDate = new ColumnHeader();
            ((System.ComponentModel.ISupportInitialize)errorProvider).BeginInit();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(27, 42);
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
            // tbLastName
            // 
            tbLastName.Location = new Point(158, 42);
            tbLastName.Name = "tbLastName";
            tbLastName.Size = new Size(125, 27);
            tbLastName.TabIndex = 5;
            tbLastName.TextChanged += tbLastName_TextChanged;
            tbLastName.Validating += tbLastName_Validating;
            tbLastName.Validated += tbLastName_Validated;
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
            // errorProvider
            // 
            errorProvider.ContainerControl = this;
            // 
            // dtpBirthDate
            // 
            dtpBirthDate.Location = new Point(149, 157);
            dtpBirthDate.Name = "dtpBirthDate";
            dtpBirthDate.Size = new Size(250, 27);
            dtpBirthDate.TabIndex = 10;
            // 
            // button1
            // 
            button1.Location = new Point(484, 193);
            button1.Name = "button1";
            button1.Size = new Size(233, 29);
            button1.TabIndex = 11;
            button1.Text = "Add Participants";
            button1.UseVisualStyleBackColor = true;
            button1.Click += btnAdd_Click;
            // 
            // lvParticipants
            // 
            lvParticipants.Columns.AddRange(new ColumnHeader[] { LastName, FirstName, BirthDate });
            listViewGroup1.Header = "ListViewGroup";
            listViewGroup1.Name = "listViewGroup1";
            lvParticipants.Groups.AddRange(new ListViewGroup[] { listViewGroup1 });
            lvParticipants.Items.AddRange(new ListViewItem[] { listViewItem1 });
            lvParticipants.Location = new Point(27, 267);
            lvParticipants.Name = "lvParticipants";
            lvParticipants.Size = new Size(539, 117);
            lvParticipants.TabIndex = 12;
            lvParticipants.UseCompatibleStateImageBehavior = false;
            lvParticipants.View = View.Details;
            lvParticipants.SelectedIndexChanged += listView1_SelectedIndexChanged;
            // 
            // LastName
            // 
            LastName.Text = "LastName";
            // 
            // FirstName
            // 
            FirstName.Text = "FirstName";
            // 
            // BirthDate
            // 
            BirthDate.Text = "BirthDate";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            AutoValidate = AutoValidate.EnableAllowFocusChange;
            ClientSize = new Size(800, 450);
            Controls.Add(lvParticipants);
            Controls.Add(button1);
            Controls.Add(dtpBirthDate);
            Controls.Add(tbFirstName);
            Controls.Add(tbLastName);
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
        private TextBox tbLastName;
        private TextBox tbFirstName;
        private ErrorProvider errorProvider;
        private DateTimePicker dtpBirthDate;
        private Button button1;
        private ListView lvParticipants;
        private ColumnHeader LastName;
        private ColumnHeader FirstName;
        private ColumnHeader BirthDate;
    }
}
