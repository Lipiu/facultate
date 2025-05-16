using System.ComponentModel;
using System.Diagnostics;
using System.Runtime.Intrinsics.X86;
using WinFormsApp11.Entities;

namespace WinFormsApp11
{
    public partial class Form1 : Form
    {
        #region Properties
        private List<Participant> _participants;
        #endregion
        public Form1()
        {
            InitializeComponent();

            _participants = new List<Participant>();

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
                if ((DateTime.Now - participant.BirthDate).TotalDays / 365 >= 18)
                    listViewItem.ImageKey = "adult.png";
                else
                    listViewItem.ImageKey = "child.png";

                lvParticipants.Items.Add(listViewItem);
            }
        }


        #region Events
        private void btnAdd_Click(object sender, EventArgs e)
        {
            string firstName = tbFirstName.Text;
            string lastName = tbLastName.Text;
            DateTime birthDate = dtpBirthDate.Value;

            var participant = new Participant(lastName, firstName, birthDate);
            _participants.Add(participant);

            DisplayParticipants();
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

        private void listView1_SelectedIndexChanged_1(object sender, EventArgs e)
        {

        }
    }
}
