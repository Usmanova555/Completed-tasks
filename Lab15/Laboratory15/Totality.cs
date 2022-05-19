using System;
using System.Collections.Generic;
using System.Text;

namespace Lab_16
{
    abstract class Totality
    {
        protected string name;
        protected string lastname;
        string Name { get { return name; } set { name = value; } }
        string Lastname { get { return lastname; } set { lastname = value; } }
        public Totality()
        {

        }
        abstract public bool Proverka();

        public Totality (string name, string lastname)
        {
            this.Name = name;
            this.Lastname = lastname;
        }
        virtual public bool Place()
        {
            bool place = false;
            Console.WriteLine("Работает или учится в университете? Да/Нет");
            string r = Console.ReadLine();

            while (r.ToLower()!="да")
            {
                if (r.ToLower() == "нет")
                    break;
            }
            if (r.ToLower() == "да")
                place = true;
            else place = false;
            return place;
        }
        abstract public void Print();
    } 
}
