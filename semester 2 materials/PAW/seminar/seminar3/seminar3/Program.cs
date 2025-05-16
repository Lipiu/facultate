using System;

namespace myProgram
{
    class Program
    {

        private static void ListExample()
        {
            // New string-typed list
            var words = new List<string>();
            words.Add("melon");
            words.Add("avocado");
            words.AddRange(new[] { "banana", "plum" });

            // Insert at start
            words.Insert(0, "lemon");

            // Insert at start
            words.InsertRange(0, new[] { "peach", "nashi" });
            words.Remove("melon");

            words.RemoveAt(3);

            words.RemoveRange(0, 2);

            words.RemoveAll(x => x.StartsWith("n"));

            for (var i = 0; i < words.Count; i++)
            {
                Console.WriteLine(words[i]);
            }

            foreach (var word in words)
            {
                Console.WriteLine(word);
            }
        }
        internal class Person
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

            public override string ToString()
            {
                return string.Format("Name: {0}, Age: {1}", Name, Age);
            }
        }

        private static void ListPersonExample()
        {
            var personList = new List<Person>();

            var rnd = new Random();
            for (var i = 0; i < 10; i++)
            {
                personList.Add(new Person("Persoana " + i, rnd.Next(100)));
            }

            //Which interface is needed for Array.Sort(personList)

            foreach (var p in personList) //equivalent to foreach (Person p in personList)
                Console.WriteLine(p);
        }
        static void Main(string[] args)
        {
            ListPersonExample();


        }

    }
}