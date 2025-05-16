using System.Globalization;

namespace MouseEvents
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void tbNumericTextBox_TextChanged(object sender, EventArgs e)
        {

        }
        private void tbNumericTextBox_KeyPress(object sender, KeyPressEventArgs e)
        {
            string decimalSeparator = CultureInfo.CurrentCulture.NumberFormat.CurrencyDecimalSeparator;

            if (!char.IsDigit(e.KeyChar) && e.KeyChar != (char)8 && e.KeyChar.ToString() != decimalSeparator)
            {
                // Consume this invalid key
                e.Handled = true;
            }
        }
    }
}
