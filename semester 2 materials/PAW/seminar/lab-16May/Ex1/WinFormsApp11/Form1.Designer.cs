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
            menuStrip1 = new MenuStrip();
            BinarySerialization = new ToolStripMenuItem();
            btnSerializeBinary = new ToolStripMenuItem();
            btnDeserializeBinary = new ToolStripMenuItem();
            XMLSerialization = new ToolStripMenuItem();
            btnSerializeXML = new ToolStripMenuItem();
            btnDeserializeXML = new ToolStripMenuItem();
            jSONSerializationToolStripMenuItem = new ToolStripMenuItem();
            serializeToolStripMenuItem2 = new ToolStripMenuItem();
            deserializeToolStripMenuItem2 = new ToolStripMenuItem();
            TextFile = new ToolStripMenuItem();
            btnExport = new ToolStripMenuItem();
            contextMenuStrip1 = new ContextMenuStrip(components);
            btnEdit = new Button();
            btnDelete = new Button();
            ((System.ComponentModel.ISupportInitialize)errorProvider).BeginInit();
            menuStrip1.SuspendLayout();
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
            // menuStrip1
            // 
            menuStrip1.ImageScalingSize = new Size(20, 20);
            menuStrip1.Items.AddRange(new ToolStripItem[] { BinarySerialization, XMLSerialization, jSONSerializationToolStripMenuItem, TextFile });
            menuStrip1.Location = new Point(0, 0);
            menuStrip1.Name = "menuStrip1";
            menuStrip1.Size = new Size(800, 28);
            menuStrip1.TabIndex = 13;
            menuStrip1.Text = "menuStrip1";
            // 
            // BinarySerialization
            // 
            BinarySerialization.DropDownItems.AddRange(new ToolStripItem[] { btnSerializeBinary, btnDeserializeBinary });
            BinarySerialization.Name = "BinarySerialization";
            BinarySerialization.Size = new Size(146, 24);
            BinarySerialization.Text = "BinarySerialization";
            // 
            // btnSerializeBinary
            // 
            btnSerializeBinary.Name = "btnSerializeBinary";
            btnSerializeBinary.Size = new Size(165, 26);
            btnSerializeBinary.Text = "Serialize";
            btnSerializeBinary.Click += btnSerializeBinary_Click;
            // 
            // btnDeserializeBinary
            // 
            btnDeserializeBinary.Name = "btnDeserializeBinary";
            btnDeserializeBinary.Size = new Size(165, 26);
            btnDeserializeBinary.Text = "Deserialize";
            btnDeserializeBinary.Click += btnDeserializeBinary_Click;
            // 
            // XMLSerialization
            // 
            XMLSerialization.DropDownItems.AddRange(new ToolStripItem[] { btnSerializeXML, btnDeserializeXML });
            XMLSerialization.Name = "XMLSerialization";
            XMLSerialization.Size = new Size(134, 24);
            XMLSerialization.Text = "XMLSerialization";
            // 
            // btnSerializeXML
            // 
            btnSerializeXML.Name = "btnSerializeXML";
            btnSerializeXML.Size = new Size(165, 26);
            btnSerializeXML.Text = "Serialize";
            btnSerializeXML.Click += btnSerializeXML_Click;
            // 
            // btnDeserializeXML
            // 
            btnDeserializeXML.Name = "btnDeserializeXML";
            btnDeserializeXML.Size = new Size(165, 26);
            btnDeserializeXML.Text = "Deserialize";
            btnDeserializeXML.Click += btnDeserializeXML_Click;
            // 
            // jSONSerializationToolStripMenuItem
            // 
            jSONSerializationToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { serializeToolStripMenuItem2, deserializeToolStripMenuItem2 });
            jSONSerializationToolStripMenuItem.Name = "jSONSerializationToolStripMenuItem";
            jSONSerializationToolStripMenuItem.Size = new Size(144, 24);
            jSONSerializationToolStripMenuItem.Text = "JSON Serialization";
            // 
            // serializeToolStripMenuItem2
            // 
            serializeToolStripMenuItem2.Name = "serializeToolStripMenuItem2";
            serializeToolStripMenuItem2.Size = new Size(165, 26);
            serializeToolStripMenuItem2.Text = "Serialize";
            serializeToolStripMenuItem2.Click += serializeToolStripMenuItem2_Click;
            // 
            // deserializeToolStripMenuItem2
            // 
            deserializeToolStripMenuItem2.Name = "deserializeToolStripMenuItem2";
            deserializeToolStripMenuItem2.Size = new Size(165, 26);
            deserializeToolStripMenuItem2.Text = "Deserialize";
            deserializeToolStripMenuItem2.Click += deserializeToolStripMenuItem2_Click;
            // 
            // TextFile
            // 
            TextFile.DropDownItems.AddRange(new ToolStripItem[] { btnExport });
            TextFile.Name = "TextFile";
            TextFile.Size = new Size(73, 24);
            TextFile.Text = "TextFile";
            // 
            // btnExport
            // 
            btnExport.Name = "btnExport";
            btnExport.Size = new Size(135, 26);
            btnExport.Text = "Export";
            btnExport.Click += btnExport_Click;
            // 
            // contextMenuStrip1
            // 
            contextMenuStrip1.ImageScalingSize = new Size(20, 20);
            contextMenuStrip1.Name = "contextMenuStrip1";
            contextMenuStrip1.Size = new Size(61, 4);
            // 
            // btnEdit
            // 
            btnEdit.Location = new Point(545, 388);
            btnEdit.Name = "btnEdit";
            btnEdit.Size = new Size(89, 44);
            btnEdit.TabIndex = 14;
            btnEdit.Text = "Edit";
            btnEdit.UseVisualStyleBackColor = true;
            btnEdit.Click += btnEdit_Click;
            // 
            // btnDelete
            // 
            btnDelete.Location = new Point(667, 388);
            btnDelete.Name = "btnDelete";
            btnDelete.Size = new Size(86, 44);
            btnDelete.TabIndex = 15;
            btnDelete.Text = "Delete";
            btnDelete.UseVisualStyleBackColor = true;
            btnDelete.Click += btnDelete_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            AutoValidate = AutoValidate.EnableAllowFocusChange;
            ClientSize = new Size(800, 450);
            Controls.Add(btnDelete);
            Controls.Add(btnEdit);
            Controls.Add(lvParticipants);
            Controls.Add(button1);
            Controls.Add(dtpBirthDate);
            Controls.Add(tbFirstName);
            Controls.Add(tbLastName);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(menuStrip1);
            MainMenuStrip = menuStrip1;
            Name = "Form1";
            Text = "Form1";
            FormClosing += Form1_FormClosing;
            Load += Form1_Load;
            ((System.ComponentModel.ISupportInitialize)errorProvider).EndInit();
            menuStrip1.ResumeLayout(false);
            menuStrip1.PerformLayout();
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
        private MenuStrip menuStrip1;
        private ToolStripMenuItem BinarySerialization;
        private ToolStripMenuItem btnSerializeBinary;
        private ToolStripMenuItem btnDeserializeBinary;
        private ToolStripMenuItem XMLSerialization;
        private ToolStripMenuItem btnSerializeXML;
        private ToolStripMenuItem btnDeserializeXML;
        private ContextMenuStrip contextMenuStrip1;
        private ToolStripMenuItem jSONSerializationToolStripMenuItem;
        private ToolStripMenuItem serializeToolStripMenuItem2;
        private ToolStripMenuItem deserializeToolStripMenuItem2;
        private ToolStripMenuItem TextFile;
        private ToolStripMenuItem btnExport;
        private Button btnDelete;
        private Button btnEdit;
    }
}
