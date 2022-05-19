using System;
using System.Collections.Generic;
using System.Text;

namespace Laboratory14
{
    class Book : Edition
    {
        public string Name;
        public string LastName;
        public int Year;
        public string Izd;
        public Book(string name, string lastName, int year, string izd)
        {
            this.Name = name;
            this.LastName = lastName;
            this.Year = year;
            this.Izd = izd;
        }
        public Book()
        {

        }
        public override void Info()
        {
            Console.WriteLine("Введите название книги");
            Name = Console.ReadLine();
            Console.WriteLine("Введите фамилию автора");
            LastName = Console.ReadLine();
            Console.WriteLine("Введите год издания книги");
            Year = int.Parse(Console.ReadLine());
            Console.WriteLine("Введите название издательства");
            Izd = Console.ReadLine();

        }
        public override void Desired(string LASTName)
        {
            if (LastName == LASTName) Console.WriteLine($"Данное издание принадлежит автору: {LastName}");
        }
    }
}
