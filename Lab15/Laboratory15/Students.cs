using System;
using System.Collections.Generic;
using System.Text;

namespace Lab_16
{
    class Student : Totality
    {
        string Mark;
        public Student()
        {

        }
        public Student(string name, string lastname, string mark) : base (name, lastname)
        {
            this.Mark = mark;
        }
        public override bool Proverka()
        {
            bool f1 = false;
            bool f2 = false;
            bool ff = false;
            Console.WriteLine("Студент учится на бюджете?");
            string c = Console.ReadLine();

            while (c.ToLower() != "да")
            {
                if (c.ToLower() == "нет")
                    break;
            }
            if (c.ToLower() == "да")
                f1 = true;
            else
                f1 = false;

            Console.WriteLine("Студент проживает в общежитии?");
            c = Console.ReadLine();

            while (c.ToLower() != "да")
            {
                if (c.ToLower() == "нет")
                    break;
            }
            if (c.ToLower() == "да")
                f2 = true;
            else
                f2 = false;
            if (f1 && f2)
              ff = true;
                return ff;
        }
        public string Ratestudent()
        {
            Random rnd = new Random();
            int m = rnd.Next(2, 5); // m присваивается любая оценка от 2 до 5
            if (m == 2) Mark = "неудовлетворительно";
            else if (m == 3) Mark = "удовлетворительно";
            else if (m == 4) Mark = "хорошо";
            else Mark = "отлично";
            return Mark;
        }
        public override void Print()
        {
            Console.WriteLine("Введите имя студента");
            name = Console.ReadLine();
            Console.WriteLine("Введите фамилию студента");
            lastname = Console.ReadLine();
            Console.WriteLine($"Студент {name} {lastname} получил оценку - {Ratestudent()}");
        }
    }
}
