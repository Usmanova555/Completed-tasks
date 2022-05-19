using System;
using System.Collections.Generic;
using System.Text;

namespace Lab_16
{
    class Teacher : Totality
    {
        string Subject;
        public Teacher()
        {

        }
        public Teacher(string name, string lastname, string subject) : base (name, lastname)
        {
            this.Subject = subject;
        }
        public override bool Proverka()
        {
            bool ff = false;
            Console.WriteLine("Учитель проживает в Казани?");
            string c = Console.ReadLine();

            while (c.ToLower() != "да")
            {
                if (c.ToLower() == "нет")
                    break;
            }
            if (c.ToLower() == "да")
                ff = true;
            else
                ff = false;
            return ff;
        }
        public string Subjectt()
        {
            Console.WriteLine("Введите название предмета");
            Subject = Console.ReadLine();
            return Subject.ToLower();
        }
        public override void Print()
        {
            Console.WriteLine("Введите имя преподавателя");
            name = Console.ReadLine();
            Console.WriteLine("Введите фамилию преподавателя");
            lastname = Console.ReadLine();
            Console.WriteLine($"Преподаватель {name} {lastname} преподаёт предмет - {Subjectt()}");
        }
    }
}
