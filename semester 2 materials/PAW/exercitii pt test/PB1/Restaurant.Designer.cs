namespace PB1
{
    partial class Restaurant
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
            btn_add = new Button();
            btn_edit = new Button();
            lvWaiters = new ListView();
            columnHeader1 = new ColumnHeader();
            columnHeader2 = new ColumnHeader();
            columnHeader3 = new ColumnHeader();
            btnSortByBirthDate = new Button();
            SuspendLayout();
            // 
            // btn_add
            // 
            btn_add.Location = new Point(61, 196);
            btn_add.Name = "btn_add";
            btn_add.Size = new Size(170, 58);
            btn_add.TabIndex = 0;
            btn_add.Text = "ADD";
            btn_add.UseVisualStyleBackColor = true;
            btn_add.Click += btnAddParticipant_Click;
            // 
            // btn_edit
            // 
            btn_edit.Location = new Point(267, 196);
            btn_edit.Name = "btn_edit";
            btn_edit.Size = new Size(176, 58);
            btn_edit.TabIndex = 1;
            btn_edit.Text = "EDIT";
            btn_edit.UseVisualStyleBackColor = true;
            // 
            // lvWaiters
            // 
            lvWaiters.Columns.AddRange(new ColumnHeader[] { columnHeader1, columnHeader2, columnHeader3 });
            lvWaiters.Location = new Point(12, 277);
            lvWaiters.Name = "lvWaiters";
            lvWaiters.Size = new Size(776, 161);
            lvWaiters.TabIndex = 2;
            lvWaiters.UseCompatibleStateImageBehavior = false;
            lvWaiters.View = View.Details;
            // 
            // columnHeader1
            // 
            columnHeader1.Text = "First Name";
            columnHeader1.Width = 150;
            // 
            // columnHeader2
            // 
            columnHeader2.Text = "Last Name";
            columnHeader2.Width = 150;
            // 
            // columnHeader3
            // 
            columnHeader3.Text = "Birth Date";
            columnHeader3.Width = 150;
            // 
            // btnSortByBirthDate
            // 
            btnSortByBirthDate.Location = new Point(502, 199);
            btnSortByBirthDate.Name = "btnSortByBirthDate";
            btnSortByBirthDate.Size = new Size(175, 52);
            btnSortByBirthDate.TabIndex = 3;
            btnSortByBirthDate.Text = "Sort";
            btnSortByBirthDate.UseVisualStyleBackColor = true;
            btnSortByBirthDate.Click += btnSortByBirthDate_Click;
            // 
            // Restaurant
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(btnSortByBirthDate);
            Controls.Add(lvWaiters);
            Controls.Add(btn_edit);
            Controls.Add(btn_add);
            Name = "Restaurant";
            Text = "Form1";
            ResumeLayout(false);
        }

        #endregion

        private Button btn_add;
        private Button btn_edit;
        private ListView lvWaiters;
        private ColumnHeader columnHeader1;
        private ColumnHeader columnHeader2;
        private ColumnHeader columnHeader3;
        private Button btnSortByBirthDate;
    }
}
