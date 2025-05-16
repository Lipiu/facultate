using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormsApp11.Entities
{
    internal class Participant
    {
        public string LastName { get; set; }
        public string FirstName { get; set; }
        private DateTime _birthDate;

        #region BirthDate
        public DateTime BirthDate
        {
            get { return _birthDate; }
            set
            {
                if (value >= DateTime.Today)
                    throw new InvalidBirthDateException(value);
                _birthDate = value;
            }
        }
        #endregion

        public Participant(string lastName, string firstName, DateTime birthDate)
        {
            LastName = lastName;
            FirstName = firstName;
            BirthDate = birthDate;
        }

        public static explicit operator TextBox(Participant v)
        {
            throw new NotImplementedException();
        }
    }

    public class InvalidBirthDateException : Exception
    {
        public DateTime BirthDate { get; set; }

        public InvalidBirthDateException(DateTime birthDay)
        {
            BirthDate = birthDay;
        }

        public override string Message
        {
            get
            {
                return "The birthDate " + BirthDate + " is invalid";
            }
        }
    }

}
