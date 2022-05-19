using System;
using System.Collections.Generic;
using System.Text;

namespace Laboratory14
{
    class Article : Edition //статья
    {
        public string Name;
        public string LastName;
        public int Number;
        public int Year
        {
            set
            {
                if (value <= 2019)
                    Year = value;
                else Console.WriteLine("Некорректная дата издания статьи");
            }
        }
        public string MagazineName;
        public Article(string name, string lastName, string magazineName, int number, int year)
        {
            this.Name = name;
            this.LastName = lastName;
            this.MagazineName = magazineName;
            this.Number = number;
            this.Year = year;
        }
        public Article()
        {

        }
        public override void Info()
        {
            Console.WriteLine("Введите название статьи");
            Name = Console.ReadLine();
            Console.WriteLine("Введите фамилию автора");
            LastName = Console.ReadLine();
            Console.WriteLine("Введите название журнала");
            MagazineName = Console.ReadLine();
            Console.WriteLine("Введите номер журнала");
            Number = int.Parse(Console.ReadLine());
            Console.WriteLine("Введите год издания журнала");
            Year = int.Parse(Console.ReadLine());
        }
        public override void Desired(string LASTName)
        {
            if (LastName == LASTName) Console.WriteLine($"Данное издание принадлежит автору: {LastName}");
        }
    }
}
