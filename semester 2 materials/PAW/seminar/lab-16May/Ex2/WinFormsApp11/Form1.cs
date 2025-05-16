using System.ComponentModel;
using System.Diagnostics;
using System.Runtime.Intrinsics.X86;
using System.Runtime.Serialization.Formatters.Binary;
using System.Xml.Serialization;
using WinFormsApp11.Entities;
using Newtonsoft.Json;
using Microsoft.VisualBasic.Devices;
using System.Data.SQLite;

namespace WinFormsApp11
{
    public partial class Form1 : Form
    {
        #region Properties
        private List<Participant> _participants;
        #endregion
        private const string ConnectionString = "Data Source=database.db";

        public Form1()
        {
            InitializeComponent();

            _participants = new List<Participant>();

        }

        private void DeleteParticipant(Participant participant)
        {
            const string query = "DELETE FROM Participant WHERE Id=@id";

            using (SQLiteConnection connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();

                //Remove from the database
                SQLiteCommand command = new SQLiteCommand(query, connection);
                command.Parameters.AddWithValue("@id", participant.id);

                command.ExecuteNonQuery();

                //Remove from the local copy
                _participants.Remove(participant);
            }
        }

        private void LoadParticipants()
        {
            const string query = "SELECT * FROM Participant";

            using (SQLiteConnection connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();

                var command = new SQLiteCommand(query, connection);

                using (SQLiteDataReader reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        long id = (long)reader["Id"];
                        string lastName = (string)reader["LastName"];
                        string firstName = (string)reader["FirstName"];
                        DateTime birthDate = DateTime.Parse((string)reader["BirthDate"]);

                        Participant participant = new Participant(id, lastName, firstName, birthDate);
                        _participants.Add(participant);
                    }
                }
            }
        }
        public void DisplayParticipants()
        {
            lvParticipants.Items.Clear();

            foreach (Participant participant in _participants)
            {
                var listViewItem = new ListViewItem(participant.LastName);
                listViewItem.SubItems.Add(participant.FirstName);
                listViewItem.SubItems.Add(participant.BirthDate.ToShortDateString());

                //approximate calculation of the age 
                listViewItem.Tag = participant;

                lvParticipants.Items.Add(listViewItem);
            }
        }

        private void AddParticipant(Participant participant)
        {
            var query = "insert into Participant(LastName, FirstName, BirthDate)" +
                                " values(@lastName,@firstName,@birthDate);  " +
                                "SELECT last_insert_rowid()";

            using (SQLiteConnection connection = new SQLiteConnection(ConnectionString))
            {
                connection.Open();

                //1. Add the new participant to the database
                var command = new SQLiteCommand(query, connection);
                command.Parameters.AddWithValue("@lastName", participant.LastName);
                command.Parameters.AddWithValue("@firstName", participant.FirstName);
                command.Parameters.AddWithValue("@birthDate", participant.BirthDate);

                participant.id = (long)command.ExecuteScalar();

                //2. Add the new participants to the local collection
                _participants.Add(participant);
            }
        }
        #region Events
        private void btnAdd_Click(object sender, EventArgs e)
        {
            var lastName = tbLastName.Text;
            var firstName = tbFirstName.Text;
            var birthDate = dtpBirthDate.Value;

            var participant = new Participant(lastName, firstName, birthDate);

            try
            {
                AddParticipant(participant);
                DisplayParticipants();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
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
            try
            {
                LoadParticipants();
                DisplayParticipants();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

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
            if (lvParticipants.SelectedItems.Count == 0)
            {
                MessageBox.Show("Choose a participant");
                return;
            }

            if (MessageBox.Show("Are you sure?", "Delete participant", MessageBoxButtons.YesNo, MessageBoxIcon.Warning) == DialogResult.Yes)
            {
                try
                {
                    ListViewItem selectedItem = lvParticipants.SelectedItems[0];
                    Participant participant = (Participant)selectedItem.Tag;

                    DeleteParticipant(participant);

                    DisplayParticipants();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }

        private void btnEdit_Click(object sender, EventArgs e)
        {
            if (lvParticipants.SelectedItems.Count == 0)
            {
                MessageBox.Show("Choose a participant");
                return;
            }

            EditForm editForm = new EditForm((Participant)lvParticipants.SelectedItems[0].Tag);
            if (editForm.ShowDialog() == DialogResult.OK)
                DisplayParticipants();
        }
    }
}
