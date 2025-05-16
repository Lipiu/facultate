namespace model1
{
    public partial class Form1 : Form2
    {
        public Restaurant Restaurant { get; set; }
        public Form1()
        {
            InitializeComponent();
            Restaurant = new Restaurant();

            listView1.View = View.Details;
            listView1.Columns.Add("Name");
            listView1.Columns.Add("Age");
            listView1.Columns.Add("ID");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form2 addWaiterForm = new Form2(Restaurant);
            addWaiterForm.Show();
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        public void listView1_SelectedIndexChanged_1(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
