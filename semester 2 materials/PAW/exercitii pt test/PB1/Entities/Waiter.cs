using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PB1.Entities
{
    public class Waiter: IComparable<Waiter>
    {
        public string firstName { get; set; }
        public string lastName { get; set; }
        public DateTime birthDate { get; set; }


        public Waiter() { }
        public Waiter(string inFirstName, string inLastName, DateTime inBirthDate)
        {
            firstName = inFirstName;
            lastName = inLastName;
            birthDate = inBirthDate;
        }
        public int CompareTo(Waiter other)
        {
            return birthDate.CompareTo(other.birthDate);
        }
    }

}
