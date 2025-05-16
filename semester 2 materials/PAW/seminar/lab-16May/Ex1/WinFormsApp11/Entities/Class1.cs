using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormsApp11.Entities
{
    [Serializable]

    public class Participant
    {
        public string LastName { get; set; }
        public string FirstName { get; set; }
        public DateTime BirthDate { get; set; }
        public long ID { get; internal set; }

        public Participant(string lastName, string firstName, DateTime birthDate)
        {
            LastName = lastName;
            FirstName = firstName;
            BirthDate = birthDate;
        }

        public Participant(long id, string lastName, string firstName, DateTime birthDate)
        {
            this.ID = id;
            LastName = lastName;
            FirstName = firstName;
            BirthDate = birthDate;
        }
        public Participant()
        {

        }
    }

}
