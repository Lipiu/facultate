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
        public long id {  get; set; }
        public string LastName { get; set; }
        public string FirstName { get; set; }
        public DateTime BirthDate { get; set; }


        public Participant(long id, string lastName, string firstName, DateTime birthDate)
        {
            this.id = id;
            LastName = lastName;
            FirstName = firstName;
            BirthDate = birthDate;
        }
        public Participant(string lastName, string firstName, DateTime birthDate)
        {
            LastName = lastName;
            FirstName = firstName;
            BirthDate = birthDate;
        }
        public Participant()
        {

        }
    }

}
