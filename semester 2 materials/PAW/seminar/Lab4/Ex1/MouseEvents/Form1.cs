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

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            string decimalSeparator = CultureInfo.CurrentCulture.NumberFormat.CurrencyDecimalSeparator;

            if (!char.IsDigit(e.KeyChar) && e.KeyChar != (char)8 && e.KeyChar.ToString() != decimalSeparator)
            {
                // Consume this invalid key
                e.Handled = true;
            }
        }

        private void button1_Enter(object sender, EventArgs e)
        {
            int value1 = int.Parse(tbValue1.Text);
            int value2 = int.Parse(tbValue2.Text);
            tbResult.Text = (value1 + value2).ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}
