using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace model1
{
    public class Waiter {
        public string name { get; set; }
        public int age { get; set; }
        public string id { get; set; }

        //constructor without parameters
        public Waiter()
        {
            this.name = "";
            this.age = 0;
            this.id = "";
        }

        //constructor with parameters
        public Waiter(string name, int age, string id)
        {
            this.name = name;
            this.age = age;
            this.id = id;
        }

        public void getInfo()
        {
            System.Console.WriteLine($"Name: {name}\nAge: {age}\nID: {id}");
        }
    }
}
