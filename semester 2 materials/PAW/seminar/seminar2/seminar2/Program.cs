using System;
using System.Diagnostics;
using System.Text;
using System.Xml.Linq;

namespace MyProject
{
    class Program
    {
        internal class Person : IComparable<Person>
        {
            #region Properties
            public string Name { get; set; }
            public int Age { get; set; }
            #endregion

            public Person(string name, int age)
            {
                Name = name;
                Age = age;
            }

            public int CompareTo(Person other)
            {
                //Note: string.CompareTo is culture-specific
                return Name.CompareTo(other.Name);
            }
        }
        private static void ReferenceTypeArray()
            {
                var p1 = new Person("Name3", 42);
                var p2 = new Person("Name1", 23);
                var p3 = new Person("Name2", 32);

                var pArray = new Person[] { p1, p2, p3 };

                Array.Sort(pArray);

                //IComparable implementation is called automatically by methods such as Array..::.Sort

                foreach (var person in pArray)
                {
                    Console.WriteLine(person);
                }
            }
        static void Main()
        {
            ReferenceTypeArray();
        }
    }
}
