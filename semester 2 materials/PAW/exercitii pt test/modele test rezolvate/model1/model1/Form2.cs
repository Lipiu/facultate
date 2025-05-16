using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml.Linq;


namespace model1
{
    public partial class Form2 : Form
    {
        private Restaurant restaurant;
        public Form2(Restaurant restaurant)
        {
            InitializeComponent();
            this.restaurant = restaurant;
            errorProvider = new ErrorProvider();
        }

        public Form2() { }

        //define error provider
        private System.Windows.Forms.ErrorProvider errorProvider;


        private void btnAddWaiter_Click(object sender, EventArgs e)
        {
            string name = textBoxName.Text;
            int age;
            string id = textBoxID.Text;
            listView1_SelectedIndexChanged_1(restaurant, e);
            //validating input
            bool isValid = true;
            if (string.IsNullOrEmpty(name))
            {
                errorProvider.SetError(textBoxName, "Invalid name!");
                isValid = false;
            }

            if (!int.TryParse(textBoxAge.Text, out age) || age <= 0)
            {
                errorProvider.SetError(textBoxAge, "Invalid age!");
                isValid = false;
            }

            if (string.IsNullOrEmpty(id))
            {
                errorProvider.SetError(textBoxID, "Invalid ID!");
                isValid = false;
            }

            if (!isValid)
            {
                return;
            }

            Waiter newWaiter = new Waiter(name, age, id);
            restaurant.addWaiter(newWaiter);
            Refresh();

            this.Close();
        }

        private void listView1_SelectedIndexChanged_1(Restaurant restaurant, EventArgs e)
        {
            throw new NotImplementedException();
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }
    }
}
