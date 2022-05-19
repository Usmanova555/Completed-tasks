using System;
using System.Collections.Generic;
using System.Text;

namespace classPerson
{
    class Person
    {
        public string LastName { protected set; get; } //доступен из любого места в текущем классе или в производных классах (protected)
        public string Name { protected set; get; } 
        public DateTime Age {protected set; get;}
        int age1;
        char Gender = ' ';
        public char gender
        {
            get
            {
                return Gender;
            }
            set
            {
                if ((value == 'м') || (value == 'ж') || (value == 'М') || (value == 'Ж'))
                    this.Gender = value;
                else Console.WriteLine("Неправильное значение пола, должно быть одно из: М, Ж, м или ж");
            }
        }
        public Person()
        {
            LastName = "";
            Name = "";
            Age = DateTime.MinValue;
            
        }
        public Person(string lastName, string name, string age, char Gender)
        {
            this.LastName = lastName;
            this.Name = name;
            this.Age = DateTime.Parse(age);
            this.Gender = Gender;
            
        }
        public virtual void Read()
        {
            Console.WriteLine("Введите фамилию");
            LastName = Console.ReadLine();
            Console.WriteLine("Введите имя");
            Name = Console.ReadLine();
            Console.WriteLine("Введите дату рождения");
            Age = DateTime.Parse(Console.ReadLine());
            Console.WriteLine("Введите пол");
            while (Gender == ' ')
            {
                gender = char.Parse(Console.ReadLine());
            }
        }
        public int Age1()
        {
            DateTime bday = DateTime.Now;
            if ((bday.Month > Age.Month) || (bday.Month == Age.Month && bday.Day >= Age.Day))
                age1 = bday.Year - Age.Year;
            else age1 = bday.Year - Age.Year - 1;
            return age1;
        }
        public virtual void Print()
        {
            Console.WriteLine("Фамилия - " + LastName);
            Console.WriteLine("Имя - " + Name);
            Console.WriteLine("Возраст - " + Age1());
            Console.WriteLine("Пол - " + Gender);
        }
    }
}
