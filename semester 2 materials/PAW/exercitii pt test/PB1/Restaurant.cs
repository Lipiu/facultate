using PB1.Entities;

namespace PB1
{
    public partial class Restaurant : System.Windows.Forms.Form
    {
        List<Waiter> _waiters;

        public Restaurant()
        {
            InitializeComponent();
            _waiters = new List<Waiter>();
        }

        public void DisplayWaiters()
        {
            lvWaiters.Items.Clear();
            foreach (Waiter waiter in _waiters)
            {
                var item = new ListViewItem(waiter.firstName);
                item.SubItems.Add(waiter.lastName);
                item.SubItems.Add(waiter.birthDate.ToShortDateString());

                item.Tag = waiter;

                lvWaiters.Items.Add(item);
            }
        }

        private void btnAddParticipant_Click(object sender, EventArgs e)
        {
            AddForm newAdd = new AddForm();

            if (newAdd.ShowDialog() == DialogResult.OK)
            {
                Waiter newW = newAdd.newWaiter;
                _waiters.Add(newW);
                DisplayWaiters();
            }
        }
        private void btnSortByBirthDate_Click(object sender, EventArgs e)
        {
            _waiters.Sort();
            DisplayWaiters();
        }
    }
}
