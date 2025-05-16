using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using WinFormsApp11.Entities;

namespace WinFormsApp11
{
    public partial class EditForm : Form
    {
        private readonly Participant _participant;
        public EditForm(Participant participant)
        {
            _participant = participant;
            InitializeComponent();
        }
        private void EditForm_Load(object sender, System.EventArgs e)
        {
            tbLastName.Text = _participant.LastName;
            tbFirstName.Text = _participant.FirstName;
            dtpBirthDate.Value = _participant.BirthDate;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            _participant.LastName = tbLastName.Text;
            _participant.FirstName = tbFirstName.Text;
            _participant.BirthDate = dtpBirthDate.Value;
        }

        private void labelFirstName_Click(object sender, EventArgs e)
        {

        }
    }
}
