using System;
using System.Collections.Generic;
using System.Text;

namespace controlwork
{
    class Worker : IComparable
    {
        string Surname { get; set; }
        string Name { get; set; }
        string Nameofwork {get; set;}
        int Year { get; set;}
        public Worker(string surname, string name, string nameofwork, int year)
        {
            this.Surname = surname;
            this.Name = name;
            this.Nameofwork = nameofwork;
            this.Year = year;
        }
        public int CompareTo(object obj)
        {
            Worker p = obj as Worker;
            if (p != null)
                return this.Surname.CompareTo(Surname);
            else throw new Exception();
        }
        public bool IfTrue(string d)
        {
            if (Surname == d) return true;
            else return false;
        }
        public override string ToString()
        {
            return (Surname + " " + Name + " " + Nameofwork + " " + Year);
        }
    }
}
