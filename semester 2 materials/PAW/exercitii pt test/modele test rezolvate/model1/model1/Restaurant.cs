using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace model1
{
    public class Restaurant { 
        List<Waiter> waiter;
        public Restaurant() { 
            waiter = new List<Waiter>();
        }

        public void addWaiter(Waiter newWaiter)
        {
            waiter.Add(newWaiter);
        }

        public List<Waiter> Waiters => waiter;
    }
}
