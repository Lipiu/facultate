using System.ComponentModel;
using System.Diagnostics;
using System.Runtime.Intrinsics.X86;
using System.Runtime.Serialization.Formatters.Binary;
using System.Xml.Serialization;
using WinFormsApp11.Entities;
using Newtonsoft.Json;
using Microsoft.VisualBasic.Devices;


namespace WinFormsApp11
{

    public partial class Form1 : Form
    {
        #region Properties
        private List<Participant> _participants;
        private readonly MainFormViewModel _viewModel;

        #endregion
        public Form1()
        {
            InitializeComponent();

            _participants = new List<Participant>();
            _viewModel = new MainFormViewModel();


        }


        public void DisplayParticipants()
        {

        }


        #region Events
        private void btnAdd_Click(object sender, EventArgs e)
        {
            _viewModel.AddParticipant();

        }
        #endregion

        private void tbFirstName_TextChanged(object sender, EventArgs e)
        {

        }

        private void tbLastName_TextChanged(object sender, EventArgs e)
        {

        }
        private bool IsLastNameValid()
        {
            return string.IsNullOrWhiteSpace(tbLastName.Text.Trim());
        }

        private void tbFirstName_Validating(object sender, CancelEventArgs e)
        {

        }

        private void tbLastName_Validating(object sender, CancelEventArgs e)
        {
            if (IsLastNameValid())
            {
                e.Cancel = true; //prevents the user from changing the focus to another control
                errorProvider.SetError((Control)sender, "Last Name is empty!");

            }
        }

        private void tbLastName_Validated(object sender, EventArgs e)
        {
            errorProvider.SetError((Control)sender, string.Empty);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (!ValidateChildren())
            {
                MessageBox.Show("The form contains errors!",
                    "Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);

                return;
            }

        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            dgvParticipants.DataSource = _viewModel.Participants;

            //tbLastName.DataBindings.Add("Text", _viewModel, "LastName");
            //Recommended (without magic strings):
            tbLastName.DataBindings.Add("Text", _viewModel, nameof(MainFormViewModel.LastName));

            tbFirstName.DataBindings.Add("Text", _viewModel, "FirstName");
            dtpBirthDate.DataBindings.Add("Value", _viewModel, "BirthDate");
        }

        private void btnSerializeBinary_Click(object sender, EventArgs e)
        {
            fcnSerializeBinary();
        }

        private void fcnSerializeBinary()
        {
            BinaryFormatter formatter = new BinaryFormatter();
            using (FileStream stream = File.Create("serialized.bin"))
                formatter.Serialize(stream, _participants);
        }
        private void btnSerializeXML_Click(object sender, EventArgs e)
        {
            XmlSerializer serializer = new XmlSerializer(typeof(List<Participant>));

            using (FileStream stream = File.Create("SerializedXML.xml"))
                serializer.Serialize(stream, _participants);
        }

        private void btnDeserializeXML_Click(object sender, EventArgs e)
        {
            XmlSerializer serializer = new XmlSerializer(typeof(List<Participant>));

            using (FileStream stream = File.OpenRead("SerializedXML.xml"))
            {
                _participants = (List<Participant>)serializer.Deserialize(stream);
                DisplayParticipants();
            }
        }

        private void fcnDeserilizeBinary()
        {
            XmlSerializer serializer = new XmlSerializer(typeof(List<Participant>));
            using (FileStream stream = File.OpenRead("SerializedXML.xml"))
            {
                _participants = (List<Participant>)serializer.Deserialize(stream);
                DisplayParticipants();
            }
        }

        private void btnDeserializeBinary_Click(object sender, EventArgs e)
        {
            fcnDeserilizeBinary();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            fcnSerializeBinary();

        }

        private void btnExport_Click(object sender, EventArgs e)
        {
            // Create an instance of the open file dialog box.
            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "Text File | *.csv";
            saveFileDialog.Title = "Save as text file";

            if (saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                //Approach 1
                //StreamWriter sw = new StreamWriter(saveFileDialog.FileName);
                //try
                //{
                //	sw.WriteLine("LastName,FirstName,BirthDate");

                //	foreach (var participant in _participants)
                //	{
                //		sw.WriteLine("{0}, {1}, {2}"
                //			, participant.LastName
                //			, participant.FirstName
                //			, participant.BirthDate.ToShortDateString());
                //	}
                //}
                //finally
                //{
                //	sw.Dispose();
                //}

                //2. Approach 2 - recommended
                // When compiled, this code in this approach is converted to: try{} finally{}
                using (StreamWriter sw = File.CreateText(saveFileDialog.FileName))
                // Equivalent to:
                // using (StreamWriter sw = new StreamWriter(saveFileDialog.FileName))
                {
                    sw.WriteLine("LastName,FirstName,BirthDate");

                    foreach (var participant in _participants)
                    {
                        sw.WriteLine("\"{0}\", \"{1}\", \"{2}\""
                                    , participant.LastName.Replace("\"", "\"\"")
                                    , participant.FirstName.Replace("\"", "\"\"")
                                    , participant.BirthDate.ToShortDateString());
                    }
                }
            }
        }

        private void serializeToolStripMenuItem2_Click(object sender, EventArgs e)
        {
            string json = JsonConvert.SerializeObject(_participants);
            File.WriteAllText("participants.json", json);
        }

        private void deserializeToolStripMenuItem2_Click(object sender, EventArgs e)
        {
            string json = File.ReadAllText("participants.json");
            _participants = JsonConvert.DeserializeObject<List<Participant>>(json);
            DisplayParticipants();
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {

        }

        private void dgvParticipants_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
