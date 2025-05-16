using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using PB1.Entities;

namespace PB1
{
    public partial class AddForm : Form
    {
        public Waiter newWaiter { get; set; }
        public AddForm()
        {
            InitializeComponent();
            newWaiter = new Waiter();
        }




        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void AddForm_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string firstName = tbFirstName.Text.Trim();
            string lastName = tbLastName.Text.Trim();
            DateTime birthDate = dtpBirthDate.Value;

            newWaiter = new Waiter(firstName, lastName, birthDate);

            DialogResult = DialogResult.OK;
            Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void tbFirstName_Validating(object sender, CancelEventArgs e)
        {
            if (!IsFirstNameValid())
            {
                e.Cancel = true;
                errorProvider.SetError((Control)sender, "First name is wrong!");
            }
            else
                errorProvider.SetError((Control)sender, string.Empty);

        }
        private bool IsFirstNameValid()
        {
            if (string.IsNullOrEmpty(tbFirstName.Text.Trim()) == false)
                return true;
            return false;
        }

        private void dtpBirthDate_Validating(object sender, CancelEventArgs e)
        {
            if (!IsBirthDateValid())
            {
                e.Cancel = true;
                errorProvider.SetError((Control)sender, "The date is in the future!");

            }
            else
                errorProvider.SetError((Control)sender, string.Empty);

        }
        private bool IsBirthDateValid()
        {
            if (dtpBirthDate.Value <= DateTime.Today)
                return true;
            return false;
        }

        private void tbLastName_Validating(object sender, CancelEventArgs e)
        {
            if (!IsLastNameValid())
            {
                e.Cancel = true;
                errorProvider.SetError((Control)sender, "Last name is wrong!");
            }
            else
                errorProvider.SetError((Control)sender, string.Empty);
        }
        private bool IsLastNameValid()
        {
            if (string.IsNullOrEmpty(tbLastName.Text.Trim()) == false)
                return true;
            return false;
        }
    }
}
